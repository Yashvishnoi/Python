# Make a list which contain all the thing like number, string etc.
# Now detect wheather it is number or not and it should be greater than 6 then print it.
 # =======================================================================

list = ["harry" , 1 ,78 , "Hey" , 'A' , 85 , 74 , 2 , 20 , 8, 5]
for item in list:
    if str(item).isnumeric() and item>=6:
        print(item)
