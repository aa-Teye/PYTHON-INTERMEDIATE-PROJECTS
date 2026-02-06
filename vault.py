import os
from cryptography.fernet import Fernet

def generate_and_save_key():
    """Generates a master key file if it doesn't exist."""
    if not os.path.exists("master.key"):
        key = Fernet.generate_key()
        with open("master.key", "wb") as key_file:
            key_file.write(key)
        print("[!] NEW KEY GENERATED: Keep 'master.key' safe!")

def load_key():
    """Loads the secret key from the current directory."""
    return open("master.key", "rb").read()

def encrypt_message(message):
    """Turns readable text into unreadable gibberish."""
    key = load_key()
    f = Fernet(key)
    return f.encrypt(message.encode())

def decrypt_message(encrypted_data):
    """Turns the gibberish back into readable text."""
    key = load_key()
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

if __name__ == "__main__":
    generate_and_save_key()
    
    choice = input("Do you want to (1) Encrypt or (2) Decrypt? ")
    
    if choice == '1':
        secret = input("Enter the secret message to hide: ")
        encrypted = encrypt_message(secret)
        print(f"\n[LOCKED]: {encrypted}")
        # Save it to a file
        with open("secret_vault.txt", "wb") as vault:
            vault.write(encrypted)
        print("Done! Your secret is saved in 'secret_vault.txt'")
        
    elif choice == '2':
        if os.path.exists("secret_vault.txt"):
            with open("secret_vault.txt", "rb") as vault:
                content = vault.read()
            decrypted = decrypt_message(content)
            print(f"\n[UNLOCKED]: {decrypted}")
        else:
            print("[ERROR] No vault file found!")