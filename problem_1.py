# check the given number is palindrome or not
def ispalindrome(n):
    original_n = n
    reversed_n = 0
    while n > 0:
        digit = n % 10
        reversed_n = reversed_n * 10 + digit
        n = n // 10
    if original_n == reversed_n:
        return True
    else:
        return False    

number = int(input("Enter the number: "))
output = ispalindrome(number)
print(output)
