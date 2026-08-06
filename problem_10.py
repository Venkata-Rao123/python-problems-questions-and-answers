def SingleNumber(nums):
    count = 0
    for i in nums:
        count = count ^ i
    return count
list_n = [1,2,3,2,5,1,3]
res = SingleNumber(list_n)
print(res)
