# For Loops
list1 = ["Harry", "Carry", "Nikhil", "Flying Beast","Mortal"]
for item in list1 : # it will print all items in list
    print(item)
list1 = (["Harry",745], ["Carry",78], ["Nikhil",5], ["Flying Beast",8],["Mortal",4])
for item in list1 : # it will print both thing as one
    print(item)
list1 = (["Harry",745], ["Carry",78], ["Nikhil",5], ["Flying Beast",8],["Mortal",4])
for item,toffee in list1 : # it will print both object as different because both are reffered by different varia
    print(item," And they eat no. of toffee : ",toffee)
