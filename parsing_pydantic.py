from pydantic import BaseModel, Field
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
from typing import Literal
# Load environment variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")

# Define Pydantic model
class Review(BaseModel):
    summary: str = Field(description='a brief summary of the review')
    sentiment: Literal["positive", "negative"] = Field(description='return sentiment of the review')
    rating: int = Field(description='rating out of 5 stars', ge=1, le=5)
    pros: list[str] = Field(description='list of positive points mentioned in the review')
    cons: list[str] = Field(description='list of negative points mentioned in the review')
    product_category: str = Field(description='the type of product being reviewed')
    recommended: bool = Field(description='whether the reviewer recommends this product')

# Set up the LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro-latest",
    google_api_key=google_api_key
)

# Create a structured output version of the LLM
structured_llm = llm.with_structured_output(Review)

# Send your input
response = structured_llm.invoke("""
The phone feels incredibly sleek and premium in hand.
Its AMOLED display is bright, vibrant, and great for media consumption.
Battery life easily lasts a full day, even with heavy use.
The camera performs well in daylight but struggles in low-light scenarios.
Performance is snappy, thanks to the optimized chipset and smooth UI.
However, it tends to heat up during gaming or video recording.
There’s no headphone jack, which might be a dealbreaker for some.
Software updates are timely, but there's some bloatware out of the box.
Overall, it offers great value for the price and covers most user needs.
Sentiment: Positive, with a few minor drawbacks.""")

print(response.model_dump_json())  # Pydantic model to Python dict
