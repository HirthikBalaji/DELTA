import os
def Generate_audio(text):
    os.system(f"echo '{text.replace("'", "").replace("\n", ",").replace('"','')}' | wsl ./piper/piper --model ./piper/en_US-hfc_male-medium.onnx --output_file welcome.wav")

# PRE_REQUESTS INSTALL WSL IN WINDOWS...
