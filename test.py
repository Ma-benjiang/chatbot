# First
import openai
import streamlit as st
with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[获得一个OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"  

st.title("💬 Chatbot-Ma") 
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "人工智能为您服务"}] 

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
#     代理
USE_PROXY = False
if USE_PROXY:
    proxies = {
        #          [协议]://  [地址]  :[端口]
        "http":  "http://127.0.0.1:1128",  # 再例如  "http":  "http://127.0.0.1:7890", 
        "https": "http://127.0.0.1:1128",  # 再例如  "https": "http://127.0.0.1:7890",
    }
else:
    proxies = None
if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
