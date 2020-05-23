n=[int(i)for i in input("Enter the first list").split()]
m=[int(i)for i in input("Enter the second list").split()]
n1=set(n)
m1=set(m)
print("Intersection of above two list is:",list(n1.intersection(m1)))
