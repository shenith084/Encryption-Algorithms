def rail_fence_encrypt(plaintext, num_rails):
   
    if num_rails <= 1:
        return plaintext
    
    # Create fence structure as list of lists
    fence = [[] for _ in range(num_rails)]
    
    # Variables to track current rail and direction
    current_rail = 0
    direction = 1  # 1 for down, -1 for up
    
    # Place each character in appropriate rail
    for char in plaintext:
        fence[current_rail].append(char)
        
        # Change direction at top and bottom rails
        if current_rail == 0:
            direction = 1
        elif current_rail == num_rails - 1:
            direction = -1
        
        # Move to next rail
        current_rail += direction
    
    # Read characters from fence row by row to create ciphertext
    ciphertext = ""
    for rail in fence:
        ciphertext += ''.join(rail)
    
    return ciphertext

def rail_fence_decrypt(ciphertext, num_rails):
    
    if num_rails <= 1:
        return ciphertext
    
    # Create fence structure to determine character positions
    fence = [[None for _ in range(len(ciphertext))] for _ in range(num_rails)]
    
    # Mark positions in the fence pattern
    current_rail = 0
    direction = 1
    
    for i in range(len(ciphertext)):
        fence[current_rail][i] = True
        
        # Change direction at top and bottom rails
        if current_rail == 0:
            direction = 1
        elif current_rail == num_rails - 1:
            direction = -1
        
        current_rail += direction
    
    # Fill the marked positions with characters from ciphertext
    char_index = 0
    for rail in range(num_rails):
        for col in range(len(ciphertext)):
            if fence[rail][col] is True:
                fence[rail][col] = ciphertext[char_index]
                char_index += 1
    
    # Read the fence in zigzag pattern to get plaintext
    plaintext = ""
    current_rail = 0
    direction = 1
    
    for col in range(len(ciphertext)):
        plaintext += fence[current_rail][col]
        
        # Change direction at top and bottom rails
        if current_rail == 0:
            direction = 1
        elif current_rail == num_rails - 1:
            direction = -1
        
        current_rail += direction
    
    return plaintext

def visualize_fence(text, num_rails):
   
    if num_rails <= 1:
        return text
    
    # Create visualization grid
    fence = [[' ' for _ in range(len(text))] for _ in range(num_rails)]
    
    current_rail = 0
    direction = 1
    
    for i, char in enumerate(text):
        fence[current_rail][i] = char
        
        if current_rail == 0:
            direction = 1
        elif current_rail == num_rails - 1:
            direction = -1
        
        current_rail += direction
    
    # Create visual representation
    visualization = ""
    for rail in fence:
        visualization += ''.join(rail) + '\n'
    
    return visualization.rstrip()

def main():
  
    
    print("RAIL FENCE CIPHER ")
    
    
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
                num_rails = int(input("Enter number of rails (minimum 2): "))
                if num_rails >= 2:
                    encrypted = rail_fence_encrypt(plaintext, num_rails)
                    print(f"\nPlaintext:  {plaintext}")
                    print(f"Rails:      {num_rails}")
                    print(f"Ciphertext: {encrypted}")
                else:
                    print("Error: Number of rails must be at least 2")
            except ValueError:
                print("Error: Please enter a valid integer for number of rails")
                
        elif choice == '2':
            # Decryption process
            ciphertext = input("Enter ciphertext to decrypt: ")
            try:
                num_rails = int(input("Enter number of rails used for encryption: "))
                if num_rails >= 2:
                    decrypted = rail_fence_decrypt(ciphertext, num_rails)
                    print(f"\nCiphertext: {ciphertext}")
                    print(f"Rails:      {num_rails}")
                    print(f"Plaintext:  {decrypted}")
                else:
                    print("Error: Number of rails must be at least 2")
            except ValueError:
                print("Error: Please enter a valid integer for number of rails")
                
        elif choice == '3':
            print("Exiting Rail Fence Cipher program...")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()