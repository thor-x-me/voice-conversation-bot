from gtts import gTTS
import os


def text_to_speech(text, language='en', slow=False):
    # Create the gTTS object
    tts = gTTS(text=text, lang=language, slow=slow, tld='ca')

    # Save the converted audio to a file
    filename = "output.mp3"
    tts.save(filename)

    # Play the audio file
    os.system(f"start {filename}")  # For Windows
    # os.system(f"afplay {filename}")  # For macOS
    # os.system(f"mpg321 {filename}")  # For Linux

    print("Speech generated successfully!")


# Example usage
text_to_speech("Hello, this is a test of the text-to-speech function.")