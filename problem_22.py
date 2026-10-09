#Sort a list in ascending and descending order ?
n = [1,4,5,2,3]
for i in range(len(n)):
    for j in range(len(n)-1):
        if n[j] > n[j+1]:
            temp = n[j]
            n[j] = n[j+1] 
            n[j+1] = temp
print(n)
