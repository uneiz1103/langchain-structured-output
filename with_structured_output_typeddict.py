from langchain_openai import ChatOpenAIOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAIOpenAI()

# schema
class Review(TypedDict):

    summary: str
    sentiment: str

structured_model = model.with_structured_output(Review)



result = structured_model.invoke("""The hardwase is great, but the software feels bloated. There are two many pre-installed apps that i can't remove also, the UI looks outdated compared to other brands. Hoping for a software update to fix this.""")

print(result)


