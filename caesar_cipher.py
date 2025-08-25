"""
ICT 3310 - Information Security
Caesar Cipher Implementation
Author: Student Implementation
Description: Implementation of Caesar Cipher encryption and decryption algorithms
"""

def caesar_encrypt(plaintext, shift):
    """
    Encrypts plaintext using Caesar cipher with given shift value
    
    Args:
        plaintext (str): Text to be encrypted
        shift (int): Number of positions to shift each character
        
    Returns:
        str: Encrypted ciphertext
    """
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
    """
    Decrypts ciphertext using Caesar cipher with given shift value
    
    Args:
        ciphertext (str): Text to be decrypted
        shift (int): Number of positions to shift back each character
        
    Returns:
        str: Decrypted plaintext
    """
    # Decryption is encryption with negative shift
    return caesar_encrypt(ciphertext, -shift)

def main():
    """
    Main function to handle user interaction and demonstrate Caesar cipher
    """
    print("=" * 50)
    print("CAESAR CIPHER IMPLEMENTATION")
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

def demo_run():
    """
    Demonstration function showing sample inputs and outputs
    """
    print("\n" + "=" * 50)
    print("SAMPLE DEMONSTRATION")
    print("=" * 50)
    
    # Sample 1
    text1 = "Hello World"
    shift1 = 3
    encrypted1 = caesar_encrypt(text1, shift1)
    decrypted1 = caesar_decrypt(encrypted1, shift1)
    
    print(f"\nSample 1:")
    print(f"Original:   {text1}")
    print(f"Shift:      {shift1}")
    print(f"Encrypted:  {encrypted1}")
    print(f"Decrypted:  {decrypted1}")
    
    # Sample 2
    text2 = "CRYPTOGRAPHY"
    shift2 = 13
    encrypted2 = caesar_encrypt(text2, shift2)
    decrypted2 = caesar_decrypt(encrypted2, shift2)
    
    print(f"\nSample 2:")
    print(f"Original:   {text2}")
    print(f"Shift:      {shift2}")
    print(f"Encrypted:  {encrypted2}")
    print(f"Decrypted:  {decrypted2}")

if __name__ == "__main__":
    # Run demonstration first
    demo_run()
    # Then run interactive program
    main()