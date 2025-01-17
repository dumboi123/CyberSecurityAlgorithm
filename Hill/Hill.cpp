#include <iostream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int>> GetKeyMatrix(const string& key, int size) {
    vector<vector<int>> keyMatrix(size, vector<int>(size));
    int k = 0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            keyMatrix[i][j] = (key[k]) % 65;
            k++;
        }
    }
    return keyMatrix;
}

vector<int> GetMessageVector(const string& message, int size) {
    vector<int> messageVector(size);
    for (int i = 0; i < size; i++) {
        messageVector[i] = (message[i]) % 65;
    }
    return messageVector;
}

string EncryptMessage(const string& message, const vector<vector<int>>& keyMatrix, int size) {
    vector<int> messageVector = GetMessageVector(message, size);
    vector<int> cipherVector(size);

    for (int i = 0; i < size; i++) {
        cipherVector[i] = 0;
        for (int j = 0; j < size; j++) {
            cipherVector[i] += keyMatrix[i][j] * messageVector[j];
        }
        cipherVector[i] = cipherVector[i] % 26;
    }

    string cipherText;
    for (int i = 0; i < size; i++) {
        cipherText += cipherVector[i] + 65;
    }

    return cipherText;
}

int main() {
    string message, key;
    cout << "Enter the message: ";
    cin >> message;
    cout << "Enter the key: ";
    cin >> key;

    if (message.length() != 3 || key.length() != 9) {
        cerr << "Error: Message must be 3 characters long and key must be 9 characters long." << endl;
        return 1;
    }

    int size = 3; // Assuming a 3x3 key matrix for simplicity

    vector<vector<int>> keyMatrix = GetKeyMatrix(key, size);
    string cipherText = EncryptMessage(message, keyMatrix, size);

    cout << "Encrypted Message: " << cipherText << endl;

    return 0;
}