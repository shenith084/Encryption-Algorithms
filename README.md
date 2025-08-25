
## Implementing Encryption Algorithms

### Project Overview
This project implements four classical encryption algorithms in Python:
1. **Caesar Cipher** - Simple substitution cipher with fixed shift
2. **Vigenère Cipher** - Polyalphabetic substitution cipher using a keyword
3. **Rail Fence Cipher** - Transposition cipher using zigzag pattern
4. **Columnar Cipher** - Transposition cipher using column rearrangement

### Files Structure
```
encryption_algorithms/
├── caesar_cipher.py          # Caesar Cipher implementation
├── vigenere_cipher.py        # Vigenère Cipher implementation
├── rail_fence_cipher.py      # Rail Fence Cipher implementation
├── columnar_cipher.py        # Columnar Cipher implementation
├── main_program.py           # Unified interface for all algorithms
```

### How to Run

#### Individual Algorithm Files
Each algorithm can be run independently:
```bash
python caesar_cipher.py
python vigenere_cipher.py
python rail_fence_cipher.py
python columnar_cipher.py
```

#### Main Program (Recommended)
Run the unified interface:
```bash
python main_program.py
```

### Algorithm Descriptions

#### 1. Caesar Cipher
- **Type**: Substitution Cipher
- **Key**: Integer shift value (0-25)
- **Method**: Each letter shifted by fixed number of positions
- **Example**: "HELLO" with shift 3 → "KHOOR"

#### 2. Vigenère Cipher
- **Type**: Polyalphabetic Substitution Cipher
- **Key**: Alphabetic keyword
- **Method**: Each letter shifted by corresponding key letter value
- **Example**: "HELLO" with key "KEY" → "RIJVS"

#### 3. Rail Fence Cipher
- **Type**: Transposition Cipher
- **Key**: Number of rails (rows)
- **Method**: Text written in zigzag pattern, read row by row
- **Example**: "HELLO" with 3 rails → "HOELL"

#### 4. Columnar Cipher
- **Type**: Transposition Cipher
- **Key**: Alphabetic keyword
- **Method**: Text arranged in grid, columns read in alphabetical key order
- **Example**: "HELLO WORLD" with key "KEY" → "ELHLROWOLD"

### Sample Runs

#### Caesar Cipher Sample Run
```
==================================================
CAESAR CIPHER IMPLEMENTATION
==================================================

SAMPLE DEMONSTRATION
==================================================

Sample 1:
Original:   Hello World
Shift:      3
Encrypted:  Khoor Zruog
Decrypted:  Hello World

Sample 2:
Original:   CRYPTOGRAPHY
Shift:      13
Encrypted:  PELCGBTENCUL
Decrypted:  CRYPTOGRAPHY

Select operation:
1. Encrypt
2. Decrypt
3. Exit

Enter your choice (1-3): 1
Enter plaintext to encrypt: Information Security
Enter shift value (0-25): 5

Plaintext:  Information Security
Shift:      5
Ciphertext: Nsknwrfynts Xjhzwnyd
```

#### Vigenère Cipher Sample Run
```
==================================================
VIGENÈRE CIPHER IMPLEMENTATION
==================================================

SAMPLE DEMONSTRATION
==================================================

Sample 1:
Original:   HELLO WORLD
Key:        KEY
Extended:   KEYKEYKEYKE
Encrypted:  RIJVS AIDNP
Decrypted:  HELLO WORLD

Select operation:
1. Encrypt
2. Decrypt
3. Exit

Enter your choice (1-3): 1
Enter plaintext to encrypt: ATTACK AT DAWN
Enter encryption key (alphabetic characters only): LEMON

Plaintext:  ATTACK AT DAWN
Key:        LEMON
Ciphertext: LXFOPV EF RNHR
```

#### Rail Fence Cipher Sample Run
```
==================================================
RAIL FENCE CIPHER IMPLEMENTATION
==================================================

SAMPLE DEMONSTRATION
==================================================

Sample 1:
Original:   HELLO WORLD
Rails:      3
Encrypted:  HOELL WRDLO
Decrypted:  HELLO WORLD
Fence Pattern:
H   O   O   D
 E L   W R L
  L     L

Select operation:
1. Encrypt
2. Decrypt
3. Visualize Fence Pattern
4. Exit

Enter your choice (1-4): 1
Enter plaintext to encrypt: WE ARE DISCOVERED
Enter number of rails (minimum 2): 4

Plaintext:  WE ARE DISCOVERED
Rails:      4
Ciphertext: WECRLTEERDSOEEAUIVD
```

#### Columnar Cipher Sample Run
```
==================================================
COLUMNAR CIPHER IMPLEMENTATION
==================================================

SAMPLE DEMONSTRATION
==================================================

Sample 1:
Original:   HELLO WORLD
Key:        KEY
Column Order: [1, 0, 2]
Encrypted:  ELHLROWOLRX
Decrypted:  HELLOWORLD

Grid Visualization:
Key:     K E Y
Order:   2 1 3
---------
         H E L
         L O W
         O R L
         D X X

Select operation:
1. Encrypt
2. Decrypt
3. Visualize Grid
4. Exit

Enter your choice (1-4): 1
Enter plaintext to encrypt: MEET ME AT MIDNIGHT
Enter encryption key: ZEBRA

Plaintext:  MEET ME AT MIDNIGHT
Key:        ZEBRA
Ciphertext: MMEMTIDNETEATGHIX
