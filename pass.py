from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

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
        continue

