import streamlit as st
from PIL import Image
import ollama
import easyocr
import os

def summarize_text(text, model="llama3.2"):
    prompt = f"Summarize the following text in 250 words:\n\n{text}\n\nSummary:"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()

def perform_ocr(preprocessed_image):
    reader = easyocr.Reader(['en'])  # You can add more langs like ['en', 'hi'] etc.

    result = reader.readtext(preprocessed_image, detail=0)
    return result

def convert_text(text,model='llama3.2'):
    prompt=f"""
You are a battle-hardened military general addressing your troops. Convert the following news summary into a motivational speech or monologue with intensity, purpose, and urgency. Use powerful, commanding language that inspires action and resilience — as if you're delivering this in a war room before a critical mission.

Rules:
- Keep it under 120 words.
- Maintain factual accuracy — do NOT add fake info.
- Start with a punchy headline or call to action.
- Mix short, powerful sentences with dramatic tone.
- Channel the voice of a soldier-leader rallying a nation.

Here is the news summary:
{text}

DELIVER THE SPEECH:
"""
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()



st.title("📷 Image to Audio 🎧")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    with st.spinner("🔍 Performing OCR, summarizing and converting to news..."):
        text = convert_text(summarize_text(perform_ocr(image)))
        os.system(
            f"echo '{text.replace("'", "").replace("\n", ",").replace('"','')}' | wsl ./piper/piper --model ./piper/en_US-hfc_male-medium.onnx --output_file welcome.wav")

    st.write(text)
    if os.path.exists('welcome.wav'):
        audio_file = open("welcome.wav", "rb")
        audio_bytes = audio_file.read()

        st.audio(audio_bytes, format="audio/wav")

