import os
import easyocr

# Initialize EasyOCR Reader (supports multiple languages)
reader = easyocr.Reader(['en'])  # You can add more langs like ['en', 'hi'] etc.

result = reader.readtext('Delta Headlines/0e8716f5-03a9-4a7f-aca9-e0941bb48442.jpg',detail=0)
print(result)
