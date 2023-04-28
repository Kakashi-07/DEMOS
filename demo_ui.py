import streamlit as st
import os

st.set_page_config(page_title="CHIRP CHAT",
                  page_icon="🐥",
                  layout="wide",
                  initial_sidebar_state="expanded")

#st.title(':orange[CHIRP CHAT]')
#st.markdown("<h1 style='text-align: center;'>:orange[CHIRP CHAT]</h1>", unsafe_allow_html=True,)
st.markdown("<h1 style='text-align: center; color: orange;'>CHIRP CHAT 🐥 </h1> ", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["CHAT HERE 💬", " Uploaded Documents 📄"])

with tab1:
    user_input = st.text_area(label=":green[Welcome to CHIRP CHAT! Type in your bird-brained questions]")
    
with tab2:
   if uploaded_file is not None:
    st.image(image, caption='Uploaded Image.', use_column_width=True)

if not os.path.exists("./tempfolder"):
    os.makedirs("./tempfolder")
    
def save_uploadedfile(uploadedfile):
    with open(
        os.path.join("tempfolder", uploadedfile.name),
        "wb",
    ) as f:
        f.write(uploadedfile.getbuffer())
    return st.sidebar.success("Saved File")


# Creating Sidebar for Utilites
with st.sidebar:
    st.title("Upload Your Birdie")
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg"])
    clear_button = st.button("Clear Conversation", key="clear")
    
