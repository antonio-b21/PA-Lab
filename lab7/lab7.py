# # problema 1
# def paths(currentIndex):
#     if len(lastFor[currentIndex]) == 0:
#         global pathsNo
#         pathsNo += 1
#     else:
#         for index in lastFor[currentIndex]:
#             paths(index)
#
# with open("domino.txt") as file:
#     dominosNo = int(file.readline())
#     dominos = [tuple([int(x) for x in file.readline().split()]) for i in range(dominosNo)]
#
# lenghtAt = [1] * dominosNo
# lenghtAtRev = [1] * dominosNo
# # lastFor = [[] for i in range(dominosNo)]        # pentru
# # lastForRev = [[] for i in range(dominosNo)]     # oglindire
# for currentIndex, currentDomino in enumerate(dominos):
#     for index, domino in enumerate(dominos[:currentIndex]):
#         if currentDomino[0] == domino[1] and lenghtAt[index]+1 >= lenghtAt[currentIndex]:
#             if lenghtAt[index]+1 == lenghtAt[currentIndex]:
#                 lastFor[currentIndex].append(index)
#             else:
#                 lastFor[currentIndex] = [index]
#             lenghtAt[currentIndex] = lenghtAt[index] + 1
#     # ########### pentru oglindire
#     #     if currentDomino[0] == domino[0] and lenghtAtRev[index] + 1 >= lenghtAt[currentIndex]:
#     #         if lenghtAtRev[index]+1 == lenghtAt[currentIndex]:
#     #             lastFor[currentIndex].append(-1*index)
#     #         else:
#     #             lastFor[currentIndex] = [-1*index]
#     #         lenghtAt[currentIndex] = lenghtAtRev[index] + 1
#     #     if currentDomino[1] == domino[1] and lenghtAt[index]+1 >= lenghtAtRev[currentIndex]:
#     #         if lenghtAt[index]+1 == lenghtAtRev[currentIndex]:
#     #             lastForRev[currentIndex].append(index)
#     #         else:
#     #             lastForRev[currentIndex] = [index]
#     #         lenghtAtRev[currentIndex] = lenghtAt[index] + 1
#     #     if currentDomino[1] == domino[0] and lenghtAtRev[index] + 1 >= lenghtAtRev[currentIndex]:
#     #         if lenghtAtRev[index]+1 == lenghtAtRev[currentIndex]:
#     #             lastForRev[currentIndex].append(-1*index)
#     #         else:
#     #             lastForRev[currentIndex] = [-1*index]
#     #         lenghtAtRev[currentIndex] = lenghtAtRev[index] + 1
#     # ######## pentru oglindire
#
# pathsNo = 0
# maxLength = max(lenghtAt)
# index = lenghtAt.index(maxLength)
# path = []
# while(len(lastFor[index]) != 0):
#     path.append(dominos[index])
#     index = lastFor[index][0]
# path.append(dominos[index])
# path.reverse()
# print(path)
# ##### in cazul oglindirii, indexarea de la 0 produce confuzie intre piesa 0 si piesa 0 oglindita
# #numarul de subsiruri posibile
# for index in range(dominosNo-1, -1, -1):
#     if lenghtAt[index] == maxLength:
#         paths(index)
# print(pathsNo, maxLength)
#
#
# print()
# print("   "+"      ".join([str(x) for x in range(dominosNo)]))
# print(*dominos)
# print("   "+"      ".join([str(x) for  x in lenghtAt]))
# print("  "+"     ".join([str(x) for  x in lastFor]))
# # print("    "+"      ".join([str(x) for  x in lenghtAtRev]))       # pentru
# # print("   "+"     ".join([str(x) for  x in lastForRev]))          # oglindire

# # problema 2
# with open("sah.txt") as file:
#     n, m = [int(x) for x in file.readline().split()]
#     table = [[0, 0, 0, 0]]
#     for i in range(n):
#         line = [0]
#         line.extend([int(x) for x in file.readline().split()])
#         table.append(line)
# cost = [[0] * (m+1) for i in range(n+1)]
# cost[n][m] = table[n][m]
# for line in range(n-1, 0, -1):
#     cost[line][m] = cost[line+1][m] + table[line][m]
# for row in range(m-1, 0, -1):
#     cost[n][row] = cost[n][row+1] + table[n][row]
# for line in range(n-1, 0, -1):
#     for row in range(m-1, 0, -1):
#         if cost[line][row+1] >= cost[line+1][row]:
#             cost[line][row] = cost[line][row+1] + table[line][row]
#         else:
#             cost[line][row] = cost[line+1][row] + table[line][row]
# ##
# for i in range(len(table)):
#     print(table[i],"\t", cost[i])
# ##
# print(cost[1][1])
# line = 1
# row = 1
# while(line < n and row < m):
#     print(line, row)
#     if cost[line+1][row] >= cost[line][row+1]:
#         line += 1
#     else:
#         row += 1
# while(line < n):
#     print(line, row)
#     line += 1
# while(row < m):
#     print(line, row)
#     row += 1
# print(line, row)

# # problema 3
# sum = 14
# coins = [5, 3, 2]
# partSums = [i for i in range(sum+1)]
# coinsNo = [-1] * 15
# lastCoin = [-1] * 15
# coinsNo[0] = 0
# lastCoin[0] = 0
# for coin in coins:
#     for index in range(sum):
#         if coinsNo[index] >= 0 and index+coin <= sum:
#             if coinsNo[index+coin] < 0 or coinsNo[index] + 1 < coinsNo[index+coin]:
#                 coinsNo[index+coin] = coinsNo[index] + 1
#                 lastCoin[index+coin] = coin
# coining=[]
# while(sum):
#     coining.append(lastCoin[sum])
#     sum -= coining[-1]
# coining.reverse()
# print(coining)
#
# print(partSums)
# print(coinsNo)
# print(lastCoin)

# # problema 4
# V = [0, 5, 1, 7, 3, 7, 8, 4, 9, 2]
# V = [5, 7, 2, 9, 3, 4, 8, 2, 15, 12, 13, 1, 4]
# lengthAt = [1] * len(V)
# lastFor = [0] * len(V)
# for currentIndex in range(1, len(V)):
#     for index in range(1, currentIndex):
#         if V[index] < V[currentIndex] and lengthAt[index]+1 > lengthAt[currentIndex]:
#             lengthAt[currentIndex] = lengthAt[index] + 1
#             lastFor[currentIndex] = index
# index = lengthAt.index(max(lengthAt))
# seq =[]
# while(index):
#     seq.append(V[index])
#     index = lastFor[index]
#
# print(tuple([i for i in range(len(V))]))
# print(V)
# print(lengthAt)
# print(lastFor)
#
# seq.reverse()
# print(seq)

# # problema 5
# s = "UBSSIR"
# t = "RUSSSTICE"
# table = [[0] * len(s) for i in range(len(t))]
# if s[0] == t[0]:
#     table[0][0] = 1
# for line in range(1, len(t)):
#     table[line][0] = table[line-1][0] + (s[0] == t[line] and t[line] != t[line-1])
# for row in range(1, len(s)):
#     table[0][row] = table[0][row-1] + (s[row] == t[0] and s[row] != s[row-1])
# for line in range(1, len(t)):
#     for row in range(1, len(s)):
#         table[line][row] = max([table[line-1][row], table[line][row-1], table[line-1][row-1]+(s[row]==t[line])])
#
# for line in table:
#     print(line)
#
# line = len(t)-1
# row = len(s)-1
# seq = []
# while (line and row):
#     while(line and table[line-1][row] == table[line][row]):
#         line -= 1
#     while(row and table[line][row-1] == table[line][row]):
#         row -= 1
#     seq.append(t[line])
#     line -= 1
#     row -= 1
# seq.reverse()
# print(seq)

# # problema 6
# from operator import itemgetter
# maxWgh = 50
# objectsNo = 3
# objects = [(100, 20), (60, 10), (120, 30)]
# objects.sort(key=itemgetter(1))
# valForWgh = [-1] * (maxWgh+1)
# lastFor = [-1] * (maxWgh+1)
# valForWgh[0] = 0
# for objIndex, obj in enumerate(objects):
#     for index in range(maxWgh+1):
#         if valForWgh[index] >= 0 and lastFor[index] != objIndex:
#             if index + obj[1] <= maxWgh and valForWgh[index] + obj[0] > valForWgh[index + obj[1]]:
#                 valForWgh[index + obj[1]] = valForWgh[index] + obj[0]
#                 lastFor[index + obj[1]] = objIndex
#
# def printList(list):
#     for i in range(maxWgh + 1):
#         if valForWgh[i] >= 0:
#             print(list[i], end="\t")
#     print()
# printList([*range(maxWgh+1)])
# printList(valForWgh)
# printList(lastFor)
#
# wgh = valForWgh.index(max(valForWgh))
# objs = []
# while(wgh):
#     objs.append(objects[lastFor[wgh]])
#     wgh -= objects[lastFor[wgh]][1]
# objs.reverse()
#
# print(objs)

"""
# problema 8
with open("nvectori.txt") as file:
    n, k = [int(x) for x in file.readline().split()]
    arrays = [[int(x) for x in file.readline().split()] for i in range(n)]
    for line in arrays:
        print(line)
partSums = [-1] * (k+1)
partSums[0] = 0
arraysIn = [[]] * (k+1)

for arrayIndex in range(n):
    for elem in arrays[arrayIndex]:
        for index in range(k+1):
            if partSums[index] >= 0:
                if len(arraysIn[index]) == 0 or (len(arraysIn[index]) != 0 and arraysIn[index][-1] != arrayIndex):
                    pass
for x in partSums:
    print(str(x).center(4), end="")
print()
for x in arraysIn:
    print(str(x).center(4), end="")
print()
"""
