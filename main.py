import streamlit as st
import os
import importlib.util

# Set page title
st.set_page_config(page_title="Multi-Page Streamlit App", layout="wide")

# Sidebar navigation
st.sidebar.title("Navigation")
pages = {
    "Home": "home",
    "About": "about",
    "Contact": "contact",
}

selection = st.sidebar.radio("Go to", list(pages.keys()))

# Load the selected page dynamically
page_module = pages[selection]
page_path = f"features/{page_module}.py"

if os.path.exists(page_path):
    spec = importlib.util.spec_from_file_location(page_module, page_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    module.run()
else:
    st.error("Page not found!")
