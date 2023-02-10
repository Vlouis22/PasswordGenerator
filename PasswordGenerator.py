import random
'''A password generator that generates a random password
 from the length of the user input '''


class PasswordGenerator:
    # takes the length from the user
    def __init__(self, length):
        self.length = length
        self.characters = characters

    # algorithm for generating the password
    def generate_password(self):
        # empty set that will take from the random module
        your_password = []
        # makes the password equal to the length of the user request
        for ch in range(self.length):
            # generates random characters
            passw = random.randint(0, len(characters))
            # append those characters to the empty password set
            your_password.append(characters[passw])
        # return the password set as strings
        return ''.join(your_password)

# This will take the length of the password the user request
length_of_password = int(input("Length of password requested: "))
alpha = 'abcdefghijklmnopqrstuvwxyz'
alpha_upper = alpha.upper()
special_char = '!@#$%^&*'
num = '0123456789'
# Adds up all the possibilities from letters, numbers, and special characters
characters = (alpha + alpha_upper + special_char + num)

# Use class and length of the password
password_generator = PasswordGenerator(length_of_password)
# get password from the password generator and print it
password = password_generator.generate_password()
print(password)