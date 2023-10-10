# Import streamlit libraries
import streamlit as st
from streamlit_chat import message

# Import langchain libraries
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory, ConversationSummaryMemory, ConversationBufferWindowMemory)
from langchain.memory import ConversationTokenBufferMemory

# Import tokenization libraries
import tiktoken

# Import ambient libraries
import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = str(os.getenv('OPENAI_API_KEY'))


FIRST_CHATBOT_PHASE ="How can I help you Sr.?"
# Setting title and header on page
st.set_page_config(page_title="Chatbot Arthur", page_icon=":robot_face:")
st.markdown(f"<h1 style='text-align:center;'> {FIRST_CHATBOT_PHASE} </h1>", unsafe_allow_html=True)

st.sidebar.title("😁")
api_key = st.sidebar.text_input("What's your API key?", type="password")
summarise_button = st.sidebar.button("Summarise the conversation", key="summarise")
if summarise_button:
    # summarise_placeholder =  st.sidebar.write("Nice chatting with you my friend ❤️ :\n\n"+"Hello friend") if api_key == OPENAI_API_KEY else st.sidebar.write("Ups😢!!! Your authentication key is wrong! Try again 💪:\n\n")
    summarise_placeholder = st.sidebar.write("Nice chatting with you my friend ❤️ :\n\n"+"Hello friend")
    # summarise_placeholder = st.sidebar.write("Nice chatting with you my friend ❤️ :\n\n"+st.session_state['conversation'].memory.buffer)


# Inicialiação o modelo llm
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

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area('Your question goes here:', key='input', height=100)
        submit_button = st.form_submit_button(label='Send')

with response_container:
    st.write("Response container")
    


