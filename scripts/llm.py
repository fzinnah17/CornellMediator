import os
from langchain.chains import LLMChain
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,

)
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from langchain.memory import ConversationBufferMemory
from langchain.llms import Together

openai_api_key = os.environ["OPENAI_API_KEY"]
print(openai_api_key)

def create_emo_agent(background):

    # llm = ChatOpenAI()
    llm = Together(
    model="togethercomputer/CodeLlama-34b-Python",
    temperature=0.7,
    max_tokens=128,
    top_k=1,
    together_api_key="eef23e8a6ce9107ad32981ceac02d11ec3527940e825ef984a79e63635975387"    
    )
    background_context = "You are an empathetic yet assertive chatbot. I struggle with confrontation and I need you to help me have an objective and calm conversation. Remember, this conversation is very important for me. I will tell what the other person is saying and you need to formulate my response. Your response should point out when the other person is straying off topic. Don't be apologetic unless necessary. The following is the background for conversation: " + background
    # Prompt
    prompt = ChatPromptTemplate(
        messages=[
            SystemMessagePromptTemplate.from_template(
                background_context
            ),
            # The `variable_name` here is what must align with memory
            MessagesPlaceholder(variable_name="chat_history"),
            HumanMessagePromptTemplate.from_template("{question}"),
        ]
    )

    # Notice that we `return_messages=True` to fit into the MessagesPlaceholder
    # Notice that `"chat_history"` aligns with the MessagesPlaceholder name
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    conversation = LLMChain(llm=llm, prompt=prompt, verbose=True, memory=memory)

    return conversation

