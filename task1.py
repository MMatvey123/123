game = [
    ["x","x","x"],
    ["0","x",""],
    ["0","",""]
]

if game[0][0]==game[1][1] and game[0][0]== game[2][2]:#\ здесь проверка диагонали из верху правого к низу левому
    print(game[0][0], "- win")

elif game[0][2]==game[1][1] and game[0][2]== game[2][0]:#/ здесь от низу левого до верху правого
    print(game[0][2], "- win")

for i in range(3): #здесь проверка по строкам
    if game[i][0] == game[i][1] and game[i][2]==game[i][0]:
        print(game[i][0],"- win")
        break
'''
for i in range(3):
    for j in range(3):
        print(game[j][i],"next")
        '''
for i in range(3): #здесь проверка по столбчикам
    if game[0][i]==game[1][i] and game[0][i]==game[2][i]:
        print(game[2][i],"- win")
        break