from cryptography.fernet import Fernet
import os

def generate_key():
    """Generates a key and saves it to a file"""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("New key generated and saved as 'secret.key'. Keep this safe!")

def load_key():
    """Loads the key from the current directory"""
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """Encrypts a string message"""
    key = load_key()
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    """Decrypts an encrypted byte string"""
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)
    return decrypted_message.decode()

if __name__ == "__main__":
    # Check if a key already exists; if not, create one
    if not os.path.exists("secret.key"):
        generate_key()

    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").upper()
    
    if choice == 'E':
        msg = input("Enter the message to secure: ")
        secret = encrypt_message(msg)
        print(f"Encrypted: {secret.decode()}")
    elif choice == 'D':
        coded_msg = input("Enter the encrypted string: ")
        try:
            plain_text = decrypt_message(coded_msg.encode())
            print(f"Decrypted: {plain_text}")
        except Exception as e:
            print("Error: Invalid key or corrupted message.")