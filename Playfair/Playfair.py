def GenerateKeyMatrix(key):
    key = key.upper().replace("J", "I")
    matrix = []
    used_chars = set()
    
    for char in key:
        if char not in used_chars and char.isalpha():
            matrix.append(char)
            used_chars.add(char)
    
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in used_chars:
            matrix.append(char)
            used_chars.add(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def PreprocessText(text):
    text = text.upper().replace("J", "I")
    processed_text = ""
    
    i = 0
    while i < len(text):
        processed_text += text[i]
        if i + 1 < len(text) and text[i] == text[i + 1]:
            processed_text += 'X'
        elif i + 1 < len(text):
            processed_text += text[i + 1]
            i += 1
        i += 1
    
    if len(processed_text) % 2 != 0:
        processed_text += 'X'
    
    return processed_text

def FindPosition(matrix, char):
    for i, row in enumerate(matrix):
        if char in row:
            return i, row.index(char)
    return None

def PlayfairEncrypt(plaintext, key):
    matrix = GenerateKeyMatrix(key)
    plaintext = PreprocessText(plaintext)
    ciphertext = ""
    
    for i in range(0, len(plaintext), 2):
        row1, col1 = FindPosition(matrix, plaintext[i])
        row2, col2 = FindPosition(matrix, plaintext[i + 1])
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5]
            ciphertext += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1]
            ciphertext += matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    
    return ciphertext

def PlayfairDecrypt(ciphertext, key):
    matrix = GenerateKeyMatrix(key)
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        row1, col1 = FindPosition(matrix, ciphertext[i])
        row2, col2 = FindPosition(matrix, ciphertext[i + 1])
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5]
            plaintext += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1]
            plaintext += matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    
    return plaintext

# Example usage
if __name__ == "__main__":
    try:
        plaintext = input("Enter plaintext: ")
        key = input("Enter key: ")
        choice = int(input("Encrypt or Decrypt (1/0): "))
        if choice not in [0, 1]:
            raise ValueError("Invalid choice. Enter 1 for Encrypt or 0 for Decrypt.")
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    
    if choice == 1:
        ciphertext = PlayfairEncrypt(plaintext, key)
        print(f"Ciphertext: {ciphertext}")
    else:
        ciphertext = input("Enter ciphertext: ")
        decrypted_text = PlayfairDecrypt(ciphertext, key)
        print(f"Decrypted text: {decrypted_text}")