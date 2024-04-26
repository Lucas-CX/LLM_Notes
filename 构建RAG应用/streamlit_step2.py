# streamlit_step2.py 实现界面的对话历史记录

import streamlit as st
from langchain_openai import ChatOpenAI
import os
from langchain_core.output_parsers import StrOutputParser

openai_api_key = os.environ['OPENAI_API_KEY']



def generate_response(input_text, openai_api_key):
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
    output = llm.invoke(input_text)
    output_parser = StrOutputParser()
    output = output_parser.invoke(output)
    #st.info(output)
    return output


  
# Streamlit 应用程序界面
def main():
    st.title('🦜🔗 动手学大模型应用开发')
    openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

    # 用于跟踪对话历史
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    messages = st.container(height=300)
    if prompt := st.chat_input("Say something"):
        # 将用户输入添加到对话历史中
        st.session_state.messages.append({"role": "user", "text": prompt})

        # 调用 respond 函数获取回答
        answer = generate_response(prompt, openai_api_key)
        # 检查回答是否为 None
        if answer is not None:
            # 将LLM的回答添加到对话历史中
            st.session_state.messages.append({"role": "assistant", "text": answer})

        # 显示整个对话历史
        for message in st.session_state.messages:
            if message["role"] == "user":
                messages.chat_message("user").write(message["text"])
            elif message["role"] == "assistant":
                messages.chat_message("assistant").write(message["text"])   

                
if __name__ == '__main__':
    main()