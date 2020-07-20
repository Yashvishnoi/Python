me = "Yash"
a1 = 3
# a= "This is %s %s "%(me, a1)
a= "This is {1} {0} "
b=a.format(me,a1)
print(b)
