from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage

# Load environment variables
load_dotenv()

# Get the API key from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=google_api_key)

print("Chatbot initialized. Type 'exit' to quit.")
chat_history = [
    SystemMessage(content='You are a helpful AI assistant')
]

while True:
    user_input = input('You: ')
    chat_history.append(HumanMessage(content=user_input))
    if user_input == 'exit':
        break
    result = llm.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("AI: ",result.content)

print(chat_history)