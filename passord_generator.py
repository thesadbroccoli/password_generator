import random
import mysql.connector

lc = 'abcdefghijklmnopqrstuvwxyz'
uc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '0123456789'
symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?/~'

def generate_password(strength="medium", length=12):
    if strength == "simple":
        characters = lc + uc
    elif strength == "medium":
        characters = lc + uc + num
    else:  
        characters = lc + uc + num + symbols

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_db(username, password):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin",
        database="password_db"
    )
    
    cursor = connection.cursor()

    query = "INSERT INTO passwords (username, password) VALUES (%s, %s)"
    cursor.execute(query, (username, password))

    connection.commit()

    cursor.close()
    connection.close()

    print("Password saved successfully!")

def main():
    while True:
        print("\n--- Password Generator Menu ---")
        print("1. Generate Simple Password (Only Letters)")
        print("2. Generate Medium Password (Letters + Digits)")
        print("3. Generate Strong Password (Letters + Digits + Symbols)")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == "4":
            print("Exiting...")
            break

        elif choice in ["1", "2", "3"]:
            length = int(input("Enter the desired length of the password: "))
            
            username = input("Enter a username: ")

            strength = "simple" if choice == "1" else "medium" if choice == "2" else "strong"
            
            password = generate_password(strength, length)
            print("Generated Password:", password)

            save_option = input("Do you want to save this password to the database? (y/n): ").lower()
            if save_option == "y":
                save_password_to_db(username, password)
        
        else:
            print("Invalid choice.")


 main()
