import random
passlen = int(input("Enter the length of password: "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$^&*_"
password = ""
while passlen > 0:
    password = password + random.choice(s)
    passlen = passlen-1
print(password)
