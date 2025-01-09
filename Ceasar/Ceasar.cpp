#include <iostream>
using namespace std;

void Annotation(string text, int key, bool encrypt);
int main()
{
    string text;
    int key;
    bool encrypt;
    Annotation(text, key, encrypt);
    return 0;
}
// * Function to shift a character by key value
char shiftChar(char inputChar, char conditionChar, int key, bool encrypt = true)
{
    if (encrypt)
        inputChar = (inputChar - conditionChar + key) % 26 + conditionChar;
    else
        inputChar = (inputChar - conditionChar - key + 26) % 26 + conditionChar;
    return inputChar;
}
// * Function to shift a string by key value
string shiftString(string text, int key, bool encrypt = true)
{
    string result = "";
    for (int i = 0; i < text.length(); i++)
    {
        if (isupper(text[i]))

            result += shiftChar(text[i], 'A', key, encrypt);

        else if (islower(text[i]))

            result += shiftChar(text[i], 'a', key, encrypt);

        else

            result += text[i];
    }
    return result;
}

string Ceasar(string text, int key, bool encrypt = true)
{
    return shiftString(text, key, encrypt);
}
// * Function to take input from user and give output
void Annotation(string text, int key, bool encrypt)
{
    try
    {
        cout << "Enter the text to be encrypted: ";
        getline(cin, text);
        cout << "Enter the key value: ";
        cin >> key;
        if (cin.fail())
        {
            throw invalid_argument("Invalid key value. Please enter an integer.");
        }
        cout << "Encrypt or Decrypt? (1/0): ";
        cin >> encrypt;
        if (cin.fail())
        {
            throw invalid_argument("Invalid choice for encrypt/decrypt. Please enter 1 or 0.");
        }
    }
    catch (const invalid_argument &e)
    {
        cerr << "Error: " << e.what() << endl;
        exit(1);
    }
    cout << "The result text is: " << Ceasar(text, key, encrypt) << endl;
}
