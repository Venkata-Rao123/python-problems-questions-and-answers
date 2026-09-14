# first largest number find
'''def arr(n):
    first = n[0]
    for i in n:
        if (i > first):
            first = i
    return first
li = [12,45,34,67,10,23,78]
res = arr(li)
print(res)'''

# largest number find
def arr(n):
    first = -float()
    second = -float()
    for i in n:
        if (i>first):
            second = first
            first = i
        if (i>second and i<first):
            second = i
    return second
li = [12,45,34,67,10,23,78]
res = arr(li)
print(res)
