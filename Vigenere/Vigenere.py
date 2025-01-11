def ConvertCharToInt(char):
    if char.islower():
        return ord(char) - ord('a')
    return ord(char) - ord('A')

def ChooseAlphabet(char, num):
    base = ord('a')
    if char.isupper():
        base = ord('A')
    return chr((ConvertCharToInt(char) + num)%26 + base)

def ShiftChar(char, shift, encrypt):
    if char.isalpha():
        shift = ConvertCharToInt(shift) * (1 if encrypt else -1)
        return ChooseAlphabet(char, shift)
    else:
        return char
    
def Vigenere(text, key, encrypt):
    result = ""
    keyIndex = 0
    for i in range(len(text)):
        if keyIndex >= len(key):
            keyIndex = 0
        result += ShiftChar(text[i], key[keyIndex], encrypt)
        if text[i] != ' ':
            keyIndex += 1
    return result

if __name__ == "__main__":
    try:
        text = input("Enter text: ")
        key = input("Enter key: ")
        encrypt = bool(int(input("Encrypt or Decrypt (1/0): ")))
    except ValueError:
        print("Invalid input. Please enter the correct values.")
        exit(1)
    print("Result: "+ Vigenere(text, key, encrypt))