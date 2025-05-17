# ------------------------PROBLEM STATEMENT:
'''
Write a program that loops through a dictionary of fruits, prompting the user to see how many of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
'''
# import for password login
from hashlib import sha256
# login function
def login(email, logins, password_check):
# Check if the hashed password matches the stored one otherwise it will be false   
    if logins[email] == hashed_password(password_check):
        return True
    return False

# encodes password and change it into hash
def hashed_password(password):
    return sha256(password.encode()).hexdigest()

def main():
#dictionary of emails and hash passwords
    logins = {
        "abc123@gmail.com": "5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8",
        "example@21.yahoo": "973607a4ae7b4cf7d96a100b0fb07e8519cc4f70441d41214a9f811577bb06cc",
        "studyport@education": "882c6df720fd99f5eebb1581a1cf975625cea8a160283011c0b9512bb56c95fb"
    }
# test prints 
    print(login("abc123@gmail.com", logins, "password"))
    print(login("abc123@gmail.com", logins, "word"))
    
    print(login("example@21.yahoo", logins, "karel"))
    print(login("example@21.yahoo", logins, "Karel"))
    
    print(login("studyport@education", logins, "123!456?789"))
    print(login("studyport@education", logins, "password"))

# calling main function
if __name__ == '__main__':
    main()