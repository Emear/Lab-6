poop = True

encoded_password = None  # Initialize the encoded password variable
og_password = None  # Initialize the original password variable


def encode_password(password):
    encoded = ""
    for char in str(password):
        if char.isdigit():
            digit = int(char)
            if 0 <= digit <= 6:
                encoded_digit = (digit + 3) % 10
            else:
                encoded_digit = (digit - 7) % 10
            encoded += str(encoded_digit)
        else:
            encoded += char
    return encoded

def decode_password(option, password):
    if option == '2':
        encodedPassword = ''

        for i in range(len(password)):
            encodedPassword += (str((int(password[i]) + 3) % 10))

        print(f"The encoded password is {encodedPassword}, and the original password is {password}.\n")

    return

def menu_display():  # Function for the menu
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit\n")


while True:
    menu_display()
    user_input = input("Please enter an option: ")

    if user_input == "1":
        og_password = input("Please enter your password to encode: ")
        encoded_password = encode_password(og_password)
        print("Your password has been encoded and stored!\n")

    elif user_input == "2":
        decode_password(user_input, og_password)

    elif user_input == "3":
        break
