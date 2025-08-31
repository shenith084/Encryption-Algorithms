def caesar_encrypt(plaintext, shift):
    
    ciphertext = ""
    
    for char in plaintext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            # Apply Caesar shift with wrap-around using modulo
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += shifted_char
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    
    return ciphertext

def caesar_decrypt(ciphertext, shift):
   
    # Decryption is encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)

def main():
   
    print("=" * 50)
    print("CAESAR CIPHER")
    print("=" * 50)
    
    while True:
        print("\nSelect operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Encryption process
            plaintext = input("Enter plaintext to encrypt: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                if 0 <= shift <= 25:
                    encrypted = caesar_encrypt(plaintext, shift)
                    print(f"\nPlaintext:  {plaintext}")
                    print(f"Shift:      {shift}")
                    print(f"Ciphertext: {encrypted}")
                else:
                    print("Error: Shift value must be between 0 and 25")
            except ValueError:
                print("Error: Please enter a valid integer for shift value")
                
        elif choice == '2':
            # Decryption process
            ciphertext = input("Enter ciphertext to decrypt: ")
            try:
                shift = int(input("Enter shift value used for encryption: "))
                if 0 <= shift <= 25:
                    decrypted = caesar_decrypt(ciphertext, shift)
                    print(f"\nCiphertext: {ciphertext}")
                    print(f"Shift:      {shift}")
                    print(f"Plaintext:  {decrypted}")
                else:
                    print("Error: Shift value must be between 0 and 25")
            except ValueError:
                print("Error: Please enter a valid integer for shift value")
                
        elif choice == '3':
            print("Exiting Caesar Cipher program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()