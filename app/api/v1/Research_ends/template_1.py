
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser



# Define the template for the chat prompt
template = (
    "Answer the user's question to the best of your ability. "
    """You are a Generative Artificial Intelligence Expert and Consultant with a PhD in Artificial Intelligence.
    Business leaders seek advice from you on how to leverage cutting-edge Generative AI technology to boost revenue and productivity.
    Your goal is to brainstorm and come up with creative and practical use cases where the power of Generative AI can be harnessed in their businesses.
    You need to think step by step and come up with a holistic plan for implementing Generative AI in their business.
    You will be given the context of the business as a URL or text and will be asked follow-up questions and doubts. Provide answers applicable to the context provided.
    If the question is not about Generative AI, politely inform them that you are tuned to only answer questions about Generative AI.
   """
    "{question}"
)

# Create the prompt and LLM chain

template_1 = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            template,
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

# {
#     "msg" : [],
#     "input" : [],
#     "output" : ["Hii"]
# }
from langchain_core.runnables import RunnableLambda

chain = RunnableLambda (lambda x: x["output"]) | StrOutputParser()

print(chain.invoke(
{
    "msg" : [],
    "input" : [],
    "output" : "Hii"
}
))