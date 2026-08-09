def isvalidparathesis(n):
    st = []
    for ch in n:
        if ch in "([{":
            st.append(ch)
        else:
            if st and ((st[-1] == '(' and ch == ')') or
                       (st[-1] == '[' and ch == ']') or
                       (st[-1] == '{' and ch == '}')):
                st.pop()
            else:
                return False
    return not st

brackets = input("Enter the brackets: ")
res = isvalidparathesis(brackets)
print(res)
