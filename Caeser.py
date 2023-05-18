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
        if char.isalpha():
            encrypted_char = key.get(char.upper(), char).upper()
        else:
            encrypted_char = char
        cipher += encrypted_char
    return cipher

def decrypt(ciphertext):
    valid_messages = []
    for key in range(26):
        plaintext = ""
        for char in ciphertext:
            if char.isalpha():
                if char.isupper():
                    decrypted_char = chr((ord(char) - 65 - key) % 26 + 65)
                else:
                    decrypted_char = chr((ord(char) - 97 - key) % 26 + 97)
            else:
                decrypted_char = char
            plaintext += decrypted_char
        if all(char.isalpha() or char.isspace() for char in plaintext):
            valid_messages.append(plaintext)
    return valid_messages

while True:
    print("Caesar Cipher Program")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Break the cipher")
    print("4. Reset and start from the beginning")
    print("5. Exit")
    choice = input("Please choose an option (1-5): ")

    if choice == "1":
        key_input = input("Please input key: ")
        try:
            key = int(key_input)
            message_input = input("Please input message: ")
            key = generate_key(key)
            cipher = encrypt(key, message_input)
            print("\nEncrypted message:", cipher)
            print()
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
    elif choice == "2":
        key_input = input("Please input key: ")
        try:
            key = int(key_input)
            message_input = input("Please input message: ")
            key = generate_key(-key)
            plaintext = encrypt(key, message_input)
            print("\nDecrypted message:", plaintext)
            print()
        except ValueError:
            print("Invalid input. Please enter a valid integer.\n")
    elif choice == "3":
        ciphertext = input("Please input ciphertext to break: ")
        print("\nBrute-Force Decryption:")
        valid_messages = decrypt(ciphertext)
        if valid_messages:
            for i, message in enumerate(valid_messages, start=1):
                print("Valid decrypted message", i, ":", message)
        else:
            print("No valid decrypted messages found.")
        print()
    elif choice == "4":
        continue
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).\n")
