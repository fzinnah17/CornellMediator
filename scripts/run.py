import gradio as gr
from llm import create_emo_agent
from transcribe import transcribe_audio

# TODO
background = """
I am Morgan and have been working at IBM for the past 5 years Taylor joined the \
company 2 months back. I do not like Taylor because he keeps taking over tasks \
that are clearly mine and does not respect boundaries.
"""

conversation = create_emo_agent(background)

def run(audio):
    # stop_button_pressed = get_stop_button_status()

    # use this if the user is starting the conversation
    # opening_prompt = "Help me start the conversation"
    # emo_agent_response = conversation({"question": opening_prompt})

    # while not stop_button_pressed:
    caller_response = transcribe_audio(audio)
    emo_agent_response = conversation({"question": caller_response})
    response = emo_agent_response["text"]
    print(response)
    return response



# demo = gr.Interface(
#     fn=run,
#     inputs=gr.Audio(sources=["microphone"]),
#     outputs="text",
# )

with gr.Blocks(theme=gr.themes.Default(text_size=gr.themes.sizes.text_lg)) as demo:
    audio = gr.Audio(label="What are they saying?", sources=['microphone'])
    submit_btn = gr.Button("Enter")
    output=gr.Textbox(label="Response", lines=8)

    @submit_btn.click(inputs=audio, outputs=output)
    def go(audio):
        response = run(audio)
        return response
    submit_btn.click(fn=run, inputs=audio, outputs=output)

demo.launch(share=True)