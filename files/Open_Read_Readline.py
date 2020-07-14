f= open("harry.txt","rt") # read file in text mode by default
content = f.read()
print(content)
f.close

# read file in bnary mode
f= open("harry.txt","rb")
content = f.read()
print(content)
f.close

# f.read(3) it will read 3 characters
f= open("harry.txt","rt")
content = f.read(3)
print(content)
f.close
