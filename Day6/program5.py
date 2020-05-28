from math import*
def isfibonacci(n):
    x,y=5*n*n+4,5*n*n-4
    p,q=int(sqrt(x)),int(sqrt(y))
    if p*p==x or q*q==y:
        print("YES the sum of the array ",list," which is ",n," is a fibonacci number")
    else:
        print("NO the sum of the array ",list," which is ",n," is not a fibonacci number")
list=[int(x) for x in input("Enter fibonacci series").split()]
add=sum(list)
isfibonacci(add)
