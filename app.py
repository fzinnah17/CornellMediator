import gradio as gr
from scripts.llm import create_emo_agent
from scripts.transcribe import transcribe_audio

# TODO
background = "I am Morgan and have been working at IBM for the past 5 years Taylor joined the \
        company 2 months back. I do not like Taylor because he keeps taking over tasks \
        that are clearly mine and does not respect boundaries."
conversation = create_emo_agent(background)

def run(audio):
    # stop_button_pressed = get_stop_button_status()

    # use this if the user is starting the conversation
    # opening_prompt = "Help me start the conversation"
    # emo_agent_response = conversation({"question": opening_prompt})

    # while not stop_button_pressed:
    caller_response = transcribe_audio(audio)
    emo_agent_response = conversation({"question": caller_response})

    return emo_agent_response["text"]

demo = gr.Interface(
    run,
    gr.Audio(sources=["microphone"]),
    "text",
)

demo.launch(share=True)