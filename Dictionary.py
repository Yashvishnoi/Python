d1 = {}
print(type(d1))
d2= {"Harry":"Fish","Yash":"Murga", "Piyush":"Mayo patty", "Himanshu":{"B":"Egg","L":"Dal","D":"Roti"}}
print(d2)
print(d2["Piyush"]) # it will show the Mayo patty
print(d2["Himanshu"]) # it will print {"B":"Egg","L":"Dal","D":"Roti"}
print(d2["Himanshu"]["B"]) # it will print Egg
d2["Aurangzeb"]="Kabab" # it will add Aurangzeb in dictionary
print(d2)
d2[420]="Hey"# it will also add
print(d2)
del d2[420] # it will delete 420
print(d2)
d3=d2 # it will copy the element to d2 with some connection always enabled in it
del d2 ["Harry"]
print(d3) # isme bhi harry delete ho jayega kyoki ye usko hi refer kar raha hai
d3 = d2.copy() # it creates a independent copy
del d2 ["Piyush"]
print(d3 ) # an dictionary se Piyush delete nhi hoga
print(d2.get("Yash")) # it will give the value at harry
d2.update({"Leena":"Toffee"})
print(d2)
print(d2.keys()) # it will print the key of all the element
