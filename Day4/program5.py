from array import*
n=[i for i in input("Enter the candidates name").split(",")]
a=array('i',n)
b=array('i',[])
for i in a:
    if i not in b:
        b.append(i)
for i in b:
    print("Occurence of ",i,"=",a.count(i))
