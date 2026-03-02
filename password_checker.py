import re

print("Program Started")

password = input("Enter Password: ")

if len(password) < 8:
    print("Weak: Minimum 8 characters required")
elif not re.search("[A-Z]", password):
    print("Weak: Add at least one uppercase letter")
elif not re.search("[a-z]", password):
    print("Weak: Add at least one lowercase letter")
elif not re.search("[0-9]", password):
    print("Weak: Add at least one number")
elif not re.search("[@#$%^&*]", password):
    print("Weak: Add at least one special character")
else:
    print("Strong Password 💪")