import easyocr
def perform_ocr(image):
    reader = easyocr.Reader(['en'])  # You can add more langs like ['en', 'hi'] etc.

    result = reader.readtext(image, detail=0)
    return result
