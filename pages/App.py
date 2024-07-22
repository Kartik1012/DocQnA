import streamlit as st
from PyPDF2 import PdfReader
import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from langchain_community.document_loaders import UnstructuredURLLoader
import darkmode
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
genai.GenerationConfig(temperature=0.4)
model=genai.GenerativeModel("gemini-pro")

def get_response_doc(doc):
    text=""
    for pdf in doc:
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text
def get_response_url(urls):
    text = ""
    loader = UnstructuredURLLoader(urls=urls)  # Correct initialization with the list of URLs
    data = loader.load()  # Load data from all URLs

    for document in data:
        text += document.page_content  # Concatenate text from each loaded document

    return text

def get_chunk_text(text):
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    chunk=text_splitter.split_text(text)
    return chunk

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template="""
    Answer the questions as detailed as possible form provided , make sure to provide all details ,if answer is not in 
    provided context just say "your given question isn't in direct context of documnet" , don't provide the wrong answer
    context:\n{context}?\n
    Question:\n{question}\n
    Answer:
    """
    model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.5)
    prompt=PromptTemplate(template=prompt_template,input_variable=["context","question"])
    chain=load_qa_chain(model,chain_type="stuff",prompt=prompt)
    return chain

def user_input(question):
    embedding=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    new_db=FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)
    doc=new_db.similarity_search(question)
    chain=get_conversational_chain()

    response=chain(
        {"input_documents":doc,"question":question},
        return_only_outputs=True
    )
    print(response)
    st.subheader("Your Response ")
    st.write(response["output_text"])

def main():
    st.set_page_config("*DocQnA*")
    st.header("DocQnA")
    user_question=st.text_input("Ask Questions from given doc files")

    if user_question:
        user_input(user_question)
    with st.sidebar:
        if st.button("Toggle Dark Mode"):
            darkmode.toggle_theme()
        st.title("Menu")
        option = st.selectbox("Choose an option", ("Upload PDF", "Upload URL"))

        if option == "Upload PDF":
            pdf_doc = st.file_uploader("Upload your document files(.pdf,.doc) here and click on submit after upload.", type=["pdf", "doc"],
                                       accept_multiple_files=True)
            if st.button("Submit PDF"):
                with st.spinner("Processing..."):
                    if pdf_doc is not None:
                        raw_text = get_response_doc(pdf_doc)
                        text_chunk = get_chunk_text(raw_text)
                        get_vector_store(text_chunk)
                        st.success("Done")
                    else:
                        st.error("Please upload a PDF document.")

        elif option == "Upload URL":
            try:
                n = int(st.text_input("Enter number of URLs"))
                urls = []
                for i in range(n):
                    url = st.text_input(f"Enter URL {i + 1} here:")
                    urls.append(url)
                if st.button("Submit URLs"):
                    with st.spinner("Processing..."):
                        if any(urls):
                            result = get_response_url(urls)
                            text_chunk = get_chunk_text(result)
                            get_vector_store(text_chunk)
                            st.success("Done")
                        else:
                            st.error("Please enter at least one URL.")

            except ValueError:
                st.error("Please enter a valid number for the number of URLs.")




if __name__ == "__main__":
    main()

