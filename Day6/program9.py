def kth_term(arr, k):
    a=[]
    for i in range(k):
        a.append(arr[i])
    print("kth smallest element in the given list=",min(a))    
arr=[int(x) for x in input("Enter the list= ").split()]
k=int(input("Enter a number smaller than the size of list"))
kth_term(arr, k)
