from cryptography.fernet import Fernet
import os

def write_key():
    # generate new key
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("New encryption key generated and saved as 'key.key'.")
    else:
        print("'key.key' already exists. Skipping key generation.")

def load_key():
    if os.path.exists("key.key"):
        with open("key.key", "rb") as key_file:
            key = key_file.read()
            if len(key) == 44:
                return key
            else:
                raise ValueError("Invalid key length or format.")
    else:
        print("Key file 'key.key' not found. Generating a new key...")
        write_key()
        return load_key() 

write_key() 
try:
    key = load_key()
    fernet = Fernet(key)
except ValueError as e:
    print(f"An error occurred with the encryption key: {e}")
    os.remove("key.key")
    write_key()
    key = load_key()
    fernet = Fernet(key)
name = input("Enter your name to start: ")

def view():
    try:
        with open('pass.txt', 'r') as f:
            for line in f.readlines():
                if "User Name =" in line:
                    parts = line.rstrip().split(", ")
                    user = parts[0].split("= ")[1]
                    encrypted_pwd = parts[1].split("= ")[1]
                    decrypted_pwd = fernet.decrypt(encrypted_pwd.encode()).decode()
                    print(f"User: {user}, Password: {decrypted_pwd}")
    except FileNotFoundError:
        print("No passwords stored yet.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to add a new username and password
def add():
    new_name = input("Enter your name: ")
    new_pwd = input("Enter new password: ")
    encrypted_pwd = fernet.encrypt(new_pwd.encode()).decode()
    with open('pass.txt', 'a') as f:
        f.write(f"User Name = {new_name}, Password = {encrypted_pwd}\n")
    print("Password added and encrypted successfully!")
while True:
    action = input("Would you like to add a new password or view (view/add/quit): ").lower()
    if action == "quit":
        break
    elif action == "add":
        add()
    elif action == "view":
        view()
    else:
        print("Invalid input")
