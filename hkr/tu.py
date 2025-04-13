#i < n, print i^2
#The provided code stub reads an integer, n, from STDIN. For all non-negative integers
#Example :n = 3
#The list of non-negative integers that are less than n = 3 is (0, 1, 2). Print the square of each number on a separate
n = int(input())
for i in range(0,n) :
    print(i*i)