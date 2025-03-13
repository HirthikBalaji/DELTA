from bark import generate_audio, SAMPLE_RATE
import pytesseract
from PIL import Image
import ollama

import scipy

# Optional: path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Hirthik Balaji C\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"


def perform_ocr(preprocessed_image):
    # Convert the OpenCV image to PIL Image for pytesseract
    pil_image = Image.open(preprocessed_image)

    # Run OCR with recommended PSM
    text = pytesseract.image_to_string(pil_image, config='--psm 6')
    return text

def summarize_text(text, model="llama3.2"):
    prompt = f"Summarize the following text in 250 words:\n\n{text}\n\nSummary:"
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    return response['message']['content'].strip()

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




def Generate_audio(text):
    text_prompt = text
    audio_array = generate_audio(text_prompt,history_prompt="v2/en_speaker_6")
    scipy.io.wavfile.write("cm.mp3",rate=SAMPLE_RATE,data=audio_array)


image_path = "Delta Headlines/0e8716f5-03a9-4a7f-aca9-e0941bb48442.jpg"

# ocr_text = perform_ocr(image_path)

print("\nOCR Output:\n")
text = convert_text(summarize_text(perform_ocr(image_path)))
print(text)
Generate_audio(text)




