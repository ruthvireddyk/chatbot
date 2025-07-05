def chatbot():
    print("Chatbot: Hello! I’m Chatster, your friendly chatbot. Type 'bye' to end the chat.")

    while True:
        user_input = input("You: ").lower().strip()

        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hi there! Nice to meet you. How can I help?")
        
        elif "how are you" in user_input:
            print("Chatbot: I’m just a chatbot, but I’m happy to chat with you. How are you?")
        
        elif "your name" in user_input:
            print("Chatbot: I’m Chatster, a simple chatbot built with Python.")
        
        elif "help" in user_input:
            print("Chatbot: I can respond to greetings, tell you my name, or say goodbye.")
        
        elif user_input == "bye":
            print("Chatbot: Goodbye! It was great talking to you.")
            break
        
        else:
            print("Chatbot: I didn’t understand that. Can you ask me something else?")


chatbot()
