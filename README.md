# 📷 Image to Audio 🎧 — Motivational News Speech Generator

This Streamlit app transforms **text from an image** into a **motivational speech** with military-style intensity — and then speaks it out loud using text-to-speech synthesis.

## 🚀 Features

- 📸 **Upload Image**: Accepts `.jpg`, `.jpeg`, and `.png` formats.
- 🧠 **OCR (Optical Character Recognition)**: Extracts text from the uploaded image using `easyocr`.
- ✍️ **Summarization**: Summarizes extracted text using an AI model via `ollama` (LLaMA 3.2).
- 🎙 **Speech Conversion**: Transforms the summary into a **motivational military speech**.
- 🔊 **Text-to-Speech (TTS)**: Converts the speech into audio using [Piper TTS](https://github.com/rhasspy/piper).
- 🎧 **Audio Playback**: Streamlit interface plays the generated audio.

---

## 🛠 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/image-to-audio-speech.git
cd image-to-audio-speech
```

### 2. Install Dependencies
Make sure you have Python 3.9+ and virtualenv:

```bash
pip install streamlit easyocr pillow
```

Install and configure:
- [`ollama`](https://ollama.com/) (for local LLM inference)
- [`piper`](https://github.com/rhasspy/piper) (TTS engine)

---

## 🧠 Model Dependencies

### Ollama LLM (LLaMA 3.2)
Ensure `llama3.2` model is pulled and available for chat-based summarization:
```bash
ollama pull llama3.2
```

### Piper TTS
Make sure Piper is installed (via WSL or Linux), and you have a model like `en_US-hfc_male-medium.onnx` in the `./piper/` directory:
```bash
# Inside WSL or Linux terminal
cd piper
./piper --list  # To list available voices
```

---

## 🖼 How It Works

1. Upload an image.
2. The app extracts text using OCR (`easyocr`).
3. It summarizes the text using the LLaMA 3.2 model via `ollama`.
4. The summary is transformed into a powerful motivational speech.
5. Piper TTS synthesizes the speech into an audio file.
6. The audio is played directly in the Streamlit UI.

---

## 🔉 Example Output

<audio controls> <source src="blah" type="audio/wav"> Your browser does not support the audio element. </audio>

---

## ⚙️ File Structure

```
├── app.py                # Main Streamlit application
├── piper/
│   ├── piper             # Piper binary (Linux or WSL)
│   └── en_US-hfc_male-medium.onnx  # TTS voice model
├── welcome.wav           # Output audio file (auto-generated)
```

---

## 🧪 Run the App

```bash
streamlit run app.py
```

---

## 📌 Notes

- The Piper TTS command uses WSL (`wsl ./piper/piper`) — make sure you have WSL set up if on Windows.
- Ensure `ollama` is running as a background service before using the app.
- Piper models can be downloaded from [Piper TTS GitHub](https://github.com/rhasspy/piper#pre-built-models).

---

## 🙌 Credits

- [Streamlit](https://streamlit.io/)
- [EasyOCR](https://github.com/JaidedAI/EasyOCR)
- [Ollama](https://ollama.com/)
- [Piper TTS](https://github.com/rhasspy/piper)

---

## 📜 License

MIT License
