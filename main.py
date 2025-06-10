import os, sys, pathlib
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"

    if len(sys.argv)>1:
        user_prompt = sys.argv[1]
    else:
        with open("config/usage") as f:
            print(f.read())
        sys.exit(1)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),    
    ]

    print("...")
    response = client.models.generate_content(model=model,contents=messages)
    print(response.text)
    if len(sys.argv)>2 and sys.argv[2] == "--verbose":
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")


if __name__ == "__main__":
    main()
