# Encoder Function
def encode(password):
    encoded_password = ""
    for digit in password:
        new_digit = str((int(digit) + 3) % 10)
        encoded_password += new_digit
    return encoded_password


# Decoder Function
def decode(encoded_password):
    decoded_password = ""
    for digit in encoded_password:
        original_digit = str((int(digit) - 3) % 10)
        decoded_password += original_digit
    return decoded_password


# Main Program
def main():
    while True:
        print("\nMenu\n-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")

        choice = input("Please enter an option: ")

        if choice == '1':
            password = input("Please enter your password to encode: ")
            encoded_password = encode(password)
            print("Your password has been encoded and stored!")
        elif choice == '2':
            if 'encoded_password' in locals():
                decoded_password = decode(encoded_password)
                print(f"The encoded password is {encoded_password}, and the original password is {decoded_password}.")
            else:
                print("Please encode a password first.")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose a valid option.")


if __name__ == "__main__":
    main()