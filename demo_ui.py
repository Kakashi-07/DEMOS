import numpy as np
import streamlit as st
from PIL import Image
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16

st.set_page_config(page_title="CHIRP CHAT",
                  page_icon="🐥",
                  layout="wide",
                  initial_sidebar_state="expanded")

#st.title(':orange[CHIRP CHAT]')
#st.markdown("<h1 style='text-align: center;'>:orange[CHIRP CHAT]</h1>", unsafe_allow_html=True,)
st.markdown("<h1 style='text-align: center; color: orange;'>CHIRP CHAT 🐥 </h1> ", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["CHAT HERE 💬", " Uploaded Documents 📄"])

# Creating Sidebar for Utilites
with st.sidebar:
    st.title("Upload Your Birdie")
    uploaded_file = st.file_uploader("Choose a file", type=["png", "jpg"])
    clear_button = st.button("Clear Conversation", key="clear")

 if uploaded_file is not None:
    save_uploadedfile(uploaded_file)
    PDF_loader("tempfolder/" + uploaded_file.name)
    tab1.markdown(
        "<h3 style='text-align: center;'>Now You Are Talking With "
        + uploaded_file.name
        + "</h3>",
        unsafe_allow_html=True,
    )   
    
with tab1:
    user_input = st.text_area(label=":green[Welcome to CHIRP CHAT! Type in your bird-brained questions]")
     
with tab2:
   if uploaded_file is not None:
    uploaded_image = Image.open(uploaded_file)
    x = preprocess_input(np.array(uploaded_image))
    model = VGG16(weights='imagenet')
    #img = uploaded_file
    #x = np.array(img)
    x = np.expand_dims(x, axis=0)
    preds = model.predict(x)
    
    decoded_preds = decode_predictions(preds, top=1)[0]
    for pred in decoded_preds:
      result = pred[1]
    st.image(uploaded_file, caption=result)
    
 with tab1:   
    if uploaded_file is not None:
      tab1.markdown(
        "<h3 style='text-align: center;'>Now you're chirping about the bird "
        + result
        + "</h3>",
        unsafe_allow_html=True,
    )  
