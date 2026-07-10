def chatbot():
    print("Hello there! My name is Chitty")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks!")
        elif user == "what is your name":
            print("Bot: I am a simple Python ChatBot and my name is Chitty.")
        elif user == "who made you":
            print("Bot: I was created by a Python programmer.")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry, I don't understand that.")

chatbot()