import whisper


def speech_to_text(audio):

    model = whisper.load_model("small")
    result = model.transcribe(audio=audio)
    print(result['text'])
    return result["text"]


# text = speech_to_text(r'\\wsl.localhost\Ubuntu\home\thorxme\WSL-voice-bot\audio\stt\audio.mp3')
# print(text)
