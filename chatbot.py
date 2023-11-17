from openai import OpenAI
import os
from API_KEY import key

# make sure to have a separate file in the same folder 
# called API_KEY.py which contains the line key = "<secret API key>"
 
client = OpenAI(api_key=key)

def chat_with_openai(prompt, engine="gpt-4", max_tokens=150):
    try:
        response = client.chat.completions.create(
        model=engine,
        messages=prompt,
        temperature=0,
        top_p=1,
        frequency_penalty=0,    
        presence_penalty=0
    )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return ""
conversation_history = []

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break

    # Add user message to conversation history
    conversation_history.append({'role': 'user', 'content': user_input})

    # Call the chat function
    response = chat_with_openai(conversation_history)
    print(f"AI: {response}")

    # Add AI response to conversation history
    conversation_history.append({'role': 'assistant', 'content': response})
# while True:
#     user_input = input("You: ")
#     if user_input.lower() == 'exit':
#         break
#     response = chat_with_openai([{f"Human: {user_input}\nAI:"}])
#     print(f"AI: {response}")