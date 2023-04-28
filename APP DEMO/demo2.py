import cv2
import numpy as np
import streamlit as st
import tensorflow as tf
from langchain import Cohere, ConversationChain, LLMChain, PromptTemplate
from langchain.memory import ConversationBufferWindowMemory
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions, VGG16

st.set_page_config(page_title="Endangered Bird Voice Identifier")

tab1= st.tabs(["📈 Talk Here"])

tab1.markdown(
    "<h1 style='text-align: center;'>Talk With Chatbot</h1>",
    unsafe_allow_html=True,
)

st.sidebar.title("SeLeCt YoUr ChOiCe")
options = [
    "Image Recognition",
]

choice = st.sidebar.radio("Select the method you want", options)

if choice == "Image Recognition":
    Uploaded_file = st.file_uploader(
        "Upload the Image File", type=["jpg", "png"])
    if Uploaded_file is None:
        st.header(" File format not supported!! ")
    st.image(Uploaded_file, caption='YOUR IMAGE')

model = VGG16(weights='imagenet')

img = Uploaded_file
img = cv2.resize(img,(224, 224))
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
     st.subheader(result)
    
def Img_DataGen(Input):
    template = """
    You are an AI Chatbot developed solely to help users to talk about Birds and their information.
    
    {history}
    Human: {human_input}
    Assistant:"""

    prompt1 = PromptTemplate(
    input_variables=["product"],
    template="Generate a paragraph about {product} as if an Ornithologist is saying it.",
    )
    chain = LLMChain(llm=LLM, prompt=prompt1)
    var = chain.run(result)
    
    template = """
        You are an AI Chatbot who acts as a professional Ornithologist. You are designed to be able to assist with a wide range of tasks, from answering simple questions to providing in-depth explanations and discussions. As a language model, you must be able to generate human-like text based on the input it receives, allowing it to engage in natural-sounding conversations and provide responses that are coherent and relevant to the topic at hand.
        Assistant is constantly learning and improving, and its capabilities are constantly evolving. It is able to process and understand large amounts of text, and can use this knowledge to provide accurate and informative responses to a wide range of questions. Additionally, Assistant is able to generate its own text based on the input it receives, allowing it to engage in discussions and provide explanations and descriptions on a wide range of topics.
        Overall, Assistant is a powerful tool that can help with a wide range of tasks and provide valuable insights and information on a wide range of topics. Whether you need help with a specific question or just want to have a conversation about a particular topic, Assistant is here to assist.
        your task is answer any question asked about {result}. some basic info on {result} is: {var}
        """

    prompt = PromptTemplate(
    input_variables=["result","var"], 
    template=template
    )
    
    var = var + """{history}
    Human: {human_input}
    Assistant:"""

    var = prompt.format(result=result, var = var)
    
    global chat
    prompt = PromptTemplate(
    input_variables=["history", "human_input"], 
    template=var
    )

    chat_chain = LLMChain(
    llm = Cohere(cohere_api_key= st.secrets["cohere_apikey"], model="command-xlarge-nightly"), 
    prompt=prompt, 
    verbose=True, 
    memory=ConversationBufferWindowMemory(k=8),
    )
    )
    return "Ready"

if Uploaded_file is not None:
    save_uploadedfile(Uploaded_file)
    Img_DataGen(result)
    )

 # Session State
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
if "generated" not in st.session_state:
    st.session_state["generated"] = []
if "past" not in st.session_state:
    st.session_state["past"] = []
    
user_input = st.text_input("You:", key="input")

# Generating Response
def generate_response(query):
    query = user_input
    if user_input:
        res = chat.predict(human_input = query)
        res = chat({"query": query, "chat_history": st.session_state["chat_history"]})
        res["res"] = res["res"]
        return res["res"]


response_container = tab1.container()
container = tab1.container()


with container:
    with st.form(key="my_form", clear_on_submit=True):
        user_input = st.text_input("You:", key="input")
        submit_button = st.form_submit_button(label="Send")

    if user_input and submit_button:
        if uploaded_file is not None:
            output = generate_response(user_input)
            print(output)
            st.session_state["past"].append(user_input)
            st.session_state["generated"].append(output)
            st.session_state["chat_history"] = [(user_input, output)]
        else:
            st.session_state["past"].append(user_input)
            st.session_state["generated"].append(
                "Please upload the picture!"
            )

if clear_button:
    st.session_state["generated"] = []
    st.session_state["past"] = []
    st.session_state["chat_history"] = []
