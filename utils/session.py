import streamlit as st

def init_session_state():
    if "qc_history" not in st.session_state:
        st.session_state.qc_history = []