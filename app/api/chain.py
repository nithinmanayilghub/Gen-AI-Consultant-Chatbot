
from langchain_core.output_parsers import StrOutputParser


#for the chat history
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.runnables import RunnableLambda






import os
from dotenv import load_dotenv
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is not None:
    os.environ['GOOGLE_API_KEY'] = google_api_key
else:
    print("GOOGLE_API_KEY environment variable is not set or is empty.")








# llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7)
#chain = template_1 | llm | StrOutputParser()

# tools = [pdf_retriever_tool]
# agent=create_tool_calling_agent(llm,tools=tools)

# rag_tool = AgentExecutor(agent=agent,tools=tools,verbose=True)


#make runnable 
# runnable = web_loader_chain | StrOutputParser()


# runnable.invoke("Hello! this is my website and i want to know how can gen ai help me grow my website https://www.snapdeal.com/ ")
from .use_case_agent import use_case_agent

# response = use_case_agent.invoke({"msgs": "Hi, I'm the Founder of Al Reyami International Steel Tech LLC. How can I leverage Gen AI to grow my business?"})
# print(response)
# use_case_agent = use_case_agent | StrOutputParser


from fastapi import APIRouter, HTTPException, Request, Query

# Define the router
router = APIRouter()



runnable_with_history = RunnableWithMessageHistory(
    use_case_agent,
    lambda session_id: RedisChatMessageHistory(
        session_id, url="redis://localhost:6379"
    ),
    input_messages_key="msgs",
    history_messages_key="history",
)   | RunnableLambda (lambda x: x["output"]) | StrOutputParser()





# @router.post("/invoke", response_model=ItemResponse, tags=["chain"])

# def invoke_chain(request: Request, input_data: str, session_id: str = Query(None)):
#     try:
#         result = runnable_with_history.invoke(
#         {"msgs": input_data},
#         config={"configurable": {"session_id": session_id}},
#         )
#         return {"result": result}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


from pydantic import BaseModel

class ItemResponse(BaseModel):
    result : str

class ItemRequest(BaseModel):
    input_data: str
    session_id: str


@router.post("/invoke", response_model=ItemResponse, tags=["chain"])
async def invoke_chain(request: Request, body: ItemRequest):
    try:
        result = runnable_with_history.invoke(
            {"msgs": body.input_data},
            config={"configurable": {"session_id": body.session_id}},
        )
        return {"result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))