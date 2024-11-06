from langchain_ollama import OllamaLLM
import gradio as gr

from audio.stt.capture_audio import record_audio
from audio.stt.whisper_stt import speech_to_text
from audio.tts.microsoft_speecht5_tts import ttsMicrosoft

ollama = OllamaLLM(model='smollm2:latest')


# Define a function to handle user input and return the model's response
def chat_with_ollama(user_input, history):
    # Use Ollama's model to generate a response
    response = ollama.invoke(input=user_input)
    print(response)

    # Append the response to chat history
    history.append((user_input, response))

    return history, history


def pipeline(history):
    # Step 1: Record Audio
    record_audio()
    print("recording complete!!!")

    # Step 2: Transcipt generation
    text = speech_to_text(r"C:\Users\thorxme\PycharmProjects\voice-conversation-bot\llm\recorded_audio.wav")

    # step 3: LLM inference
    result = chat_with_ollama(user_input=text, history=history)

    # Step 4: text to speech
    # ttsMicrosoft(str(result))

    # Step 5: return result in chat window
    return result




# Set up Gradio's Chat Interface
with gr.Blocks() as app:
    gr.Markdown("<h1>Sales Agent</h1>")

    # Chatbot component
    chat_interface = gr.Chatbot()

    # Function to update chat history
    chat_history = gr.State([])
    is_recorded = False

    # Add record button to trigger record_audio function
    record_button = gr.Button("Record")
    record_button.click(pipeline, inputs=[chat_history], outputs=[chat_interface, chat_history])

# Launch the app
app.launch()
