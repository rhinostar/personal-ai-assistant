# from gtts import gTTS

# import os

# # The text that you want to convert to audio
# mytext = 'hello i am trying to test this to check if this will get transcribed by whisper'

# # Language in which you want to convert
# language = 'en'

# myobj = gTTS(text=mytext, lang=language, slow=False)

# # Saving the converted audio in a mp3 file named
# # welcome 
# myobj.save("welcome.mp3")

# # Playing the converted file
# os.system("start welcome.mp3")


import pyttsx3

engine = pyttsx3.init()

def text_to_speech(text):
    engine.setProperty('rate', 120) 
    engine.say(text)
    engine.runAndWait()