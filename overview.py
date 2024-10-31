import streamlit as st
from dotenv import load_dotenv
from Assignment3.Assignment3.loginpage import display_login_page
from home import display_home_page
from registerpage import display_register_page

# Load environment variables
load_dotenv()

def display_overview_page():
    # Initialize session state variables if not already set
    if 'logged_in' not in st.session_state:
        st.session_state['logged_in'] = False
    if 'page' not in st.session_state:
        st.session_state['page'] = 'home'  # Default page

    st.sidebar.title("AI Model Evaluation Tool")
    page = st.sidebar.selectbox("Select an option", ("Home", "Login", "Register"))

    if page == "Home":
        display_home_page()
    elif page == "Login":
        display_login_page()
    elif page == "Register":
        display_register_page()
