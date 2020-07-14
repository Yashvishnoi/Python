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
