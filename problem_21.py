#Remove duplicates from a list in Python ?

def removeduplicates(rd):
    unique = []
    for i in range(len(n)):
        found = False
        for j in range(len(unique)):
            if n[i] == unique[j]:
                found = True
                break
        if found == False:
            unique.append(n[i])
    return unique

n = [1,2,1,2,3,5,6]
res = removeduplicates(n)
print(res)
