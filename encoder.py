# Szymon Sierzega 04/09/2024

def encode(password):

    new_password = ""

    for char in password:
        char = int(char)
        char += 3

        if char >= 10:
            char = 0

        char = str(char)
        new_password += char

    return new_password


print(encode("12345555"))


