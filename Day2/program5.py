n=int(input("Enter the value="))
for i in range(n):
    print((str(n-i)+"*")*(n-i-1)+str(n-i))
for i in range(n):
    print(str(i+1)+("*"+str(i+1))*i)
