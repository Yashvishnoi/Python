import random

# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
random_number = random.randint(0,1)
print(random_number)

# Return the next random floating point number in the range [0.0, 1.0)
rand=random.random()*100
print(rand)

# # Single random element from a sequence
Ist = ["Star Plus","DD1" , "Aaj Tak","CodeWithHarry"]
choice = random.choice(Ist)
print(choice)
