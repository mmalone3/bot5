import openai
import gradio
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def custom_chatgpt(user_input):
    messages = [{"role": "user", "content": user_input}]

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        print("No API key found. Please check your .env file.")
        exit(1)

    openai.api_key = api_key

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=500
    )

    chatgpt_response = response.choices[0].message['content']
    messages.append({"role": "assistant", "content": chatgpt_response})

    return chatgpt_response

bot_title = input("Enter the title of the bot: ")
bot_type = input("Enter the type of the bot: ")

demo = gradio.Interface(
    fn=custom_chatgpt,
    inputs=gradio.Textbox(lines=2, label="Input Text"),
    outputs="text",
    title=f"{bot_title} ({bot_type})",
    description="My First Chatbot - Chat with an AI-powered bot"
)

if __name__ == "__main__":
    demo.launch()
