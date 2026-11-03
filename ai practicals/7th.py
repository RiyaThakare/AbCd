
print("Welcome to AI Chatbot!")
print("You can ask me about college, studies, technology, etc.")
print("Type 'bye' to exit the chatbot.")

while True:
    user = input("\nYou: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How can I help you?")

    elif "name" in user:
        print("Bot: I am an AI-based simple chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    elif "college" in user:
        print("Bot: College is a place where students learn new skills and build their careers.")

    elif "study" in user or "education" in user:
        print("Bot: Studying regularly helps you achieve your goals.")

    elif "python" in user:
        print("Bot: Python is a simple and powerful programming language.")

    elif "ai" in user or "artificial intelligence" in user:
        print("Bot: AI enables machines to perform tasks that require human intelligence.")

    elif "exam" in user:
        print("Bot: Don't worry! Prepare well and give your best. All the best!")

    elif "food" in user:
        print("Bot: Food gives us energy and keeps us healthy.")

    elif "weather" in user:
        print("Bot: I hope you are having a pleasant day!")

    elif "thank" in user:
        print("Bot: You're welcome! Happy to help.")

    elif "help" in user:
        print("Bot: I can answer questions about studies, college, Python, AI and more.")

    elif "bye" in user:
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand. Please try another keyword.")

