import whisper


def speech_to_text(audio):

    model = whisper.load_model("small")
    result = model.transcribe(audio=audio)
    return result["text"]

# print(speech_to_text(r"C:\Users\thorxme\PycharmProjects\voice-conversation-bot\audio.mp3"))