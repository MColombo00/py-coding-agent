import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(
    model ='gemini-2.5-flash', contents="how are potatoes grown, use one paragraph maximum"
    )
print(response.text)
print(response.prompt_token_count)
print(response.candidates_token_count)
