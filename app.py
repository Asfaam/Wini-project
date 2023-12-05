import openai
import gradio as gr


openai.api_key = "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"

messages = [
    {"role": "system", "content": "You are a helpful and kind AI Assistant."},
]

def chatbot(input):
    if input:
        new_messages = messages[:]  # Create a copy of the messages list
        new_messages.append({"role": "user", "content": input})

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=new_messages
        )
        reply = chat.choices[0].message.content

        messages.append({"role": "assistant", "content": reply})  # Append the reply to the original list
        return reply

inputs = gr.Textbox(lines=7, label="Chat with AI")
outputs = gr.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="AI Chatbot",
              description="Ask anything you want",
              theme="compact").launch(share=True)