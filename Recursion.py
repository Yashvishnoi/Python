# Iterative method to find the factorial
def factorial(n):
    fac= 1
    for i in range (n):
        fac= fac*(i+1)
    return fac

num= int(input("Enter the number "))
print("Factorial using iterative method ",factorial(num))

# Factorial using recursion
def factorial_recursion(n):
    if n==1:
        return 1
    else :
        return n*factorial_recursion(n-1)

print("Factorial using recursion method ",factorial(num))
