"""
ICT 3310 - Information Security
Main Program - All Encryption Algorithms
Author: Student Implementation
Description: Unified interface for all four encryption algorithms
"""

import sys

# Import all cipher implementations
from caesar_cipher import caesar_encrypt, caesar_decrypt
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt
from rail_fence_cipher import rail_fence_encrypt, rail_fence_decrypt, visualize_fence
from columnar_cipher import columnar_encrypt, columnar_decrypt, visualize_grid

def display_main_menu():
    """Display the main menu for cipher selection"""
    print("\n" + "=" * 60)
    print("ICT 3310 - INFORMATION SECURITY")
    print("ENCRYPTION ALGORITHMS IMPLEMENTATION")
    print("=" * 60)
    print("\nSelect Cipher Algorithm:")
    print("1. Caesar Cipher")
    print("2. Vigenère Cipher") 
    print("3. Rail Fence Cipher")
    print("4. Columnar Cipher")
    print("5. Run All Demonstrations")
    print("6. Exit")
    print("=" * 60)

def caesar_menu():
    """Handle Caesar Cipher operations"""
    print("\n--- CAESAR CIPHER ---")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            try:
                shift = int(input("Enter shift value (0-25): "))
                if 0 <= shift <= 25:
                    result = caesar_encrypt(plaintext, shift)
                    print(f"Encrypted: {result}")
                else:
                    print("Shift must be between 0 and 25")
            except ValueError:
                print("Invalid shift value")
                
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            try:
                shift = int(input("Enter shift value: "))
                if 0 <= shift <= 25:
                    result = caesar_decrypt(ciphertext, shift)
                    print(f"Decrypted: {result}")
                else:
                    print("Shift must be between 0 and 25")
            except ValueError:
                print("Invalid shift value")
                
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def vigenere_menu():
    """Handle Vigenère Cipher operations"""
    print("\n--- VIGENÈRE CIPHER ---")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key (alphabetic only): ").strip()
            if key.isalpha():
                result = vigenere_encrypt(plaintext, key)
                print(f"Encrypted: {result}")
            else:
                print("Key must contain only alphabetic characters")
                
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ").strip()
            if key.isalpha():
                result = vigenere_decrypt(ciphertext, key)
                print(f"Decrypted: {result}")
            else:
                print("Key must contain only alphabetic characters")
                
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def rail_fence_menu():
    """Handle Rail Fence Cipher operations"""
    print("\n--- RAIL FENCE CIPHER ---")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            try:
                rails = int(input("Enter number of rails (≥2): "))
                if rails >= 2:
                    result = rail_fence_encrypt(plaintext, rails)
                    print(f"Encrypted: {result}")
                else:
                    print("Number of rails must be at least 2")
            except ValueError:
                print("Invalid number of rails")
                
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            try:
                rails = int(input("Enter number of rails: "))
                if rails >= 2:
                    result = rail_fence_decrypt(ciphertext, rails)
                    print(f"Decrypted: {result}")
                else:
                    print("Number of rails must be at least 2")
            except ValueError:
                print("Invalid number of rails")
                
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def columnar_menu():
    """Handle Columnar Cipher operations"""
    print("\n--- COLUMNAR CIPHER ---")
    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Back to Main Menu")
        
        choice = input("\nEnter choice: ").strip()
        
        if choice == '1':
            plaintext = input("Enter plaintext: ")
            key = input("Enter key (alphabetic only): ").strip()
            if key.isalpha():
                result = columnar_encrypt(plaintext, key)
                print(f"Encrypted: {result}")
            else:
                print("Key must contain only alphabetic characters")
                
        elif choice == '2':
            ciphertext = input("Enter ciphertext: ")
            key = input("Enter key: ").strip()
            if key.isalpha():
                result = columnar_decrypt(ciphertext, key)
                print(f"Decrypted: {result}")
            else:
                print("Key must contain only alphabetic characters")
                
        elif choice == '3':
            break
        else:
            print("Invalid choice")

def run_all_demonstrations():
    """Run demonstrations for all cipher algorithms"""
    print("\n" + "=" * 60)
    print("RUNNING ALL CIPHER DEMONSTRATIONS")
    print("=" * 60)
    
    # Caesar Cipher Demo
    print("\n1. CAESAR CIPHER DEMONSTRATION")
    print("-" * 40)
    text = "Hello World"
    shift = 3
    encrypted = caesar_encrypt(text, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    print(f"Original:  {text}")
    print(f"Shift:     {shift}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Vigenère Cipher Demo
    print("\n2. VIGENÈRE CIPHER DEMONSTRATION")
    print("-" * 40)
    text = "INFORMATION SECURITY"
    key = "KEY"
    encrypted = vigenere_encrypt(text, key)
    decrypted = vigenere_decrypt(encrypted, key)
    print(f"Original:  {text}")
    print(f"Key:       {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    # Rail Fence Cipher Demo
    print("\n3. RAIL FENCE CIPHER DEMONSTRATION")
    print("-" * 40)
    text = "CRYPTOGRAPHY"
    rails = 3
    encrypted = rail_fence_encrypt(text, rails)
    decrypted = rail_fence_decrypt(encrypted, rails)
    print(f"Original:  {text}")
    print(f"Rails:     {rails}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    print("Pattern:")
    print(visualize_fence(text, rails))
    
    # Columnar Cipher Demo
    print("\n4. COLUMNAR CIPHER DEMONSTRATION")
    print("-" * 40)
    text = "HELLO WORLD"
    key = "CIPHER"
    encrypted = columnar_encrypt(text, key)
    decrypted = columnar_decrypt(encrypted, key)
    print(f"Original:  {text}")
    print(f"Key:       {key}")
    print(f"Encrypted: {encrypted}")
    print(f"Decrypted: {decrypted}")
    
    print("\n" + "=" * 60)
    print("ALL DEMONSTRATIONS COMPLETED")
    print("=" * 60)

def main():
    """Main program function"""
    try:
        while True:
            display_main_menu()
            choice = input("\nEnter your choice (1-6): ").strip()
            
            if choice == '1':
                caesar_menu()
            elif choice == '2':
                vigenere_menu()
            elif choice == '3':
                rail_fence_menu()
            elif choice == '4':
                columnar_menu()
            elif choice == '5':
                run_all_demonstrations()
            elif choice == '6':
                print("\nThank you for using the Encryption Algorithms Program!")
                print("Program terminated successfully.")
                break
            else:
                print("Invalid choice. Please select 1-6.")
                
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user.")
        print("Exiting gracefully...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Program terminated.")

if __name__ == "__main__":
    main()