from numpy import*
list=array([int(x) for x in input("Enter the number in square matrix of 3*3 order").split()])
z=list.reshape(3,3)
print("ANTICLOCKWISE")
print(rot90(z,axes=(0,1)))
print("CLOCKWISE")
print(rot90(z,axes=(1,0)))
