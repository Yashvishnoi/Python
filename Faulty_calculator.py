# Design a calculator which will solve all the problems correctly except.
# 45*3=555 , 56+9=77 , 56/6 = 4
# Your program should take a input 2 number and return a correct result.

n1 = int(input("Enter first number "))
n2 = int(input("Enter second number "))
if n1 == 45 :
    if n2== 3:
        print("Multiplication : ","555")
    else:
        print("Multiplication : ",n2*n1)
else :
    print("Multiplication : ",n1*n2)

if n1 == 56 :
    if n2==9 :
        print("Addititon : ","77")
    else :
        print("Addititon : ",n1+n2)
else :
    print("Addititon : ",n1+n2)

if n1 == 56 :
    if n2==6 :
        print("Divison : ","4")
    else :
        print("Divison : ",n1/n2)
else :
    print("Divison : ",n1/n2)
