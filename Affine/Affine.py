def findInverse (a, collection):
    for i in range(1, collection):
        if (a * i) % collection == 1:
            return i
    return None

def ShiftCharEncript(a, b, char, baseChar):
    numberChar = ord(char) 
    numberResult = (a * (numberChar - ord(baseChar)) + b) %26 + ord(baseChar)
    return chr(((a * (ord(char) - ord(baseChar)) + b) % 26) + ord(baseChar))

def ShiftCharDecript(a, b, char, baseChar):
    return chr(((a * ((ord(char) - ord(baseChar) + b))) % 26) + ord(baseChar))

def EncriptAffine (a, b, text):
    result = ""
    for char in text:
        if char.isupper():
            result += ShiftCharEncript(a, b, char, 'A')
        elif char.islower():
            result += ShiftCharEncript(a, b, char, 'a')
        else:
            result += char
    return result

def DecriptAffine (a, b, text):
    result = ""
    aInverse = findInverse(a, 26)
    for char in text:
        if char.isupper():
            result += ShiftCharDecript(aInverse, -b, char, 'A')
        elif char.islower():
            result += ShiftCharDecript(aInverse, -b, char, 'a')
        else:
            result += char
    return result

def AffineCipher(a, b, text, encrypt):
    if encrypt:
        return EncriptAffine(a, b, text)
    else:
        return DecriptAffine(a, b, text)
        
if __name__ == "__main__":

    try:
        text = input("Enter text: ")
        a = int(input("Enter a: "))
        if findInverse(a, 26) is None:
            raise ValueError("a and 26 must be coprime")
        b = int(input("Enter b: "))
    except ValueError as e:
        print(e)
        exit(1)

    encrypt = bool(input("Encrypt or Decrypt? (1/0): "))
    
    print("Result: " + AffineCipher(a, b, text, encrypt))