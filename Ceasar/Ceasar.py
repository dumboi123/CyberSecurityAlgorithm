"""
*Change characters in a string by shifting them by a fixed amount
@param text: string to be encrypted/decrypted, @param key: shift amount, @param encrypt: boolean to encrypt or decrypt
"""
def shiftChar(char, key, encrypt=True):
    if char.isupper():
        base = 65
    elif char.islower():
        base = 97
    else:
        return char
    
    if encrypt:
        return chr((ord(char) + key - base) % 26 + base)
    return chr((ord(char) - key - base) % 26 + base)
"""
*Encrypt or decrypt a string using the Ceasar cipher
@param text: string to be encrypted/decrypted, @param key: shift amount, @param encrypt: boolean to encrypt or decrypt
""" 
def Ceasar(text, key, encrypt=True):
    result = ""
    for i in range(len(text)):
        result += shiftChar(text[i], key, encrypt)
    return result
"""
*Encrypt or decrypt a string using the Ceasar cipher with recursion
@param result: the string to be returned, @param currentCharIndex: the index of the current character, @param text: the text to be encrypted/decrypted, @param key: the shift amount
""" 
def CeaserRecursive(result,currentCharIndex , text, key, encrypt=True):
    if currentCharIndex >= len(text):
        return result
    result += shiftChar(text[currentCharIndex], key, encrypt)
    return CeaserRecursive(result, currentCharIndex+1, text, key,encrypt)

def main():
    try:
        text = input("Enter the text: ")
        key = int(input("Enter the key: "))
        encrypted = bool(int(input("Encrypt or Decrypt? (1/0): ")))
    except ValueError:
        print("Invalid input. Please enter valid text, a numeric key, and 1 or 0 for encryption/decryption.")
        exit(1)

    # print("Result: ", Ceasar(text, key, encrypted))
    print("Recursive Result: ", CeaserRecursive("", 0, text, key, encrypted))

main()