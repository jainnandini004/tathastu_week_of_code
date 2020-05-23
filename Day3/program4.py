def duplicatelist(n):
    dup=[]
    for i in n:
        if i not in dup:
            dup.append(i)
    print("AFTER =",dup)

n=[int(i)for i in input("Enter list").split()]
print("BEFORE =",n)
duplicatelist(n)
