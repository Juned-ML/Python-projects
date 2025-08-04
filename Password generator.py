import random
import string

#this is a basic password generator
#please creaete your password using my program 
length_password = int(input("enter the length of password: "))

password_length = string.ascii_letters + string.punctuation + string.digits

password = "".join(random.choice(password_length)
for _ in range(length_password))

print(f"your password is {password}")
print("thanks to take my help to genearate your password with my program")


