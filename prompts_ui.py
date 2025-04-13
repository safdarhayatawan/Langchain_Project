from langchain_google_genai import ChatGoogleGenerativeAI


import streamlit as st
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
# Load environment variables
load_dotenv()

# Set page config
st.set_page_config(
    page_title="LangChain Prompts UI",
    page_icon="🤖",
    layout="wide"
)

# Title
st.title("LangChain Prompts UI")

# Sidebar for configuration
with st.sidebar:
    st.header("Configuration")
    st.write("Environment Variables Status:")
    
    # Check and display environment variables
    google_api_key = os.getenv('GOOGLE_API_KEY')
    huggingface_token = os.getenv('HUGGINGFACEHUB_API_TOKEN')
    
    st.write(f"Google API Key: {'✅ Loaded' if google_api_key else '❌ Not Loaded'}")
    st.write(f"HuggingFace Token: {'✅ Loaded' if huggingface_token else '❌ Not Loaded'}")

# Main content area
st.write("Welcome to the LangChain Prompts UI!")
st.write("This interface will help you manage and test your LangChain prompts.")

# Add a text input for prompts
prompt = st.text_area("Enter your prompt here:", height=200)
paper_input = st.selectbox(
    "Select Research Paper Name",
    ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", 
     "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Load the prompt template
template = load_prompt('template.json')

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest", google_api_key=google_api_key)

# Add a button to process the prompt
if st.button("Process Prompt"):
    if prompt:
        try:
            # Format the prompt with the selected options
            formatted_prompt = template.format(
                paper=paper_input,
                style=style_input,
                length=length_input,
                prompt=prompt
            )
            
            # Get the response from the LLM
            response = llm.invoke(formatted_prompt)
            
            # Display the response
            st.write("### Response:")
            st.write(response.content)
            
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter a prompt first!")
