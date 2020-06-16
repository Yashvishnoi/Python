# Read two integers from STDIN and print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# ===========================================================================

if __name__ == '__main__':
 Value1 = input('')
 a=int(Value1)
 Value2 = input('')
 b=int(Value2)
Sum=a+b
print(Sum)
diff=a-b
print(diff)
Mul=a*b
print(Mul)
