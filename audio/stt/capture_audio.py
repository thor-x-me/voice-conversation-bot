import pyaudio
import wave
from audio.stt.whisper_stt import speech_to_text

# Define parameters
FORMAT = pyaudio.paInt16  # Audio format
CHANNELS = 1  # Number of channels (mono)
RATE = 44100  # Sample rate
CHUNK = 1024  # Chunk size
RECORD_SECONDS = 5  # Recording duration

def record_audio():
    # Create PyAudio instance
    audio = pyaudio.PyAudio()

    # Start recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK,
                        input_device_index=1)
    frames = []

    print("Recording...")
    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # Save the audio to a WAV file
    waveFile = wave.open("recorded_audio.wav", 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()
    print("File saved Sucessfuly !")

    # text = speech_to_text(r'C:\Users\thorxme\PycharmProjects\voice-conversation-bot\audio\stt\recorded_audio.wav')
    # return text
