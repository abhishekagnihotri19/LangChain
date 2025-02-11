from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

import os
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

##Langsimt Tracking
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

##PROMPT CREATION
prompt= ChatPromptTemplate.from_messages(

[("system", "you ar helpful assist. please response to the query"), 
 ("user","question:{question}")]

)

## STREAMLIT FRAMEWORK
st.title("Demo of Chatbot with OpenAI and Ollama")
input_text=st.text_input("Search the topic you want")

##Open AI LLM
llm =ChatOpenAI(model="gpt-3.5-turbo")
output_parser=StrOutputParser()

chain=prompt|llm|output_parser

if input_text:
    st.write(chain.invoke({"question":input_text}))

