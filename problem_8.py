def fizzbuzz(n):
    result = []
    for i in n:
        if i % 3 == 0 and i % 5 == 0:
            result.append("Fizzbuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(i)
    return result
arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
res = fizzbuzz(arr)
print(res)
