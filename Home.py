import streamlit as st
import darkmode

st.title("DocQnA")
st.header("About")
text = """**DocQnA** chat-bot, built on the **Gemini API** and **Langchain**, is designed to efficiently handle document files and links.
 We utilize **FAISS (Facebook AI Similarity Search)** for local vector space storage, ensuring fast and accurate similarity searches. The website interface, developed using Streamlit, provides a user-friendly experience.

 The technology stack consists of the Gemini API for advanced natural language processing capabilities, Langchain for effective language model integration, and FAISS for creating and storing vector spaces locally.
 This setup allows for rapid and precise similarity searches. The interface, built with Streamlit, offers an intuitive and interactive friendly web application.


**The chatbot features two main options for users: PDF Upload and URL Upload**.

 •	Users can upload document files (PDFs,Docs) to the chat-bot, which processes the content and allows users to ask questions based on the document's information.

•	Alternatively, users can input URLs, and the chat-bot will extract and process the content from these links, enabling users to query the chatbot with questions related to the extracted information.



This systematic integration of advanced technologies ensures that our chat-bot provides reliable and efficient information retrieval from both documents and links, making it a valuable tool for users seeking quick and accurate information."""
st.write(text)
with st.sidebar:
    if st.button("Toggle Dark Mode"):
        darkmode.toggle_theme()

st.subheader("Project Author: Kartik Tyagi")
st.write("**Contact**")
st.write("\t **Linkdein**: [Linkdein](https://www.linkedin.com/in/kartik-tyagi-311464213/)")
st.write("**Gmail**: [Gmail_ID](kartiktyagi1012@gmail.com)")

# st.page_link("https://aistudio.google.com/app/apikey", label="Google Api key", icon="Google")
st.write("From here you can get your **api key** [🌎_link](https://aistudio.google.com/app/apikey)")

link = "https://www.bing.com/images/search?view=detailV2&ccid=iqkTFFKU&id=30E8F2317205864847E26D9B4E3859D7538E5370&thid=OIP.iqkTFFKU2vukdL9ttQi48QHaEo&mediaurl=https%3a%2f%2fwallpaperaccess.com%2ffull%2f210888.jpg&exph=2400&expw=3840&q=Free+Tech+Wallpaper&simid=608024914440185935&FORM=IRPRST&ck=0C37CECCAC5FA37AF67CE391BC6962DD&selectedIndex=67&itb=0"
