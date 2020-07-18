# Iterative method to find the factorial
def factorial(n):
    fac= 1
    for i in range (n):
        fac= fac*(i+1)
    return fac

num= int(input("Enter the number "))
print("Factorial using iterative mrthod ",factorial(num))
