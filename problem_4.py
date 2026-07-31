# sum of given number
def sumofdigits(n):
    sum_n = 0
    while n>0:
        last_digit = n % 10
        sum_n = sum_n + last_digit
        n = n// 10
    return sum_n
number = int(input("Enter the number: "))
output = sumofdigits(number)
print(output)
