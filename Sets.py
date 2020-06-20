s =set()
print(type(s))
s_from_list=set([1,2,5,8,7,9,10])
print(s_from_list)
s_from_list.add(58) # It will add 58 to the set
print(s_from_list)
s1= s_from_list.union({1,25,6}) # it will print the union set
print(s_from_list,s1)
s2 = s_from_list.intersection({1,2,748}) # it will print the comman numbeer from both the set
print(s2)
