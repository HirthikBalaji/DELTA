import streamlit as st
from PIL import Image
import pytesseract
import ollama
import easyocr
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Hirthik Balaji C\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def summarize_text(text, model="llama3.2"):
    prompt = f"Summarize the following text in 250 words:\n\n{text}\n\nSummary:"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()

def perform_ocr(preprocessed_image):
    reader = easyocr.Reader(['en'])  # You can add more langs like ['en', 'hi'] etc.

    result = reader.readtext(preprocessed_image, detail=0)
    return result

def convert_text(text,model='llama3.2'):
    prompt=f"""Convert the following text into a short news report script that sounds like it's being read by a professional news anchor. 

Use formal language, a neutral tone, and a concise reporting style. Begin with a headline, then a lead sentence that captures the essence of the news, followed by 2-3 informative sentences providing more detail.

Keep the report under 100 words. Do not add fake information or speculation. Use only the given text.

Here is the content to convert:
{text}

NEWS REPORT:
"""
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()


st.title("📷 Image to Audio 🎧")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    text = convert_text(summarize_text(perform_ocr(image)))

    st.write(text)
