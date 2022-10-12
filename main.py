import pytesseract
import cv2
import gtts
from playsound import playsound

# Lendo a imagem
imagem = cv2.imread("livro.jpg")
caminho = r"C:\Program Files\Tesseract-OCR"


# Extraindo texto da imagem
pytesseract.pytesseract.tesseract_cmd = caminho + r"\tesseract.exe"
texto = pytesseract.image_to_string(imagem, lang="por") #definindo a linguagem
print(texto)

frase = gtts.gTTS(texto,lang='pt-br')
frase.save('frase.mp3')
playsound('frase.mp3')
