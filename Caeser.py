def generate_key(n):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    key = {}
    counter = 0
    for c in letters:
        key[c] = letters[(counter + n) % len(letters)]
        counter += 1
    return key

def encrypt(key, message):
    cipher = ""
    for char in message:
        if char.isalpha():  # Process only alphabetical characters
            encrypted_char = key.get(char.upper(), char).upper()  # Shift letter using the generated key and convert to uppercase
        else:
            encrypted_char = char  # Preserve non-alphabetical characters
        cipher += encrypted_char
    return cipher

def decrypt(key, cipher):
    decrypted_message = ""
    for char in cipher:
        if char.isalpha():  # Process only alphabetical characters
            decrypted_char = key.get(char.upper(), char).upper()  # Reverse-shift letter using the generated key and convert to uppercase
        else:
            decrypted_char = char  # Preserve non-alphabetical characters
        decrypted_message += decrypted_char
    return decrypted_message


while True:
    option_input = input("Please choose an option: (1) Encrypt, (2) Decrypt: ")
    if option_input == "1" or option_input == "2":
        break
    else:
        print("Invalid option. Please choose either 1 or 2.")

if option_input == "1":
    while True:
        key_input = input("Please input key: ")
        try:
            key = int(key_input)
            break  # Break the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    message_input = input("Please input message: ")

    key = generate_key(key)
    cipher = encrypt(key, message_input)

    print("\nMessage prior encryption:", message_input)
    print("Message after encryption:", cipher)

elif option_input == "2":
    while True:
        key_input = input("Please input key: ")
        try:
            key = int(key_input)
            break  # Break the loop if the input is a valid integer
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    cipher_input = input("Please input cipher text: ")

    key = generate_key(-key)  # Negative key to perform reverse shift for decryption
    decrypted_cipher = decrypt(key, cipher_input)

    print("\nThe decrypted cipher message is:", decrypted_cipher)
