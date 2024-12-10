import os
import whisper
import torch
import pyaudio
import numpy as np
import wave

filename = "recording.wav"




os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'
device = "cuda" if torch.cuda.is_available() else "cpu"
print(device)
           
model = whisper.load_model("tiny").to(device)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
duration=3
sample_rate=16000

def record_audio():

    p = pyaudio.PyAudio()

    print("Recording...")
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=CHUNK)

    frames = []

    for i in range(0, int(sample_rate / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Recording complete.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    # Convert to numpy array
    # audio = np.frombuffer(b''.join(frames), dtype=np.int16).astype(np.float32) * (1.0/sample_rate)


    print("Saving Audio...")
    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()

    return filename



# from scipy.io import wavfile
# import io


def transcribe_audio(file):
    print("Transcribing Audio...")
    result = model.transcribe(file)
    print("Transcription: ",result["text"])
    return result["text"]


if __name__=="__main__":
    waveform = record_audio()
    text = transcribe_audio(waveform)