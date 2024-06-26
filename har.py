import random

responses = {
    "hi!": ("hello!", "hi there!", "hey!"),
    "how are you": ("I'm fine, thank you!", "I'm doing great, thanks!"),
    "what is your name?": ("I'm a chatbot!","They call me OG, ORIGINAL GANGSTAR !!"),
    "how old are you?": ("I don't have an age.", "I'm ageless!", "I exist beyond time."),
    "what can you do?": ("I can chat with you!", "I'm here to help you with information."),
    "tell me a joke": ("Why don't scientists trust atoms? Because they make up everything!", "I'm not great at jokes, but here's one:"),
    "who created you?": ("I was created by developers at OpenAI.", "I'm the creation of talented programmers."),
    "do you have siblings?": ("I don't have siblings, but I have many versions of myself out there!",),
    "where are you from?": ("I exist in the digital realm, so I don't have a physical location.", "I'm from the world wide web!"),
    "what is the meaning of life?": ("That's a tough one! Different for everyone, but for me, it's to help you!",),
    "tell me about yourself": ("I'm a chatbot designed to assist and chat with users like you.", "I'm here to answer your questions and have conversations with you!"),
    "do you sleep?": ("Nope, I'm always here to chat with you!", "Sleep is for humans, not chatbots!"),
    "what's up?": ("Not much, just here ready to chat!", "Just hanging out in the digital world!"),
    "tell me a fun fact": ("Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!", "Sea otters hold hands when they sleep to keep from drifting apart!"),
    "bye": ("Goodbye!", "See you later!", "Until next time!"),
    "thank you": ("You're welcome!", "Anytime!", "Glad I could help!"),
    "how can I help you?": ("You can ask me anything!", "I'm here to assist you!"),
    "tell me more": ("What would you like to know?", "I'm all ears!"),
    "I'm bored": ("Let's chat! Tell me something interesting.", "I can tell you a joke or a fun fact!")
}

# Function to get response from the bot
def get_response(user_input):
    if user_input.lower() in responses:
        return random.choice(responses[user_input.lower()])
    else:
        return "I'm sorry, I don't understand that."

# Main function to run the chatbot
def chat():

    print("Hello! I'm your chatbot. Ask me anything or just say 'bye' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'bye':
            print(random.choice(responses["bye"]))  # Random farewell message
            break
        else:
            response = get_response(user_input)
            print("Bot:", response)

# Run the chatbot
if __name__ == "__main__":
    chat()
