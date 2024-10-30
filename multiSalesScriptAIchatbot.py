import random
from transformers import pipeline

# Initialize the NLP model for response generation
nlp = pipeline("conversational", model="microsoft/DialoGPT-large")

# Sample sales script flows
sales_flows = {
    "greeting": [
        "Hi there! How can I assist you today?",
        "Hello! What brings you here today?"
    ],
    "product_info": [
        "We have a variety of products. Can you specify what you're interested in?",
        "Are you looking for something specific?"
    ],
    "closing": [
        "Would you like to proceed with your purchase?",
        "Can I help you with the checkout process?"
    ]
}

# Predefined responses for scoring
predefined_responses = {
    "yes": ["yes", "sure", "absolutely", "definitely"],
    "no": ["no", "not really", "no thanks"],
    "help": ["help", "assistance", "support"]
}

# Scoring function
def score_response(user_input, expected_responses):
    score = 0
    for response in expected_responses:
        if response in user_input.lower():
            score += 1
    return score

# Main chatbot function
def chatbot_flow():
    flow = "greeting"
    print(random.choice(sales_flows[flow]))

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Thank you for chatting! Goodbye!")
            break
        
        if flow == "greeting":
            flow = "product_info"
            print(random.choice(sales_flows[flow]))

        elif flow == "product_info":
            score = score_response(user_input, predefined_responses["help"])
            if score > 0:
                print("Chatbot: Sure! I'm here to help. What do you need assistance with?")
            else:
                flow = "closing"
                print(random.choice(sales_flows[flow]))

        elif flow == "closing":
            score = score_response(user_input, predefined_responses["yes"])
            if score > 0:
                print("Chatbot: Great! Let's proceed with your purchase.")
                break
            else:
                score = score_response(user_input, predefined_responses["no"])
                if score > 0:
                    print("Chatbot: No problem! Let me know if you need anything else.")
                    break

# Entry point for the chatbot
if __name__ == "__main__":
    chatbot_flow()
