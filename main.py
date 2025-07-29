import easyocr
import time

# OCR modelini yuklaymiz (faqat bir marta)
reader = easyocr.Reader(['en'])

def yech_captcha(rasm_manzili):
    start = time.time()
    # Rasm ichidagi matnni o‘qiymiz
    natija = reader.readtext(rasm_manzili, detail=0)  # detail=0 faqat matnni qaytaradi
    print("Topilgan matn:", natija)
    print("Yechish vaqti:", round(time.time() - start, 3), "soniya")

# Misol uchun rasm manzili
yech_captcha("./image.jpg")
