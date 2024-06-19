
import os
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())


import glob

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.document_loaders import UnstructuredPDFLoader,TextLoader



from langchain.docstore.document import Document
from langchain_community.document_loaders import PyPDFLoader


from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool


from langchain.agents import create_tool_calling_agent

from pypdf import PdfReader

from dotenv import load_dotenv
load_dotenv() 
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is not None:
    os.environ['GOOGLE_API_KEY'] = google_api_key
else:
    print("GOOGLE_API_KEY environment variable is not set or is empty.")





#Get pdf files path from the data folder for out pdf loader 

data_folder = os.path.join("data", '')
pdf_files = glob.glob(data_folder + '*.pdf')

print(pdf_files)


#load our pdf for the further processing using unstrctured io 
# pdf_loader = UnstructuredPDFLoader(r"D:\GenAi\use-case-gen\data\UseCasesGooglePage.pdf",
#                               mode='elements',
#                                 post_processors=[])

#pdf_loader = partition_pdf(r"D:\GenAi\use-case-gen\data\UseCasesGooglePage.pdf")
pdf_loader = PyPDFLoader(r"D:\GenAi\use-case-gen\data\UseCasesGooglePage.pdf")
pdf_docs = pdf_loader.load()


#text splitter so we chuck  out data 
pdf_documents= RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200).split_documents(pdf_docs)

#Embbed and store in vetor store
vectordb=FAISS.from_documents(pdf_documents,GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

#Create Retriver 
pdf_retriever=vectordb.as_retriever()
pdf_retriever_tool = create_retriever_tool(pdf_retriever,"generative_ai_use_cases_pdf_doc",
                       "you are a reference pdf document for  generative ai use cases. For any questions about generative-ai-use-cases, you must use this tool!")



