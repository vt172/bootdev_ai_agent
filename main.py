import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config.parameters import Parameters

def parameter_validation(value):
    try:
        Parameters(value)
        return True
    except ValueError:
        return False


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    model = "gemini-2.0-flash-001"
    user_prompt = ""
    global paramater
    parameter = "" 

    if len(sys.argv)>2:
        if not parameter_validation(sys.argv[2]):
            print(f"{sys.argv[2]} is not a correct parameter.")
            with open("config/usage") as f:
                print(f.read())
            sys.exit(1)
        parameter = Parameters(sys.argv[2])
    elif len(sys.argv)>1:
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

    if parameter:
        match parameter:
            case Parameters.VERBOSE:
                prompt_tokens = response.usage_metadata.prompt_token_count
                response_tokens = response.usage_metadata.candidates_token_count
                print(f"User prompt: {user_prompt}")
                print(f"Prompt tokens: {prompt_tokens}")
                print(f"Response tokens: {response_tokens}")
    print(response.text)


if __name__ == "__main__":
    main()
