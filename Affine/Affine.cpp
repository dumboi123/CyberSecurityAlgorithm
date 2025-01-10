#include <iostream>
#include <string>
#include <algorithm>
#include <stdexcept>

using namespace std;

class AffineCipher {
public:
    AffineCipher(int a, int b) : a(a), b(b) {
        // Ensure 'a' and 26 are coprime
        if (gcd(a, 26) != 1) {
            throw invalid_argument("'a' must be coprime with 26.");
        }
    }

    int gcd(int a, int b) {
        while (b != 0) {
            int t = b;
            b = a % b;
            a = t;
        }
        return a;
    }

    string encrypt(const string& plaintext) {
        string ciphertext;
        for (char c : plaintext) {
            if (isalpha(c)) {
                char base = isupper(c) ? 'A' : 'a';
                c = (a * (c - base) + b) % 26 + base;
            }
            ciphertext += c;
        }
        return ciphertext;
    }

    string decrypt(const string& ciphertext) {
        string plaintext;
        int a_inv = modInverse(a, 26);
        for (char c : ciphertext) {
            if (isalpha(c)) {
                char base = isupper(c) ? 'A' : 'a';
                c = (a_inv * ((c - base) - b + 26)) % 26 + base;
            }
            plaintext += c;
        }
        return plaintext;
    }

private:
    int a, b;

    int modInverse(int a, int m) {
        a = a % m;
        for (int x = 1; x < m; x++) {
            if ((a * x) % m == 1) {
                return x;
            }
        }
        throw invalid_argument("No modular inverse found.");
    }
};

int main() {
    try {
        AffineCipher cipher(5, 8); // Example with a=5, b=8
        string plaintext = "HELLO";
        string encrypted = cipher.encrypt(plaintext);
        string decrypted = cipher.decrypt(encrypted);

        cout << "Plaintext: " << plaintext << endl;
        cout << "Encrypted: " << encrypted << endl;
        cout << "Decrypted: " << decrypted << endl;
    } catch (const invalid_argument& e) {
        cerr << e.what() << endl;
    }

    return 0;
}