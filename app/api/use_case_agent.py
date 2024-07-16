import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools import WikipediaQueryRun,DuckDuckGoSearchResults
from langchain_community.utilities import WikipediaAPIWrapper,DuckDuckGoSearchAPIWrapper

from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import FAISS

from langchain.tools.retriever import create_retriever_tool
from langchain.agents import create_tool_calling_agent


# from langchain_chroma import Chroma

load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is not None:
    os.environ['GOOGLE_API_KEY'] = google_api_key
else:
    print("GOOGLE_API_KEY environment variable is not set or is empty.")


# Wikipedia Tool
wiki_api_wrapper=WikipediaAPIWrapper(top_k_results=1,doc_content_chars_max=500)
wiki=WikipediaQueryRun(api_wrapper=wiki_api_wrapper)


# Pdf as Retriever Tool
# croma_db = Chroma(persist_directory="data/chroma_db", embedding_function=GoogleGenerativeAIEmbeddings(model="models/embedding-001"))
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
local_faiss = "./app/data/faiss_index"

try: 
    faiss_db = FAISS.load_local(local_faiss, embeddings, allow_dangerous_deserialization=True)
except Exception as e: 
    from app.data.data_injestion import faiss_db
    print(f"Exception occurred: {e}")




pdf_retriever=faiss_db.as_retriever()
pdf_retriever_tool = create_retriever_tool(pdf_retriever,"generative_ai_use_cases_pdf_doc",
                       "you are a reference pdf document for  generative ai use cases. For any questions about generative-ai-use-cases, you must use this tool!")


# search = DuckDuckGoSearchRun()
dd_wrapper = DuckDuckGoSearchAPIWrapper(time="d", max_results=1)
dd_search = DuckDuckGoSearchResults(api_wrapper=dd_wrapper)


tools = [wiki,dd_search,pdf_retriever_tool]


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash",temperature=0.6)




system_template = """
Instructions :  1) You are expert Gen Ai software Engineer. You know business concepts about generative Ai.
                2) You must refrain yourself from answering anything else other than Genrative Ai
                3) Call the necessary tools such as web loader whenever your gives his website url.

Context :       1) Business leaders seeks advice from you on how to leverage cutting-edge Generative AI technology to boost revenue and productivity.
                your goal is to brainstorm and come up with creative and practical usecases where the power of Generative Artificial Intelligence 
                can be harnessed in their buinsesses.
                2)You need to think step by step and come up with a holistic plan for implementing Generative Artificial Intelligence in their businesses when the user asks.
                You will be given the context of the business as url or text and will be asked follow up questions or doubts.Give answers applicable to the context provided.
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("placeholder",("{history}")),
    ("human", ("{msgs}")),
    ("placeholder","{agent_scratchpad}")
    ])


### Agents
agent = create_tool_calling_agent(llm,tools,prompt)


## Agent Executor
from langchain.agents import AgentExecutor
use_case_agent  = AgentExecutor(agent=agent,tools=tools,verbose=True)
