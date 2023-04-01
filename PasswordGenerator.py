import random
def generate_password(length_of_password):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha.upper()
    special_char = '!@#$%^&*'
    num = '0123456789'
    # adding all possible characters
    characters = (alpha + alpha_upper + special_char + num)
    your_password = []

    # loop to generate the password based on the length provided
    for i in range(length_of_password):
        passw = random.choice(characters)
        # prevent duplicates
        characters = characters.replace(passw, '')
        your_password.append(passw)

    return ''.join(your_password)

length_of_password = int(input("Length of password requested: "))
password = generate_password(length_of_password)
print(password)