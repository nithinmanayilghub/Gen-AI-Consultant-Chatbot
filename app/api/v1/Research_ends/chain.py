from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser


#for the chat history
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory


#getting promt templates

from retriever_tool import pdf_retriever_tool
from web_loader_tool import web_loader_chain

from langchain.agents import create_tool_calling_agent
from langchain.agents import AgentExecutor

import os
from dotenv import load_dotenv
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is not None:
    os.environ['GOOGLE_API_KEY'] = google_api_key
else:
    print("GOOGLE_API_KEY environment variable is not set or is empty.")






from pydantic import BaseModel

class ItemResponse(BaseModel):
    result : str







from fastapi import APIRouter, HTTPException

# Define the router
router = APIRouter()







llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
#chain = template_1 | llm | StrOutputParser()

# tools = [pdf_retriever_tool]
# agent=create_tool_calling_agent(llm,tools=tools)

# rag_tool = AgentExecutor(agent=agent,tools=tools,verbose=True)


#make runnable 
runnable = web_loader_chain | StrOutputParser()


runnable.invoke("Hello! this is my website and i want to know how can gen ai help me grow my website https://www.snapdeal.com/ ")


runnable_with_history = RunnableWithMessageHistory(
    runnable,
    lambda session_id: RedisChatMessageHistory(
        session_id, url="redis://localhost:6379"
    ),
    input_messages_key="input",
    history_messages_key="history",
)





@router.post("/invoke", response_model=ItemResponse, tags=["chain"])

def invoke_chain(input_data: str):
    try:
        result = runnable_with_history.invoke(
        {"question": "", "input": input_data},
        config={"configurable": {"session_id": "3"}},
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
