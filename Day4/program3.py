a={}
n=int(input("Enter the number of items you want to enter in dictionary"))
for i in range(n):
    k=input("Enter key=")
    v=input("Enter value=")
    a.update({k:v})
print("Dictionary= ",a)
print("Second maximum value in the dictionary is ",list(sorted(a.values()))[-2])
