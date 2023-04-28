import numpy as np
import streamlit as st
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

with tab1:
    user_input = st.text_area(label=":green[Welcome to CHIRP CHAT! Type in your bird-brained questions]")
    
with tab2:
   if uploaded_file is not None:
    st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

#CLASSIFICATION
model = VGG16(weights='imagenet')
img = uploaded_file
x = np.array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

# Make predictions
preds = model.predict(x)

# Decode the predictions
decoded_preds = decode_predictions(preds, top=1)[0]
print('Predictions:')
for pred in decoded_preds:
     result = pred[1]
