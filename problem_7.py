# class monitor problem
def classmonitor(n,ranks):
    cuts = 0
    current_min = ranks[0]
    for i in range(1,n):
        if ranks[i] < current_min:
            cuts = cuts + 1
            current_min = ranks[i]
    return cuts
n1 = 6
ranks1 = [4, 3, 2, 7, 6, 1]
print(classmonitor(n1, ranks1)) 
