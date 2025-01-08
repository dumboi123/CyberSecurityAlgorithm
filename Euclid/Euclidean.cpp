#include<iostream>
using namespace std;

int Euclidean(int a, int b);
int main()
{
    int a, b;
    cout<<"Enter two numbers: "<<endl;
    cout<<"a = ";
    cin>>a;
    cout<<"b = ";
    cin>>b;
    cout<<"GCD of "<<a<<" and "<<b<<" is "<<Euclidean(a, b)<<endl;
}
//Recursive function to find the GCD of two numbers
int EuclideanRecursion(int a, int b)
{
    if(b==0) return a;
    return Euclidean(b, a%b);
}
//Iterative function to find the GCD of two numbers
int Euclidean(int a, int b)
{
    while(b!=0)
    {
        int temp = b;
        b = a%b;
        a = temp;
    }
    return a;
}
