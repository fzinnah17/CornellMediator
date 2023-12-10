from llm import create_emo_agent

stop_button_pressed = False
background = get_background_from_user()

conversation = create_emo_agent(background)

# use this if the user is starting the conversation
opening_prompt = "Help me start the conversation"
emo_agent_response = conversation({"question": opening_prompt})

while not stop_button_pressed:
    caller_response = transcribe_audio()
    emo_agent_response = conversation({"question": caller_response})
    display(emo_agent_response)

