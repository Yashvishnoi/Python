def Sum(a,b) :
    """This function gives the sum of 2 number """
    c=a+b
    return c
def Average(a,b):
    """This"""
    c= (a+b)/2
    return c
a=int(input("Enter a value of a: "))
b=int(input("Enter a value of b: "))
d=Sum(a,b)
print("Sum of two number : ",d)
e=Average(a,b)
print ("Average of entered number is : ",e)
print (Sum.__doc__)
