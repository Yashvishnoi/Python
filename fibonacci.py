def fibonacci(n):
    a=1 ,b =2
    if n==1:
        return 0
    elif n==2 :
        return 1
    else :
         return fibonacci(n-1) + fibonacci(n-2)
