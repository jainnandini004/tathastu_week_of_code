from numpy import*

def spiralform(m,n,arr):
   # k=starting row index
   #  m=ending row index
   # l=starting column index
   # n=ending column index
   k,l=0,0
   while(k<m and l<n):
       for i in range(l,n):
           print(arr[k][i],end=" ")
       k+=1
       for i in range(k,m):
           print(arr[i][n-1],end=" ")
       n-=1
       if k<m:
           for i in range(n-1,l-1,-1):
               print(arr[m-1][i],end=" ")
           m-=1
       if l<n:
           for i in range(m-1,k-1,-1):
               print(arr[i][l],end=" ")
           l+=1

m=int(input("Enter the number of rows u want to enter"))
n=int(input("Enter the number of columns u want to enter"))
arr=array([int(x) for x in input("Enter the elements in matrix").split()])
z=arr.reshape(m,n)
print("GIVEN MATRIX")
print(z)
spiralform(m,n,z)
