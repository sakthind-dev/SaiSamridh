import os
from openai import OpenAI

# It is a security risk to hardcode your API key directly in the code.
# It is recommended to use environment variables instead.
# For example: client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# A list to store the history of the conversation.
# You can add a system message to define the chatbot's personality.
messages = []
print("Chat with the AI! Type 'quit', 'exit', or 'q' to end the conversation.")

while True:
    #capture user input
    user_input = input("Enter your prompt: ")
 
    # Quit loop if user types 'quit', 'exit', or 'q'
    if user_input.lower() in ['quit', 'exit', 'q']:
        break

    # Prompt preparation
    messages.append({"role": "user", "content": user_input})

    try:
        # Use the new client syntax for openai>=1.0.0
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )

        ai_response = response.choices[0].message.content
        print(f"AI: {ai_response}")

        # Add AI response to messages for conversation history
        messages.append({"role": "assistant", "content": ai_response})

    except Exception as e:
        print(f"An error occurred: {e}")
        # Remove the last user message if the API call failed
        messages.pop()

"""

import os
from openai import OpenAI
import openai

# It is a security risk to hardcode your API key directly in the code.
# It is recommended to use environment variables instead.
# For example: client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# A list to store the history of the conversation
messages = []

while True:
    #capture user input
    user_input = input("Enter your prompt: ")
    print("Chat with the AI! Type 'quit', 'exit', or 'q' to end the conversation.")

    #prompt preparation
    messages.append({"role": "user", "content": user_input})
    #quit loop if user types 'quit' or 'exit' or 'q'
    if user_input.lower() in ['quit', 'exit', 'q']:
        exit()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    print(response.choices[0]['message']['content'])
    print("AI:", response['choices'][0]['message']['content'])

# Function to generate a response from OpenAI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )

"""
