# isautomorphic number or not
def isautomorphic(n):
    square = n**n
    str_n = str(n)
    str_square = str(square)
    for i in range(1,len(str_n)+1):
        if str_n[-i] != str_square[-i]:
            return False
    return True     
number = int(input("Enter the number: "))
result = isautomorphic(number)
print(result)
