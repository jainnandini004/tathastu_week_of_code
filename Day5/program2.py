def replaced(list):
    for i in range(size-1):
        list[i]=max(list[i+1:])
    return list
size=int(input("Enter the size of list"))
list=[int(x) for x in input("Enter elements=").split(",")]
print("Converted list=",replaced(list))
