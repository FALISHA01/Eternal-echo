from chat_engine import chat_with_person

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = chat_with_person(user_input)
    print("AI:", response)
