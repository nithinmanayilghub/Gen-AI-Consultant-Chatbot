
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import ChatPromptTemplate

import os
from langchain_community.document_loaders import UnstructuredURLLoader
from unstructured.partition.html import partition_html







# google_api_key = os.getenv("GOOGLE_API_KEY")
# if google_api_key is not None:
#     os.environ['GOOGLE_API_KEY'] = google_api_key
# else:
#     print("GOOGLE_API_KEY environment variable is not set or is empty.")





def load_web(url : str):
    """ Visits the url provided and returns the text data from the given url

    Args:
      url : The url to be visited

    Returns: The text data from the given url
    """

    loader = UnstructuredURLLoader([url])
    documents = loader.load()
    # Extract text content from the Document object
    text_content = documents[0].page_content
    elements = partition_html(text=text_content)
    #elements[0].apply(bytes_string_to_string)


    return elements[0].text


def Search_for_use_cases(query : str):
    #rag agent
    pass


# Create the prompt and LLM chain
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.7,tools = [load_web])


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
    ("human", ("{msgs}")),
    ]
    )

chain = prompt | llm
response = chain.invoke("use wikipedia to find out about gen ai")
print(response)