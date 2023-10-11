# Import streamlit libraries
import streamlit as st
from streamlit_chat import message

# Import langchain libraries
from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import (ConversationBufferMemory)

def get_model_response(user_input, api_key):    
    if st.session_state['conversation'] is None:
        llm = OpenAI(temperature=0, openai_api_key=api_key, model_name='text-davinci-003')                                 # Inicialiação o modelo llm
        st.session_state['conversation']  = ConversationChain(llm=llm, verbose=True, memory=ConversationBufferMemory()) # Instanciando a conversação

    # Testando a memória na conversa 
    response = st.session_state['conversation'].predict(input=user_input)
    print(st.session_state['conversation'].memory.buffer)
    return response


if 'conversation' not in st.session_state:
    st.session_state['conversation'] = None
if 'messages' not in st.session_state:
    st.session_state['messages'] = []
if 'API_KEY' not in st.session_state:
    st.session_state['API_KEY'] = ''

# Setting title and header on page
st.set_page_config(page_title="Chatbot Arthur", page_icon=":robot_face:")
st.markdown(f"<h1 style='text-align:center;'> How can I help you Sr.? </h1>", unsafe_allow_html=True)

st.sidebar.title("😁")
st.session_state['API_KEY'] = st.sidebar.text_input("What's your API key?", type="password")
btn_start = st.sidebar.button("Summarise the conversation", key="summarise")
if btn_start:
    st.sidebar.write("Nice chatting with you my friend ❤️ :\n\n")

response_container = st.container()
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area('Your question goes here:', key='input', height=100)
        submit_button = st.form_submit_button(label='Send')
        if submit_button: 
            if user_input == "":
                st.sidebar.write("Ups😢!!! Enter samething in the form field!")
            else:
                st.session_state['messages'].append(user_input)
                model_response = get_model_response(user_input, st.session_state['API_KEY'])
                st.session_state['messages'].append(model_response)
                with response_container:
                    for i in range(len(st.session_state['messages'])):
                        # se i é par message do user, senão message do bot 
                        message(st.session_state['messages'][i], is_user=(i%2)==0, key=str(i) + ['_user', '_AI'][i%2]) 
                       
