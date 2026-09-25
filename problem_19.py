#list compression problem

'''Let's learn about list comprehensions! You are given three integers x,y,z
representing the dimensions of a cuboid along with an integer n.
print a list all the possible.'''


def cubiod_values(x,y,z,n):
    res = [ [i,j,k]
        for i in range(x+1)
        for j in range(y+1)
        for k in range(z+1)
        if i + j + k != n
        ]
    return res
X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

result = cubiod_values(X,Y,Z,N)
print(result)
