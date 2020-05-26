def evenodd(list):
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    return sorted(odd,reverse=True)+sorted(even)
list = [int(x) for x in input("Enter number in the list").split()]
even=[]
odd=[]
print("The list after sort even number in ascending order and all odd number in descending order ",(evenodd(list)))
