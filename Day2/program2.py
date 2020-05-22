n=int(input("enter the number of elements u want to see in the fibonacci series"))
def fib(n):
	if(n<0):
		print('enter positive number')
	elif n==1:
		print("0")
	else:	
		a,b=0,1
		print(a)
		print(b)
		for i in range(3,n+1):
			c=a+b
			a=b
			b=c
			print(c,end="")
