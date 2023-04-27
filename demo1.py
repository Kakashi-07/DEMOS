import streamlit as st

st.set_page_config(page_title="Endangered Bird Voice Identifier")

st.sidebar.title("SeLeCt YoUr ChOiCe")
options = [
    "Image Recognition",
    "Audio Recognition",
]

choice = st.sidebar.radio("Select the method you want", options)

if choice == "Image Recognition":
   Uploaded_file =  st.file_uploader("Upload the Image File", type = ["jpg", "png"])    
    if Uploaded_file is None:
        st.header(" File format not supported!! ")
    
   st.image(Uploaded_file, caption ='YOUR IMAGE')
   
elif choice == "Audio Recognition":
   Uploaded_file =  st.file_uploader("Upload the Image File", type = ["mp3", "wav"])    
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
    
    
 
