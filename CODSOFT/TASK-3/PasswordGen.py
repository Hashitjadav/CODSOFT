import string
import random

def get_master_password():
    return input("What is the master password? ")

def view():
    try:
        with open('password.txt', 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No passwords stored yet. Please add some passwords first.")
                return
            for line in lines:
                data = line.strip()
                if "|" in data:
                    user, password = data.split("|", 1)
                    print(f"Name: {user}, Password: {password}")
                else:
                    print(f"Skipping line with unexpected format: {data}")
    except FileNotFoundError:
        print("No passwords stored yet. Please add some passwords first.")

def add():
    name = input("Enter name: ")
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Enter password length: "))

    if plen < 8:
        print("Password length should be at least 8 characters.")
        return

    s = s1 + s2 + s3 + s4
    generated_password = ''.join(random.choices(s, k=plen))
    print("Your Password is:", generated_password)

    with open('password.txt', 'a') as f:
        f.write(f"{name}|{generated_password}\n")

def main():
    master_pwd = get_master_password()  # Store or use master password as needed
    while True:
        mode = input("Would you like to add a new password or view old ones (view, add), press q to quit: ").lower()
        if mode == "q":
            break
        elif mode == "view":
            view()
        elif mode == "add":
            add()
        else:
            print("Invalid mode. Please enter 'view', 'add', or 'q' to quit.")

if __name__ == "__main__":
    main()
