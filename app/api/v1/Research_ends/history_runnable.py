from langchain_core.messages import HumanMessage
from langchain_core.runnables.history import RunnableWithMessageHistory

from app.api.v1.endpoints.chain import llm 




from langchain_community.chat_message_histories import RedisChatMessageHistory



'''from langchain_community.chat_message_histories import SQLChatMessageHistory

def get_session_history(session_id):
    return SQLChatMessageHistory(session_id, "sqlite:///memory.db")'''




from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You're an assistant who speaks in {language}. Respond in 20 words or fewer",
        ),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{input}"),
    ]
)

runnable = prompt | llm

runnable_with_history = RunnableWithMessageHistory(
    runnable,
    lambda session_id: RedisChatMessageHistory(
        session_id, url="redis://localhost:6379"
    ),
    input_messages_key="input",
    history_messages_key="history",
)



response = runnable_with_history.invoke(
    {"language": "italian", "input": "what is my name "},
    config={"configurable": {"session_id": "2"}},
)

print(response)