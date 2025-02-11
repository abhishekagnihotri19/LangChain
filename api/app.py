from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain.chat_models import ChatOpenAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv




load_dotenv()
os.environ["OPENAI_API_KEY"]= os.getenv("OPENAI_API_KEY")

app = FastAPI(
    title="Langchain Server",
    version ="1.0",
    descripton ="Simple API Server"
)

add_routes(
app,
ChatOpenAI(),
path ="/openai"
)
#model1
model = ChatOpenAI()
#model2
llm=Ollama(model="llama3.2:latest")

prompt1=ChatPromptTemplate.from_template("Write an essay about some {topic} with hundred words")

prompt2= ChatPromptTemplate.from_template("Write an Poem abot some{topic} with 100 words")

add_routes (
    app,
    prompt1|model,
    path= "/essay"
)

add_routes(
    app,
    prompt2|llm,
    path= "/poem")


if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)


#uvicorn api.main:app --host 0.0.0.0 --port 8000
