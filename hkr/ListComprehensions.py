#Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along with an integer n.
#Print a list of all possible coordinates given by (i, j,k) on a 3D grid where the sum of i + i + k is not equal to n. Here, 0 < i < x; 0 < j< y; 0 < k ≤ z. 
#Please use list comprehensions rather than multiple loops, as a learning exercise.
x = int(input())
y = int(input())
z = int(input())
n = int(input())
ketqua = [[i,j,k] for i in range(0,x+1) for j in range(0,y+1) for k in range(0,z+1) if i+j+k!=n]
print(ketqua)

