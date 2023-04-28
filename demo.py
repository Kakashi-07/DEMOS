import streamlit as st
from langchain.document_loaders.image import UnstructuredImageLoader
from langchain.vectorstores import Chroma
from langchain.prompts import PromptTemplate

st.set_page_config(page_title="Endangered Bird Voice Identifier")

st.sidebar.title("SeLeCt YoUr ChOiCe")
options = [
    "Image Recognition",
    "Audio Recognition",
]

choice = st.sidebar.radio("Select the method you want", options)

if choice == "Image Recognition":
    Uploaded_file = st.file_uploader(
        "Upload the Image File", type=["jpg", "png"])
    if Uploaded_file is None:
        st.header(" File format not supported!! ")

    st.image(Uploaded_file, caption='YOUR IMAGE')

elif choice == "Audio Recognition":
    Uploaded_file = st.file_uploader(
        "Upload the Image File", type=["mp3", "wav"])
    if Uploaded_file is None:
        st.header(" File format not supported!! ")

    audio_bytes = Uploaded_file.read()
    st.audio(Uploaded_file)
    sample_rate = 44100  # 44100 samples per second
    seconds = 2  # Note duration of 2 seconds
    frequency_la = 440  # Our played note will be 440 Hz
    # Generate array with seconds*sample_rate steps, ranging between 0 and seconds
    t = np.linspace(0, seconds, seconds * sample_rate, False)
    # Generate a 440 Hz sine wave
    note_la = np.sin(frequency_la * t * 2 * np.pi)
    st.audio(note_la, sample_rate=sample_rate)
    
def PDF_loader(document):
    loader = OnlinePDFLoader(document)
    documents = loader.load()
    prompt_template = """ 
    Your are an AI Chatbot devolped to help users to talk to a PDF document.Use the following pieces of context to answer the question at the end.Greet Users!!
    {context}
    {question}
    """
    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    chain_type_kwargs = {"prompt": PROMPT}
    texts = text_splitter.split_documents(documents)
    global db
    db = Chroma.from_documents(texts, embeddings)
    retriever = db.as_retriever()
    global qa
    qa = RetrievalQA.from_chain_type(
        llm=Cohere(
            model="command-xlarge-nightly",
            temperature=temp_r,
            cohere_api_key=st.secrets["cohere_apikey"],
        ),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs=chain_type_kwargs,
    )
    return "Ready"
