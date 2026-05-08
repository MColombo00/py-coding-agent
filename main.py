import argparse
import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    args = parser.parse_args()



    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model ='gemini-2.5-flash', 
        contents=args.user_prompt
        )
    print(response.text)

    if response is None or response.usage_metadata is None:
        print("failed to get usage metadata or server is busy, try again later")
        return

    print(f"Prompt Token Count: {response.usage_metadata.prompt_token_count}")
    print(f"Candidates Token Count: {response.usage_metadata.candidates_token_count}")

main()