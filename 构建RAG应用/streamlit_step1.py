# 初步搭建应用界面  实现基本的单轮对话功能
import os
import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

openai_api_key = os.environ['OPENAI_API_KEY']

def generate_response(input_text):
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
    output = llm.invoke(input_text)
    output_parser = StrOutputParser()
    output = output_parser.invoke(output)
    st.info(output)



def main():
    st.title('🦜🔗 动手学大模型应用开发')
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')
    with st.form('my_form'):
        text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
        submitted = st.form_submit_button('Submit')
        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text)


if __name__ == '__main__':
    main()