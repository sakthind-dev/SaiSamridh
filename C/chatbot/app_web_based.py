import gradio as gr
import os
from openai import OpenAI

messages = []
messages.append({"role": "system", "content": "You are a helpful assistant."})

# It is a security risk to hardcode your API key directly in the code.
# It is recommended to use environment variables instead.
# For example: client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

def respond_to_prompt(history, new_message):

    # Append user input to the messages
    messages.append({"role": "user", "content": new_message})

    #send the messages to the OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )

    #obtain response text
    ai_response = response.choices[0].message
    messages.append(ai_response)

    #display the AI response
    #ai_response = response.choices[0].message.content

    #extend the messages with the AI response
    #messages.append({"role": "assistant", "content": ai_response})
    
    print(f"History: {history}")
    print(f"New Message: {new_message}")
    return history + [[new_message, ai_response.content]]

with gr.Blocks() as demo:
    chatbot = gr.Chatbot()
    msg = gr.Text()

    msg.submit(respond, [chatbot, msg], chatbot)
    #msg.submit(respond_to_prompt, [chatbot, msg], chatbot)
    #clear = gr.ClearButton([msg, chatbot])


demo.launch()
