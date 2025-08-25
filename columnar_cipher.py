"""
ICT 3310 - Information Security
Columnar Cipher Implementation
Author: Student Implementation
Description: Implementation of Columnar Cipher encryption and decryption algorithms
"""

def get_column_order(key):
    """
    Determines the column order based on alphabetical sorting of the key
    
    Args:
        key (str): The encryption key
        
    Returns:
        list: List of column indices in sorted order
    """
    # Create pairs of (character, original_index)
    key_chars = [(char.upper(), i) for i, char in enumerate(key)]
    
    # Sort by character, then by original index for ties
    sorted_chars = sorted(key_chars, key=lambda x: (x[0], x[1]))
    
    # Return the original indices in sorted order
    return [pair[1] for pair in sorted_chars]

def columnar_encrypt(plaintext, key):
    """
    Encrypts plaintext using Columnar cipher with given key
    
    Args:
        plaintext (str): Text to be encrypted
        key (str): Encryption key (determines column arrangement)
        
    Returns:
        str: Encrypted ciphertext
    """
    if not key:
        return plaintext
    
    # Remove spaces and convert to uppercase for processing
    processed_text = plaintext.replace(' ', '').upper()
    key_length = len(key)
    
    # Calculate number of rows needed
    num_rows = len(processed_text) // key_length
    if len(processed_text) % key_length != 0:
        num_rows += 1
        # Pad with 'X' to fill the grid
        processed_text += 'X' * (num_rows * key_length - len(processed_text))
    
    # Create grid and fill it row by row
    grid = []
    for i in range(num_rows):
        row = []
        for j in range(key_length):
            char_index = i * key_length + j
            if char_index < len(processed_text):
                row.append(processed_text[char_index])
            else:
                row.append('X')  # Padding
        grid.append(row)
    
    # Get column order based on key
    column_order = get_column_order(key)
    
    # Read columns in the specified order
    ciphertext = ""
    for col_index in column_order:
        for row in grid:
            ciphertext += row[col_index]
    
    return ciphertext

def columnar_decrypt(ciphertext, key):
    """
    Decrypts ciphertext using Columnar cipher with given key
    
    Args:
        ciphertext (str): Text to be decrypted
        key (str): Decryption key (same as encryption key)
        
    Returns:
        str: Decrypted plaintext
    """
    if not key:
        return ciphertext
    
    key_length = len(key)
    num_rows = len(ciphertext) // key_length
    
    # Get column order
    column_order = get_column_order(key)
    
    # Create empty grid
    grid = [['' for _ in range(key_length)] for _ in range(num_rows)]
    
    # Fill grid column by column in the order specified by key
    char_index = 0
    for col_index in column_order:
        for row in range(num_rows):
            grid[row][col_index] = ciphertext[char_index]
            char_index += 1
    
    # Read grid row by row to get plaintext
    plaintext = ""
    for row in grid:
        plaintext += ''.join(row)
    
    # Remove trailing 'X' padding
    return plaintext.rstrip('X')

def visualize_grid(text, key, operation="encrypt"):
    """
    Visualizes the columnar cipher grid for better understanding
    
    Args:
        text (str): Text to visualize
        key (str): Encryption/decryption key
        operation (str): "encrypt" or "decrypt"
        
    Returns:
        str: Visual representation of the grid
    """
    if not key:
        return text
    
    key_length = len(key)
    
    if operation == "encrypt":
        # For encryption visualization
        processed_text = text.replace(' ', '').upper()
        num_rows = len(processed_text) // key_length
        if len(processed_text) % key_length != 0:
            num_rows += 1
            processed_text += 'X' * (num_rows * key_length - len(processed_text))
        
        # Create and fill grid
        grid = []
        for i in range(num_rows):
            row = []
            for j in range(key_length):
                char_index = i * key_length + j
                if char_index < len(processed_text):
                    row.append(processed_text[char_index])
                else:
                    row.append('X')
            grid.append(row)
    
    # Create visualization
    column_order = get_column_order(key)
    visualization = "Key:     " + " ".join(key.upper()) + "\n"
    visualization += "Order:   " + " ".join([str(i+1) for i in column_order]) + "\n"
    visualization += "-" * (key_length * 2 + 7) + "\n"
    
    if operation == "encrypt":
        for row in grid:
            visualization += "         " + " ".join(row) + "\n"
    
    return visualization

def main():
    """
    Main function to handle user interaction and demonstrate Columnar cipher
    """
    print("=" * 50)
    print("COLUMNAR CIPHER IMPLEMENTATION")
    print("=" * 50)
    
    while True:
        print("\nSelect operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Visualize Grid")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Encryption process
            plaintext = input("Enter plaintext to encrypt: ")
            key = input("Enter encryption key: ").strip()
            
            if key and key.isalpha():
                encrypted = columnar_encrypt(plaintext, key)
                print(f"\nPlaintext:  {plaintext}")
                print(f"Key:        {key.upper()}")
                print(f"Ciphertext: {encrypted}")
            else:
                print("Error: Key must be non-empty and contain only alphabetic characters")
                
        elif choice == '2':
            # Decryption process
            ciphertext = input("Enter ciphertext to decrypt: ")
            key = input("Enter decryption key: ").strip()
            
            if key and key.isalpha():
                decrypted = columnar_decrypt(ciphertext, key)
                print(f"\nCiphertext: {ciphertext}")
                print(f"Key:        {key.upper()}")
                print(f"Plaintext:  {decrypted}")
            else:
                print("Error: Key must be non-empty and contain only alphabetic characters")
        
        elif choice == '3':
            # Grid visualization
            text = input("Enter text to visualize: ")
            key = input("Enter key: ").strip()
            
            if key and key.isalpha():
                print(f"\nGrid Visualization:")
                print(visualize_grid(text, key))
            else:
                print("Error: Key must be non-empty and contain only alphabetic characters")
                
        elif choice == '4':
            print("Exiting Columnar Cipher program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

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
    encrypted1 = columnar_encrypt(text1, key1)
    decrypted1 = columnar_decrypt(encrypted1, key1)
    
    print(f"\nSample 1:")
    print(f"Original:   {text1}")
    print(f"Key:        {key1}")
    print(f"Column Order: {get_column_order(key1)}")
    print(f"Encrypted:  {encrypted1}")
    print(f"Decrypted:  {decrypted1}")
    print("Grid Visualization:")
    print(visualize_grid(text1, key1))
    
    # Sample 2
    text2 = "INFORMATION SECURITY"
    key2 = "CIPHER"
    encrypted2 = columnar_encrypt(text2, key2)
    decrypted2 = columnar_decrypt(encrypted2, key2)
    
    print(f"\nSample 2:")
    print(f"Original:   {text2}")
    print(f"Key:        {key2}")
    print(f"Column Order: {get_column_order(key2)}")
    print(f"Encrypted:  {encrypted2}")
    print(f"Decrypted:  {decrypted2}")
    print("Grid Visualization:")
    print(visualize_grid(text2, key2))

if __name__ == "__main__":
    # Run demonstration first
    demo_run()
    # Then run interactive program
    main()