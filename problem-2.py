def isArmstrong(n):
    str_n = str(n)
    count_n = len(str_n)
    sum_n = 0
    for each_number in str_n:
        sum_n = sum_n + (int(each_number)**count_n)
    if n == sum_n:
        return True
    else:
        return False    
number = int(input("Enter the number: "))
output = isArmstrong(number)  
print(output)  
