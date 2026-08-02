def togglebit(n):
    length = n.bit_length()
    mask = (1 << length) - 1
    toggle = ( n ^ mask)
    return toggle
num = int(input("Enter the number: "))
res = togglebit(num)
print(res)
