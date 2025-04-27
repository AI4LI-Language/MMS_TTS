import streamlit as st
import torch
import numpy as np
from transformers import VitsModel, AutoTokenizer
import scipy.io.wavfile as wavfile

# Load the model and tokenizer
@st.cache_resource()
def load_model():
    model = VitsModel.from_pretrained("facebook/mms-tts-vie")
    tokenizer = AutoTokenizer.from_pretrained("facebook/mms-tts-vie")
    return model, tokenizer

model, tokenizer = load_model()

st.title("Vietnamese Text-to-Speech Demo")
st.write("Enter a Vietnamese sentence and generate speech!")

text = st.text_input("Enter text:", "Xin chào! Đây là một ví dụ về giọng nói tiếng Việt.")

if st.button("Generate Speech"):
    with st.spinner("Generating audio..."):
        inputs = tokenizer(text, return_tensors="pt")
        
        with torch.no_grad():
            outputs = model(**inputs)
        
        waveform = outputs.waveform[0].cpu().numpy()
        waveform = (waveform * 32767).astype(np.int16)  # Convert to int16
        
        # Save audio file
        audio_filename = "output.wav"
        wavfile.write(audio_filename, rate=model.config.sampling_rate, data=waveform)
        
        st.audio(audio_filename, format="audio/wav")
        st.success("Speech generation complete!")
