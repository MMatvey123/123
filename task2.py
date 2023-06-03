task = [
    ['3','2','6'],
    ['2','7'],
]
b=0
a = input("введите что ищите")
for i in range(len(task)):
    for j in range(len(task[i])):
        print("i found: ",task[i][j])
        if task[i][j]==a:
            print("i got that")
            b=1
            break
    if b==1:
        break
if b==0:
    print("i have no idea where is that")