#include <iostream>
#include <vector>
#include <string>
using namespace std;

string Vigenere(string text, string key, bool encrypt);
int main()
{
    string text, key;
    bool encrypt;
    try
    {
        cout << "Enter text: ";
        getline(cin, text);
        cout << "Enter key: ";
        getline(cin, key);
        cout << "Encrypt or Decrypt? (1/0): ";
        cin >> encrypt;
        if (cin.fail())
        {
            throw invalid_argument("Invalid input for encryption choice.");
        }
        cout << "Result: " << Vigenere(text, key, encrypt) << endl;
    }
    catch (const exception &e)
    {
        cerr << "Error: " << e.what() << endl;
    }
    return 0;
}

vector<int> ConvertStringToInt(string str)
{
    vector<int> result;
    for (int i = 0; i < str.size(); i++)
    {
        if (isupper(str[i]))
        {
            result.push_back(str[i] - 'A');
        }
        else if (islower(str[i]))
        {
            result.push_back(str[i] - 'a');
        }
        else
            result.push_back(str[i]);
    }
    return result;
}

char ShiftChar(char c, int shift)
{
    if (shift < 0)
        shift += 26;
    if (isupper(c))
    {
        return (c - 'A' + shift) % 26 + 'A';
    }
    else if (islower(c))
    {
        return (c - 'a' + shift) % 26 + 'a';
    }
    return c;
}
string Vigenere(string text, string key, bool encrypt = true)
{
    vector<int> keyInt = ConvertStringToInt(key);
    string result = "";
    int keyIndex = 0;
    for (int i = 0; i < text.size(); i++)
    {
        if (keyIndex >= key.size())
            keyIndex = 0;
        result += ShiftChar(text[i], keyInt[keyIndex] * (encrypt ? 1 : -1));
        if (text[i] != ' ')
            keyIndex++;
    }
    return result;
}