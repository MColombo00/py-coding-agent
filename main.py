import argparse
import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv() #loads the dotenv file for the api key
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)


    #adding parser argument(s) to the command line when running the main program
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    response = client.models.generate_content(
        model ='gemini-2.5-flash', 
        contents=messages
        )
    
    #output and catch if server cannot respond due to busy servers
    print(response.text)
    if response is None or response.usage_metadata is None:
        print("failed to get usage metadata or server is busy, try again later")
        return
    
    print(f"Prompt Token Count: {response.usage_metadata.prompt_token_count}")
    print(f"Candidates Token Count: {response.usage_metadata.candidates_token_count}")

main()