#Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.



#method - 1:

def containsDuplicate(nums):
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                return True
    else:
        return False
li = list(map(int,input("Enter the elements: ").split()))
res = containsDuplicate(li)
print(res)

# Time complexity : O(n*2)




#method - 2:

def containsDuplicates(nums):
    if len(nums) != len(set(nums)):
        return True
    else:
        return False
li = list(map(int,input("Enter the numbers:").split()))
result = containsDuplicates(li)
print(result)

#Time complexity : O(1)





Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

