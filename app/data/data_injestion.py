# import
from langchain_chroma import Chroma
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
from langchain_text_splitters import CharacterTextSplitter

from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings

from langchain_community.vectorstores import FAISS

import os
from dotenv import load_dotenv
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if google_api_key is not None:
    os.environ['GOOGLE_API_KEY'] = google_api_key
else:
    print("GOOGLE_API_KEY environment variable is not set or is empty.")




import os
import glob

#Get pdf files path from the data folder for out pdf loader 

data_folder = os.path.join("data", '')
pdf_files = glob.glob(data_folder + '*.pdf')

print(pdf_files)


#load our pdf for the further processing using unstrctured io 
# pdf_loader = UnstructuredPDFLoader(r"D:\GenAi\use-case-gen\data\UseCasesGooglePage.pdf",
#                               mode='elements',
#                                 post_processors=[])

#pdf_loader = partition_pdf(r"D:\GenAi\use-case-gen\data\UseCasesGooglePage.pdf")
pdf_loader = PyPDFLoader(r"./app/data/UseCasesGooglePage.pdf")
pdf_docs = pdf_loader.load()

#Add chunking for documents

# save to disk
# croma_db = Chroma.from_documents(pdf_docs, GoogleGenerativeAIEmbeddings(model="models/embedding-001"),persist_directory="data/chroma_db")


#faiss db
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(pdf_docs)
faiss_db = FAISS.from_documents(docs, GoogleGenerativeAIEmbeddings(model="models/embedding-001"))

faiss_db.save_local("./app/data/faiss_index")
print("Saved to data/faiss_index")