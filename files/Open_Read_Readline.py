print("It will file in text mode\n")
f= open("harry.txt","rt") # read file in text mode by default
content = f.read()
print(content)
f.close

print("It will print line in text mode\n")
# read file in bnary mode
f= open("harry.txt","rb")
content = f.read()
print(content)
f.close

print("It will print the number of entered characters\n")
# f.read(3) it will read 3 characters
f= open("harry.txt","rt")
content = f.read(3)
print(content)
f.close

print("It will print line by line\n")
# print(f.readline()) it will print line by read line
f= open("harry.txt","rt")
print(f.readline())
f.close
