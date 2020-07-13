num1= input()
num2=input()

try:
    print("The sum of two number is" , int(num1)+int(num2))
except Exception as e:
    print(e)
