list=[int(x) for x in input("Enter number in the list which contained only 1's and 0's").split()]
zeroes=list.count(0)
total=len(list)
a=[]
for i in range(zeroes):
    a.append(0)
for i in range(zeroes,total):
    a.append(1)
print("Old list=",list)
print("New list=",a)
