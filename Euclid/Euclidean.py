def Euclidean(a,b):
# This function calculates the GCD of two numbers using Euclidean Algorithm
# The algorithm works by repeatedly taking the remainder of the division of two numbers
# until the remainder is zero. The divisor at this point is the GCD.
    temp = 0
    while b:
        a,b = b,a%b
    return a

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print ("The GCD of",a,"and",b,"is ",Euclidean(a,b))

