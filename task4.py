def F(n):
    if n == 0: return 1
    if n == 1: return 1
    if n == 2: return 2
    if n>=3:
        return F(n-1)+F(n-2)+F(n-3)

print(F(int(input("сколько ступенек?"))))