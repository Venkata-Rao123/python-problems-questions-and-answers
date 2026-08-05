# Binary search
def search(nums,target):
    left = 0
    right = len(nums) -1 # 6 -1 = 5
    while left <= right:# 0<= 5 ->T
        mid = (left + right)//2 # mid = (3 + 4)//2 = 7//2 = 3
        if nums[mid] == target:# nums[2] == 9 = 4 == 9 ->T
            return mid # 2
        elif nums[mid] < target: # nums[3] < 9 = 4 < 9
            left = left + 1 # 2 + 1 =3
        else:
            right = right -1 # 5 -1 = 4
    return -1
numbers = [-1,0,2,4,9,10,12]
tar = 9
res = search(numbers,tar)
print(res)
