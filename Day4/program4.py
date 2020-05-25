a={}
n=int(input("Enter the number of items u want to enter"))
for i in range(n):
    k=input("Enter key= ")
    v=int(input("Enter value= "))
    a.update({k:v})
print("Before removing duplicate value dictionary is= ",a)
reslist={}
for key,value in a.items():
    if value not in reslist.values():
        reslist[key]=value
print("After remove duplicates value the dictionary will be= ",reslist)
