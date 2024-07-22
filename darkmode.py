import streamlit as st

def toggle_theme():
  """Toggles the theme of the Streamlit app between light and dark."""
  if "theme" not in st.session_state:
    st.session_state.theme = "light"

  if st.session_state.theme == "light":
    st.session_state.theme = "dark"
    # Set dark theme options
    st.config.set_option("theme.base", "dark")
    st.config.set_option("theme.backgroundColor", "#121212")
    st.config.set_option("theme.primaryColor", "#6777ef")
    st.config.set_option("theme.textColor", "white")
    st.config.set_option("theme.secondaryBackgroundColor", "#262730")
  else:
    st.session_state.theme = "light"
    # Set light theme options
    st.config.set_option("theme.base", "light")
    st.config.set_option("theme.backgroundColor", "white")
    st.config.set_option("theme.primaryColor", "#5591f5")
    st.config.set_option("theme.textColor", "#0a1464")
    st.config.set_option("theme.secondaryBackgroundColor", "# ffffff")
    #82E1D7"
  # Force a rerun to apply the theme changes
  st.experimental_rerun()  # Requires Streamlit >= 1.1.0