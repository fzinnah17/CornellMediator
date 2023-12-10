from transformers import pipeline
import numpy as np
import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-base.en")

# TODO: need to make it cloud based
def transcribe_audio(audio):
    sr, y = audio
    y = y.astype(np.float32)
    y /= np.max(np.abs(y))
    transcription = transcriber({"sampling_rate": sr, "raw": y})["text"]
    return transcription
