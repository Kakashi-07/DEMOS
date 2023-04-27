import streamlit as st
import pandas as pd
import numpy as np
import time
from streamlit_chat import message
import random


# Set page title
st.set_page_config(page_title="Demo Streamlit App")

# Create sidebar
st.sidebar.title("Menu")
options = [
    "Displaying Text",
    "Data Elements",
    "Media Elements",
    "Interactive Input Elements",
    "Chart Elements",
    "Progress and Status Elements",
    "StreamlitChat",
]
choice = st.sidebar.radio("Select an option", options)


if choice == "Displaying Text":
    st.write("Streamlit  Demo")
    st.code("st.text()", language="python")

    st.header("This is Heading 1 in Markdown")
    st.code("st.markdown()", language="python")

    st.title("This is a title")
    st.code("st.title()", language="python")

    st.header("Header")
    st.code("st.header()", language="python")

    st.subheader("Sub Header")
    st.code("st.subheader()", language="python")

    st.latex(r"x^2 + y^2 = z^2")
    st.code("st.latex()", language="python")

    st.write("Streamlit can display a lot of other things too!")
    st.code("st.write()", language="python")

    st.divider()
    st.subheader("Above is a divider")
    st.code("st.divider()", language="python")
