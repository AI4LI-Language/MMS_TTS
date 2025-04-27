import torch
import numpy as np
from transformers import VitsModel, AutoTokenizer
import scipy.io.wavfile as wavfile
from IPython.display import Audio

class TextToSpeech:
    def __init__(self, model_name="facebook/mms-tts-vie"):
        """
        Initializes the Text-to-Speech model by loading the pre-trained model and tokenizer.
        """
        # Load the Vietnamese TTS model and tokenizer
        self.model = VitsModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    def to_speech(self, passage):
        # Tokenize the input text
        inputs = self.tokenizer(passage, return_tensors="pt")

        # Generate the speech waveform
        with torch.no_grad():
            outputs = self.model(**inputs)
        
        # Get the waveform as a NumPy array
        waveform = outputs.waveform[0].cpu().numpy()  # Convert to NumPy array
        waveform = waveform.squeeze()
        # Normalize the waveform to [-1, 1]
        waveform = waveform / np.max(np.abs(waveform))  

        # The sample rate used by the model
        sample_rate = self.model.config.sampling_rate
        
        return waveform, sample_rate

# Example usage
if __name__ == "__main__":
    tts = TextToSpeech()
    text = "Đây là dự án xây dựng công cụ và phần mềm ứng dụng trí tuệ nhân tạo để hỗ trợ người khuyết tật hòa nhập cuộc sống."
    waveform, sample_rate = tts.to_speech(text)

    # Save the waveform to a .wav file
    wavfile.write("output.wav", rate=sample_rate, data=(waveform * 32767).astype(np.int16))  # Convert to int16

    # Direct playback in Jupyter (if using Jupyter Notebook)
    Audio(waveform, rate=sample_rate)
