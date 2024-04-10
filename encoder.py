# Szymon Sierzega 04/09/2024

def encode(password):
    new_password = ""

    for char in password:
        char = int(char)
        char += 3

        if char >= 10:
            char -= 10

        char = str(char)
        new_password += char

    return new_password

def decode(encoded_password):
    new_password = ""
    for char in str(encoded_password):
        char = int(char)
        char -= 3
        if char < 0:
            char += 10
        new_password += str(char)
    return new_password


def main():
    encoded_password = " "
    while True:

        print("Menu "
              "\n-------------"
              "\n1. Encode"
              "\n2. Decode"
              "\n3. Quit"
              "\n")

        user_input = input("Please enter an option: ")

        if user_input == "1":
            password_input = str(input("Please enter your password to encode: "))
            encoded_password = encode(password_input)
            print("Your password has been encoded and stored!")

        elif user_input == "2":
            decoded_password = decode(encoded_password)  # decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}')

        elif user_input == '3':
            break

        else:
            print("Invalid option, please try again!")


if __name__ == "__main__":
    main()
