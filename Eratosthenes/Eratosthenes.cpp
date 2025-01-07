#include<iostream>
#include<vector>
using namespace std;

vector<int> eratosthenes(int n);
int main()
{
    int n;
    cout<<"Enter the number upto which you want to find the prime numbers: ";
    cin>>n;
    vector<int> primes = eratosthenes(n);
    cout<<"The prime numbers upto "<<n<<" are: ";
    for(int prime : primes) {
        cout << prime << " ";
    }
    cout << endl;
    return 0;
}

vector<int> eratosthenes(int n){
    vector<bool> primeNumbers(n+1, true);
    vector<int> primeNumbersList;
    int currentPrimeNumber = 2;
    while (currentPrimeNumber*currentPrimeNumber <= n){
        if (primeNumbers[currentPrimeNumber]){
            for(int i = currentPrimeNumber*currentPrimeNumber; i <= n; i+= currentPrimeNumber)
                primeNumbers[i] = false;
        }
        currentPrimeNumber++;
    }
    for(int i = 2; i <= n; i++){
        if (primeNumbers[i])
            primeNumbersList.push_back(i);
    }
    return primeNumbersList;
}