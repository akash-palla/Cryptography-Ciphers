import string

def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + shift) % 26 + base)
            result += shifted_char
        else:
         # Keep non-alphabet characters unchanged
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
  # Decryption is the same as encryption with a negative shift value
    return caesar_cipher_encrypt(text, -shift)

def vigenere_cipher_encrypt(text, keyword):
  # Convert the keyword to a list of shift values (0-25) based on the alphabet position
    keyword = keyword.upper()
    key = [ord(c) - ord('A') for c in keyword]
    result = []
    key_idx = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - base + key[key_idx]) % 26 + base)
            result.append(shifted_char)
            key_idx = (key_idx + 1) % len(key)
        else:
            result.append(char)
    return "".join(result)

def vigenere_cipher_decrypt(text, keyword):
    keyword = keyword.upper()
    key = [-ord(c) + ord('A') for c in keyword]
    result = []
    key_idx = 0
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            # Shift the character back by the corresponding key value, wrapping around if necessary
            shifted_char = chr((ord(char) - base + key[key_idx]) % 26 + base)
            result.append(shifted_char)
            key_idx = (key_idx + 1) % len(key)
        else:
            result.append(char)
    return "".join(result)

def main():
    while True:
        print("\nChoose a cipher:")
        print("1. Caesar Cipher")
        print("2. Vigenere Cipher")
        print("3. Exit")
        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            text = input("Enter the message: ")
            shift = int(input("Enter the shift value: "))
            encrypt_or_decrypt = input("Encrypt or Decrypt? (e/d): ")
            if encrypt_or_decrypt.lower() == 'e':
                encrypted_text = caesar_cipher_encrypt(text, shift)
                print(f"Encrypted message: {encrypted_text}")
            elif encrypt_or_decrypt.lower() == 'd':
                decrypted_text = caesar_cipher_decrypt(text, shift)
                print(f"Decrypted message: {decrypted_text}")
            else:
                print("Invalid input. Please choose 'e' for encryption or 'd' for decryption.")
        elif choice == 2:
            text = input("Enter the message: ")
            keyword = input("Enter the keyword: ")
            encrypt_or_decrypt = input("Encrypt or Decrypt? (e/d): ")
            if encrypt_or_decrypt.lower() == 'e':
                encrypted_text = vigenere_cipher_encrypt(text, keyword)
                print(f"Encrypted message: {encrypted_text}")
            elif encrypt_or_decrypt.lower() == 'd':
                decrypted_text = vigenere_cipher_decrypt(text, keyword)
                print(f"Decrypted message: {decrypted_text}")
            else:
                print("Invalid input. Please choose 'e' for encryption or 'd' for decryption.")
        elif choice == 3:
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
