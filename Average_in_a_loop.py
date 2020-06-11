count=0
sum=0
print('Before' , count, sum)
for value in [10,70,25,2,96] :
    count=count+1
    sum=sum + value
    print(count,sum,value)
print('After',count,sum,sum/count)
