from itertools import*
from numpy import*

list=[float(x) for x in input("Enter the real number in the array greater than zero").split()]
n=len(list)
newlist=permutations(list,3)
for i in newlist:
        z=sum(i)
        if 1<z<2:
            print(i)
