import pytesseract
import cv2

# Lendo a imagem
imagem = cv2.imread("livro.jpg")
caminho = r"C:\Program Files\Tesseract-OCR"
# Extraindo texto da imagem

pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem, lang="por") #definindo a linguagem
print(texto)

