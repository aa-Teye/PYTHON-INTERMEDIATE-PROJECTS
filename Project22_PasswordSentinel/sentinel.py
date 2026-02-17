import re

def analyze_password(password):
    score = 0
    feedback = []

    # 1. Blacklist Check (The "Smarter" Security Layer)
    # Even if complex, these words make a password weak.
    blacklist = ["password", "admin", "12345", "qwerty", "ghana", "overcomers"]
    if any(word in password.lower() for word in blacklist):
        print("\n CRITICAL: Password contains a forbidden common word.")
        score = 0 
    else:
        # 2. Length Check
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
        else:
            feedback.append("Increase length to at least 12 characters.")

        # 3. Complexity Checks (Regex)
        if re.search(r"[A-Z]", password): score += 1
        else: feedback.append("Add uppercase letters (A-Z).")

        if re.search(r"[a-z]", password): score += 1
        else: feedback.append(" Add lowercase letters (a-z).")

        if re.search(r"\d", password): score += 1
        else: feedback.append("Add numbers (0-9).")

        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
        else: feedback.append("Add special characters (e.g., @, #, $).")

    # 4. Final Rating Output
    print("\n--- Security Audit Report ---")
    if score >= 5:
        print(" Rating: STRONG")
    elif score >= 3:
        print(" Rating: MODERATE")
    else:
        print(" Rating: WEAK")

    if feedback:
        print("\nSuggestions to improve:")
        for item in feedback:
            print(item)

def main():
    while True: # Added a loop so you can test multiple passwords
        print("\n=== PROJECT 22: PASSWORD SENTINEL ===")
        user_pass = input("Enter a password to test (or type 'exit' to quit): ")
        
        if user_pass.lower() == 'exit':
            print("Sentinel shutting down. Stay secure!")
            break
            
        analyze_password(user_pass)

if __name__ == "__main__":
    main()