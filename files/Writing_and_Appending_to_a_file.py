f=open("harry2.txt","w")
f.write("Harry bhai is villan for coding. ")
f.close()

f=open("harry2.txt","a")
f.write(" He loves coding and finding errors in his own program .")
f.close()

f=open("harry2.txt","r")
content= f.read()
print(content)
f.close()

# To print number of characters you write
f=open("harry2.txt","a")
a= f.write(" He loves coding and finding errors in his own program .")
print(a)
f.close()


# To read and write to a file simuntaneously

f=open("harry2.txt","r+")
print(f.read())
f.write("Thank you")
f.close()
