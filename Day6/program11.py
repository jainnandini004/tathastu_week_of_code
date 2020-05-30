from itertools import*
from numpy import*

list=[float(x) for x in input("Enter the number in the array.").split()]
n=len(list)
a=[]
newlist=permutations(list,3)
for i in newlist:
        a.append(prod(i))
print("Highest product possible by multiplying three number from the list= ",max(a))
