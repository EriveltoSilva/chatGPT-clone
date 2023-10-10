from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, ConversationSummaryMemory, ConversationBufferWindowMemory)

import tiktoken
from langchain.memory import ConversationTokenBufferMemory

import os
from dotenv import load_dotenv

load_dotenv()

# Inicialiação o modelo llm
OPENAI_API_KEY = str(os.getenv('OPENAI_API_KEY'))
llm = OpenAI(temperature=0,                 # criatividade de resposta 
             model_name='text-davinci-003'  # modelo em uso
            ) 

# Instanciando a conversação
conversation = ConversationChain(
    llm=llm,
    verbose=True,
    memory=ConversationBufferMemory()
)


# Testando a memória na conversa 
conversation("Hi, how is it going!")
conversation("My name is Erivelto")
conversation.predict(input="I stay in hyderabad, Angola")
print(conversation.memory.buffer)
conversation.predict(input="What is my name?")


