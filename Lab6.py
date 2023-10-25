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
        if encoded_password is not None and og_password is not None:
            print(f"The encoded password is {encoded_password}, and the original password is {og_password}.\n")
        else:
            print("No password has been encoded yet.")

    elif user_input == "3":
        break
