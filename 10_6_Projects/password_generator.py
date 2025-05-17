import random
import string

def generating_password(length):
  characters = string.ascii_uppercase + string.digits

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

length_of_password = int(input("Enter the password length: "))
password = generating_password(length_of_password)

print("Here is your generated password", password)