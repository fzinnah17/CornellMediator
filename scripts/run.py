import gradio as gr
from llm import create_emo_agent
from transcribe import transcribe_audio

# TODO
background = get_background_from_user()
conversation = create_emo_agent(background)

def run():
    # stop_button_pressed = get_stop_button_status()

    # use this if the user is starting the conversation
    opening_prompt = "Help me start the conversation"
    emo_agent_response = conversation({"question": opening_prompt})

    # while not stop_button_pressed:
    caller_response = transcribe_audio()
    emo_agent_response = conversation({"question": caller_response})

    return emo_agent_response

demo = gr.Interface(
    run,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch()