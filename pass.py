from cryptography.fernet import Fernet

def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)

write_key()

name = input(str("Enter your name to start it : "))
# key = load()+name.encode()
# fer = Fernet(key)


def view():
  with open('pass.txt', 'r') as f:
    for line in f.readlines():
      data = line.rstrip()
      print(data)


def add():
  new_name = input("Enter your name : ")
  new_pwd = input("Enter new password : ")
  with open('pass.txt', 'a') as f:
    f.write(f"User name : {new_name} , Password : {new_pwd}\n")


while True:
  pwd = input(
      "Would you want to add a new password or view (view/add/quit) :)")
  if (pwd == "quit"):
    break
  elif (pwd == "add"):
    add()

  elif (pwd == "view"):
    view()

  else:
    print("Invaild input")
    continue
