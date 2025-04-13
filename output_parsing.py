from langchain_google_genai import ChatGoogleGenerativeAI
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser
from typing import TypedDict
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
load_dotenv()

# Get the API key from environment variables
google_api_key = os.getenv('GOOGLE_API_KEY')

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=google_api_key)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract the following information from the review: summary and sentiment. Format the response as a JSON object."),
    ("human", "{text}")
])

# Create the chain
chain = prompt | llm | StrOutputParser()

# Test the chain
result = chain.invoke({
    "text": """The phone boasts a sleek modern design with a vibrant AMOLED display that delivers rich colors and deep blacks. Its lightweight yet feels premium in hand perfect for one-handed use. The build quality is solid, with Gorilla Glass protection adding durability."""
})

print(result)

