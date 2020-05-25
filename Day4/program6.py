dic=[x for x in input("Enter words in dictionary=").split()]
char=[x for x in input("Enter character in array=").split()]
for i in dic:
    z=list(i)
    for j in z:
        if j not in char:
            dic.remove(i)
print(dic)

