# # problema 2
# from operator import itemgetter
# def findMaxRect(left, right, down, up):
#     maxRect = [0, None]
#     empty = True
#     for tree in trees:
#         if left < tree[0] < right and down < tree[1] < up:
#             empty = False
#             rightRect = findMaxRect(tree[0], right, down, up)
#             leftRect = findMaxRect(left, tree[0], down, up)
#             upRect = findMaxRect(left, right, tree[1], up)
#             downRect = findMaxRect(left, right, down, tree[1])
#             rects = [rightRect, leftRect, upRect, downRect]
#             rects.sort(key=itemgetter(0), reverse=True)
#             if rects[0][0] > maxRect[0]:
#                 maxRect = rects[0]
#     if empty:
#         area = (right - left) * (up - down)
#         return area, [left, right, down, up]
#     else:
#         return maxRect
#
# f = open("copaci.txt")
# left, down = tuple([int(x) for x in f.readline().split()])
# right, up = tuple([int(x) for x in f.readline().split()])
# treesNo = int(f.readline())
# trees = []
# for i in range(treesNo):
#     tree = tuple([int(x) for x in f.readline().split()])
#     trees.append(tree)
# print(trees)
# print(left, right, down, up)
# print(findMaxRect(left, right, down, up))

# # problema 3
# def binarySearch(lista, left, right, x):
#     if left  + 1 == right:
#         return left
#     else:
#         mid = (left + right) // 2
#         if x < lista[mid]:
#             return binarySearch(lista, left, mid, x)
#         else:
#             return binarySearch(lista, mid, right, x)
# lista = [54,64,55,88,34,94,88,17,15,39,10,33,32,90,52,43,72,53,47,49]
# lista.sort()
# print(lista)
# x = 52
# while x-1 in lista:
#     lista.remove(x-1)
# while x+1 in lista:
#     lista.remove(x+1)
#
# print(binarySearch(lista, 0, len(lista), x+1) - binarySearch(lista, 0, len(lista), x-1))

# # problema 4
# def findPeak(list, left, right):
#     if left + 1 == right:
#         print(left)
#     else:
#         mid = (left + right) // 2
#         print(list[left: right])
#         if list[mid - 1] < list[mid] > list[mid + 1]:
#             print(mid)
#         elif list[mid - 1] < list[mid] < list[mid + 1]:
#             findPeak(list, mid, right)
#         elif list[mid - 1] > list[mid] > list[mid + 1]:
#             findPeak(list, left, mid)
# with open("date.in") as file:
#     n = int(file.readline())
#     list = [int(x) for x in file.readline().split()]
#
# findPeak(list, 0, n)

# # problema 5
# def zFill(n, x=0, y=0):
#     if n == 0:
#         global k
#         mat[x][y] = k
#         k += 1
#     else:
#         n -= 1
#         zFill(n, x + 0, y + 0)
#         zFill(n, x + 0, y + 2 ** n)
#         zFill(n, x + 2 ** n, y + 0)
#         zFill(n, x + 2 ** n, y + 2 ** n)
# n = 2
# k = 1
# mat = [[0] * 2 ** n for i in range(2 ** n)]
# zFill(n)
# for line in mat:
#     print(line)

# n = 3
# x, y = 2, 0
# i = 0
# n -= 1
# while n+1:
#     if x >= 2**n and y >= 2**n:
#         i += 2**(n*2)*3
#         x -= 2**n
#         y -= 2**n
#     elif x >= 2**n:
#         i += 2**(n*2)
#         x -= 2**n
#     elif y >= 2**n:
#         pass
#     else:
#         i += 2**(n*2)*2
#         y -= 2**n
#     n -=1
# print(i+1)

# # problema 6
# def fill(n, i, j, x, y):
#     global k
#     if n == 1:
#         if i != x or j != y:
#             mat[i][j] = k
#         if i+1 != x or j != y:
#             mat[i+1][j] = k
#         if i != x or j+1 != y:
#             mat[i][j+1] = k
#         if i+1 != x or j+1 != y:
#             mat[i+1][j+1] = k
#         k += 1
#     else:
#         if x < i + 2**(n-1) and y < j + 2**(n-1):
#             mat[i+2**(n-1)-1][j+2**(n-1)] = k
#             mat[i+2**(n-1)][j+2**(n-1)-1] = k
#             mat[i+2**(n-1)][j+2**(n-1)] = k
#             k += 1
#             fill(n-1, i, j, x, y)
#             fill(n-1, i, j+2**(n-1), i+2**(n-1)-1, j+2**(n-1))
#             fill(n-1, i+2**(n-1), j, i+2**(n-1), j+2**(n-1)-1)
#             fill(n-1, i+2**(n-1), j+2**(n-1), i+2**(n-1), j+2**(n-1))
#         elif x < i + 2**(n-1):
#             mat[i+2**(n-1)-1][j+2**(n-1)-1] = k
#             mat[i+2**(n-1)][j+2**(n-1)-1] = k
#             mat[i+2**(n-1)][j+2**(n-1)] = k
#             k += 1
#             fill(n-1, i, j, i+2**(n-1)-1, j+2**(n-1)-1)
#             fill(n-1, i, j+2**(n-1), x, y)
#             fill(n-1, i+2**(n-1), j, i+2**(n-1), j+2**(n-1)-1)
#             fill(n-1, i+2**(n-1), j+2**(n-1), i+2**(n-1), j+2**(n-1))
#         elif y < j + 2**(n-1):
#             mat[i+2**(n-1)-1][y+2**(n-1)-1] = k
#             mat[i+2**(n-1)-1][j+2**(n-1)] = k
#             mat[i+2**(n-1)][j+2**(n-1)] = k
#             k += 1
#             fill(n-1, i, j, i+2**(n-1)-1, y+2**(n-1)-1)
#             fill(n-1, i, j+2**(n-1), i+2**(n-1)-1, j+2**(n-1))
#             fill(n-1, i+2**(n-1), j, x, y)
#             fill(n-1, i+2**(n-1), j+2**(n-1), i+2**(n-1), j+2**(n-1))
#         else:
#             mat[i+2**(n-1)-1][y+2**(n-1)-1] = k
#             mat[i+2**(n-1)-1][j+2**(n-1)] = k
#             mat[i+2**(n-1)][j+2**(n-1)-1] = k
#             k += 1
#             fill(n-1, i, j, i+2**(n-1)-1, y+2**(n-1)-1)
#             fill(n-1, i, j+2**(n-1), i+2**(n-1)-1, j+2**(n-1))
#             fill(n-1, i+2**(n-1), j, i+2**(n-1), j+2**(n-1)-1)
#             fill(n-1, i+2**(n-1), j+2**(n-1), x, y)
#
# f = open("piesa.in")
# n = int(f.readline())
# mat = [[0] * 2**n for x in range(2**n)]
# x, y = [int(x)-1 for x in f.readline().split()]
# mat[x][y] = 0
# k = 1
# fill(n, 0, 0, x, y)
# for line in mat:
#     for elem in line:
#         print(elem, end="\t")
#     print()

# problema 7




# # problema 11
# def decomp(number):
#     global sum
#     if sum == number:
#         print(lista)
#
#     else:
#         diff = number - sum
#         if len(lista):
#             diff = min(diff, lista[-1]-1)
#         for i in range(diff, 0, -1):
#             sum += i
#             lista.append(i)
#             decomp(number)
#     if sum:
#         sum -= lista.pop()
# sum = 0
# number = 7
# lista = []
# decomp(number)

# # problema 12
# def sumIs(number):
#     global sum
#     if sum == number and 0 in solution:
#         print(int("".join([str(x) for x in solution])))
#     else:
#         diff = number - sum
#         for i in range(diff+1):
#             if i not in solution:
#                 sum += i
#                 solution.append(i)
#                 sumIs(number)
#     if len(solution):
#         sum -= solution.pop()
# number = 4
# sum = 0
# solution = []
# sumIs(number)

# # problema 13
# def colouring(countriesNo, currentLevel):
#     if currentLevel == countriesNo:
#         for i in range(1, max(colours)):
#             if i not in colours:
#                 break
#         else:
#             print(colours)
#     else:
#         for colour in range(1, 4+1):
#             for level in range(currentLevel):
#                 if colours[level] == colour and (level, currentLevel) in borders:
#                     break
#             else:
#                 colours.append(colour)
#                 colouring(countriesNo, currentLevel+1)
#     if len(colours):
#         colours.pop()
#         currentLevel -= 1
# f = open("harti.txt")
# countriesNo = int(f.readline())
# borders = []
# for line in f.readlines():
#     border = tuple([int(x)-1 for x in line.split()])
#     if border [1] < border[0]:
#         border = (border[1], border[0])
#     borders.append(border)
#
# colours = []
# colouring(countriesNo, 0)

# # problema 14
# from operator import itemgetter
# def scheduling():
#     global maxLen
#     if len(schedule) and schedule[-1][1] > max(events, key=itemgetter(0))[0]:
#         if maxLen is None:
#             print(schedule)
#             maxLen = len(schedule)
#         elif maxLen == len(schedule):
#             print(schedule)
#     else:
#         for event in events:
#             if event in schedule:
#                 continue
#             if len(schedule) == 0:
#                 schedule.append(event)
#             else:
#                 if event[0] >= schedule[-1][1]:
#                     schedule.append(event)
#                 else:
#                     continue
#             scheduling()
#     if len(schedule):
#         schedule.pop()
#
# f = open("spectacole.txt")
# events = []
# for line in f.readlines():
#     x = line.split("-", 1)
#     y = x[1].split(" ", 1)
#     event = (x[0], y[0], y[1][:-1])
#     events.append(event)
#
# events.sort(key=itemgetter(1))
# schedule = []
# maxLen = None
# scheduling()
