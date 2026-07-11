def encrypt(text, shift):
    encrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                encrypted += chr((ord(char) - 65 + shift) % 26 + 65)

            else:
                encrypted += chr((ord(char) - 97 + shift) % 26 + 97)

        else:
            encrypted += char

    return encrypted


def decrypt(text, shift):
    decrypted = ""

    for char in text:

        if char.isalpha():

            if char.isupper():
                decrypted += chr((ord(char) - 65 - shift) % 26 + 65)

            else:
                decrypted += chr((ord(char) - 97 - shift) % 26 + 97)

        else:
            decrypted += char

    return decrypted


message = input("Enter Message: ")
shift = int(input("Enter Shift Key: "))

encrypted_text = encrypt(message, shift)

print("\nEncrypted Text:", encrypted_text)

decrypted_text = decrypt(encrypted_text, shift)

print("Decrypted Text:", decrypted_text)