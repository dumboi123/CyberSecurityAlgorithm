import numpy as np

def createMatrixFromKey(key, size):
    key_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(ord(key[i * size + j]) % 65)
        key_matrix.append(row)
    return np.array(key_matrix)

def encryptMessage(message, key_matrix, size):
    message_vector = []
    for i in range(size):
        message_vector.append(ord(message[i]) % 65)
    message_vector = np.array(message_vector)
    
    cipher_matrix = np.dot(key_matrix, message_vector) % 26
    cipher_text = ''.join(chr(int(cipher_matrix[i]) + 65) for i in range(size))
    
    return cipher_text

def hillCipherEncrypt(message, key):
    size = int(len(key) ** 0.5)
    key_matrix = createMatrixFromKey(key, size)
    
    message = message.upper().replace(" ", "")
    if len(message) % size != 0:
        message += 'X' * (size - len(message) % size)
    
    cipher_text = ''
    for i in range(0, len(message), size):
        cipher_text += encryptMessage(message[i:i+size], key_matrix, size)
    
    return cipher_text

# Example usage
try:
    message = input("Enter the message: ").upper().replace(" ", "")
    key = input("Enter the key: ").upper().replace(" ", "")
    if len(key) ** 0.5 != int(len(key) ** 0.5):
        raise ValueError("Key length must be a perfect square.")
except Exception as e:
    print(f"Error: {e}")
    exit(1)
encrypted_message = hillCipherEncrypt(message, key)
print(f"Encrypted Message: {encrypted_message}")