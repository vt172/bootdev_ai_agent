import os, sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    if len(sys.argv)>1:
        contents = sys.argv[1]
    else:
        print("Please provide an argument.\nExemple: python3 main.py \'your prompt\'")
        sys.exit(1)

    response = client.models.generate_content(model=model,contents=contents)
    print(response.text)
    print("...")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
