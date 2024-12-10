from stt import record_audio,transcribe_audio
from llm import ask_ollama
from tts import text_to_speech



# Record the question 
waveform = record_audio()

# get the text from recording
text = transcribe_audio(waveform)

# send the text to ollama
response = ask_ollama(text)


# speak ot the reponse
text_to_speech(response)