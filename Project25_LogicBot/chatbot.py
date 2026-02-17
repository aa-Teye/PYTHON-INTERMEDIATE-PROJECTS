import time

def get_response(user_input):
    # Normalize input: lowercase and remove punctuation logic
    processed_input = user_input.lower().split()

    # The Bot's Knowledge Base (Intent Mapping)
    knowledge = {
        "greeting": {
            "keywords": ["hello", "hi", "hey", "good morning", "greetings"],
            "response": "Hello Alex! I am your Python Assistant. How can I help you with your IT work today?"
        },
        "status": {
            "keywords": ["how", "are", "you", "doing", "status"],
            "response": "My systems are running at 100% efficiency. Ready to code!"
        },
        "church": {
            "keywords": ["church", "overcomers", "youth", "ministry", "media"],
            "response": "The Haven ONCYM media systems are configured. Do you need to check the livestream status?"
        },
        "laptop": {
            "keywords": ["laptop", "price", "sale", "dominion", "buy"],
            "response": "The current inventory for Dominion Tech Solutions is updated. Most students are looking for Core i5 models."
        },
        "project": {
            "keywords": ["30", "projects", "progress", "day"],
            "response": "You are currently on Project 25 of 30. You are in the final stretch!"
        },
    
        "identity": {
            "keywords": ["name", "who", "am", "i"],
            "response": "Your name is Alex Teye Ametepey, President of The Haven ONCYM and CEO of Dominion Tech Solutions."
        },
        "capabilities": {
            "keywords": ["what", "can", "you", "do", "help", "abilities"],
            "response": "I can audit your network, check your disk space, verify password strength, and track your 30-day coding progress!"
        },
        "affirmation": {
            "keywords": ["yes", "sure", "ok", "cool", "agree"],
            "response": "Excellent! I'm glad we're on the same page. What's our next move, Alex?"
        },
        # ... keep your other categories (church, laptop, etc.)
    }

    # Logic: Find the category with the most keyword matches
    best_match = None
    max_matches = 0

    for category, data in knowledge.items():
        matches = 0
        for word in processed_input:
            if word in data["keywords"]:
                matches += 1
        
        if matches > max_matches:
            max_matches = matches
            best_match = category

    if best_match:
        return knowledge[best_match]["response"]
    else:
        return "I'm not quite sure I understand. Could you rephrase that for me?"

def main():
    print("--- Sentinel-Bot v1.0 (Python Logic) ---")
    print("Type 'quit' or 'exit' to end the chat.\n")
    
    while True:
        user_text = input("You: ")
        
        if user_text.lower() in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! Stay productive.")
            break
            
        print("Bot: Thinking...")
        time.sleep(0.5) # Simulating "thought" process
        
        response = get_response(user_text)
        print(f"Bot: {response}\n")

if __name__ == "__main__":
    main()