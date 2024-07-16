import streamlit as st
import requests

# Function to get response from FastAPI backend
def get_response_from_backend(message: str, session_id: str) -> str:
    response = requests.post(
        "http://127.0.0.1:8000/api/chain/invoke",
        json={"input_data": message, "session_id": session_id}
    )
    response_data = response.json()
    return response_data["result"]

# Streamlit UI
st.title("Generative AI Chatbot")

# Sidebar layout using Markdown columns
st.sidebar.title("About the Chatbot")

# Input for session ID
st.sidebar.write("Session Settings")
session_id = st.sidebar.text_input("Session ID", value="42")

# First column in sidebar
st.sidebar.markdown("""
# Discover Tailored Business Use Cases with Our AI Application

Our AI application helps you uncover the best use cases specifically tailored to your business. Simply provide the URL of your business, and our system will conduct a web search using DuckDuckGo to gather relevant information.

## Key Features:

- **Smart Web Search**: Utilizes DuckDuckGo to efficiently search the web for insights related to your business.
""")



# Second column in sidebar
st.sidebar.markdown("""
- **Advanced AI Capabilities**: Uses a Retrieval-Augmented Generation (RAG) model to generate personalized use cases from an extensive knowledge base stored in a vector database.
- **Rich Knowledge Base**: Over 1,000 pre-compiled use cases are included in our vector database, ensuring comprehensive and relevant results.
- **Innovative Technology**: Built with advanced tools including LangChain and Gemini for optimal performance and accuracy.

With our application, you'll receive actionable use cases that align closely with your business needs.

---

***Created by Vishal Vijay Pachpande and Nithin M A***

---
""")



# Store session ID in session state
if "session_id" not in st.session_state:
    st.session_state["session_id"] = session_id

# Update session state when session ID input changes
if session_id != st.session_state["session_id"]:
    st.session_state["session_id"] = session_id

# Initialize the session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Hello! I can help you with generative AI use cases. You can paste your website URL."}]

# Display chat messages
for message in st.session_state["messages"]:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Input prompt for the user
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    response = get_response_from_backend(prompt, st.session_state["session_id"])
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.chat_message("assistant").write(response)
