import random


def generate_password(length_of_password):
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    alpha_upper = alpha.upper()
    special_char = '!@#$%^&*'
    num = '0123456789'
    characters = (alpha + alpha_upper + special_char + num)
    your_password = []

    for i in range(length_of_password):
        passw = random.choice(characters)
        characters = characters.replace(passw, '')
        your_password.append(passw)

    return ''.join(your_password)

length_of_password = int(input("Length of password requested: "))
password = generate_password(length_of_password)
print(password)
