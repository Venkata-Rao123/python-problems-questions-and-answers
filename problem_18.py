# runner_up of score

'''Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner'''

def runner_up_score(arr):
    second = list(set(arr))
    second.sort(reverse=True)
    return second[1]
    
array = list(map(int,input().split()))
result = runner_up_score(array)
print(result)




'''Sample Input:

2 3 6 6 5

Sample Output:
5'''
