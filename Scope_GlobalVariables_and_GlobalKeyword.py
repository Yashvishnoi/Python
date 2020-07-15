l =10; # Global
def function1(n):
    #l=5
    m=8
#    print("Here inside the block the value of l is ",l)
#    print(n,"I have printed")
    global l
    l=l+14
    print("This is global l",l)

function1("This is me")
print("Here outside the block the value of l is ",l)
