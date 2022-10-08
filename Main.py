import pyttsx3
import pytesseract 
from PIL import ImageGrab

def ReadPicture(picture):
    engine = pyttsx3.init()
    pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Ish\AppData\Local\Programs\Tesseract-OCR\tesseract'
    engine.setProperty('rate', 125)
    try:
        print("thisRan")
        imageToText = (pytesseract.image_to_string(picture))
        print("imageToTxt")
        en_voice_id = "com.apple.speech.synthesis.voice.Deranged"
        engine.setProperty('voice', en_voice_id)

        print("about to talk")
        engine.say(imageToText)
        engine.runAndWait()
        print("THISRAN")
    except:
        print("not the right input2")
        return