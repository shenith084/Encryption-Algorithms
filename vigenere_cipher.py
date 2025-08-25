"""
ICT 3310 - Information Security
Vigenère Cipher Implementation
Author: Student Implementation
Description: Implementation of Vigenère Cipher encryption and decryption algorithms
"""

def prepare_key(text, key):
    """
    Prepares the key by repeating it to match the length of the text
    
    Args:
        text (str): The text to be encrypted/decrypted
        key (str): The encryption key
        
    Returns:
        str: Extended key matching the text length
    """
    # Remove non-alphabetic characters from text for key length calculation
    alpha_text = ''.join([char for char in text if char.isalpha()])
    key = key.upper()
    
    if len(alpha_text) <= len(key):
        return key[:len(alpha_text)]
    
    # Repeat the key to match text length
    extended_key = ""
    key_index = 0
    
    for char in alpha_text:
        extended_key += key[key_index % len(key)]
        key_index += 1
    
    return extended_key

def vigenere_encrypt(plaintext, key):
    """
    Encrypts plaintext using Vigenère cipher with given key
    
    Args:
        plaintext (str): Text to be encrypted
        key (str): Encryption key (alphabetic characters only)
        
    Returns:
        str: Encrypted ciphertext
    """
    if not key.isalpha():
        raise ValueError("Key must contain only alphabetic characters")
    
    extended_key = prepare_key(plaintext, key)
    ciphertext = ""
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            
            # Get shift value from key character
            shift = ord(extended_key[key_index]) - 65
            
            # Apply Vigenère encryption
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            ciphertext += encrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            ciphertext += char
    
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using Vigenère cipher with given key
    
    Args:
        ciphertext (str): Text to be decrypted
        key (str): Decryption key (same as encryption key)
        
    Returns:
        str: Decrypted plaintext
    """
    if not key.isalpha():
        raise ValueError("Key must contain only alphabetic characters")
    
    extended_key = prepare_key(ciphertext, key)
    plaintext = ""
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():
            # Determine if character is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            
            # Get shift value from key character
            shift = ord(extended_key[key_index]) - 65
            
            # Apply Vigenère decryption (subtract shift)
            decrypted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            plaintext += decrypted_char
            key_index += 1
        else:
            # Non-alphabetic characters remain unchanged
            plaintext += char
    
    return plaintext

def main():
    """
    Main function to handle user interaction and demonstrate Vigenère cipher
    """
    print("=" * 50)
    print("VIGENÈRE CIPHER IMPLEMENTATION")
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
            key = input("Enter encryption key (alphabetic characters only): ").strip()
            
            try:
                if key.isalpha():
                    encrypted = vigenere_encrypt(plaintext, key)
                    print(f"\nPlaintext:  {plaintext}")
                    print(f"Key:        {key.upper()}")
                    print(f"Ciphertext: {encrypted}")
                else:
                    print("Error: Key must contain only alphabetic characters")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '2':
            # Decryption process
            ciphertext = input("Enter ciphertext to decrypt: ")
            key = input("Enter decryption key: ").strip()
            
            try:
                if key.isalpha():
                    decrypted = vigenere_decrypt(ciphertext, key)
                    print(f"\nCiphertext: {ciphertext}")
                    print(f"Key:        {key.upper()}")
                    print(f"Plaintext:  {decrypted}")
                else:
                    print("Error: Key must contain only alphabetic characters")
            except ValueError as e:
                print(f"Error: {e}")
                
        elif choice == '3':
            print("Exiting Vigenère Cipher program...")
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
    text1 = "HELLO WORLD"
    key1 = "KEY"
    encrypted1 = vigenere_encrypt(text1, key1)
    decrypted1 = vigenere_decrypt(encrypted1, key1)
    
    print(f"\nSample 1:")
    print(f"Original:   {text1}")
    print(f"Key:        {key1}")
    print(f"Extended:   {prepare_key(text1, key1)}")
    print(f"Encrypted:  {encrypted1}")
    print(f"Decrypted:  {decrypted1}")
    
    # Sample 2
    text2 = "Information Security"
    key2 = "CIPHER"
    encrypted2 = vigenere_encrypt(text2, key2)
    decrypted2 = vigenere_decrypt(encrypted2, key2)
    
    print(f"\nSample 2:")
    print(f"Original:   {text2}")
    print(f"Key:        {key2}")
    print(f"Extended:   {prepare_key(text2, key2)}")
    print(f"Encrypted:  {encrypted2}")
    print(f"Decrypted:  {decrypted2}")

if __name__ == "__main__":
    # Run demonstration first
    demo_run()
    # Then run interactive program
    main()