n=int(input("Enter the value"))
a=n+2
for i in range(n):
    print(" "*i+"*"+" "*a+"*")
    a-=2
a+=2
for i in range(n):
    print(" "*(n-i-1)+"*"+" "*a+"*")
    a+=2
