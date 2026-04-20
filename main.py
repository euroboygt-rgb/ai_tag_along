import os
import argparse
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import system_prompt
from call_function import available_functions, call_function

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Error: GEMINI_API_KEY not found in .env file.")
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)

    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt,
        temperature=0
    )

    messages = [
        types.Content(role="user", parts=[types.Part.from_text(text=args.user_prompt)])
    ]

    for i in range(20):
        if args.verbose:
            print(f"--- Iteration {i + 1} ---")

        # Switching back to 2.5-flash as it's the one your API key recognizes
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=messages,
            config=config
        )

        if response.candidates:
            for candidate in response.candidates:
                messages.append(candidate.content)

        if response.function_calls:
            function_responses = []
            for fc in response.function_calls:
                print(f" - Calling function: {fc.name}")
                result_content = call_function(fc, verbose=args.verbose)
                if result_content.parts:
                    function_responses.append(result_content.parts[0])

            messages.append(
                types.Content(role="user", parts=function_responses)
            )
        else:
            print(response.text)
            return

    print("Error: Maximum iterations reached.")
    sys.exit(1)

if __name__ == "__main__":
    main()
