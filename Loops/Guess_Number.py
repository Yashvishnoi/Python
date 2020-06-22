i=1
number=18
while(i<=9) :
    Entered_Number = int(input("Guess the number"))
    if(Entered_Number>number) :
        print("Guessed Number is greater")
    elif(Entered_Number<number) :
        print("Guessed number is lesser")
    else :
        print("Number found",number)
        print("Your attempt is",i)
        break
    i=i+1
if i==10 :
    print("Your attempts are over")
