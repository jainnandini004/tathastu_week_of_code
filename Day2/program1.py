def odd_even(n):
    if n%2==0:
        print(n," is an EVEN number")
    else:
        print(n," is an ODD number")

def prime(n):
    if n>0:
        for i in range(2,n):
            if n%i==0:
                print(n," is NOT a PRIME NUMBER")
                break
        else:
            print(n," is a PRIME NUMBER")
    else:
        print("Enter positive number")
def palindrome(n):
    x=str(n)
    y=str(n)[::-1]
    if x==y:
        print(n," is a palindrome number")
    else:
        print(n," is not a palindrome number")

def armstrong(n):
    sum=0
    temp=n
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp=temp//10
    if sum==n:
        print(n," is ARMSTRONG number")
    else:
        print(n," is NOT an ARMSTRONG number")

num=int(input("Enter the number which you want to check whether the input number is odd/even,prime,palindrome,armstrong "))
odd_even(num)
prime(num)
palindrome(num)
armstrong(num)
