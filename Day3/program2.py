from itertools import permutations
n=input("Enter the string whose permutation u want to find")
l=list(n)
count=0
n=permutations(l)
for i in (n):
    print(i)
    count+=1
print("TOTAL PERMUTATION=",count)
