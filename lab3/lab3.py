# # problema 2
# f = open("test.in")
# s = f.readlines()
# mark = 1
# g = open("test.out", "w")
# for line in s:
#     g.write(line.strip("\n"))
#     x = line.split("=")
#     x[1] = x[1].strip("\n")
#     y = x[0].split("*")
#     if (int)(y[0])*(int)(y[1]) == (int)(x[1]):
#         mark += 1
#         g.write(" Corect \n")
#     else:
#         g.write(f" Gresit {(int)(y[0])*(int)(y[1])} \n")
# g.write(f"Nota {mark}")


# # problema 3
# f = open("cheltuieli.txt")
# words = f.read().split()
# numbers = []
# sum = 0
# for word in words:
#     if word.isnumeric():
#         numbers.append(int(word))
#     elif len(word.split(".")) == 2 and word.split(".")[0].isnumeric() and word.split(".")[1].isnumeric():
#         numbers.append(float(word))
# for i in range(0, len(numbers), 2):
#     sum += numbers[i]*numbers[i+1]
# print(sum)

# # problema 4
# text = input("Sir de numere: ")
# s = {*[int(x) for x in text.split()]}
# if len(s) < 2:
#     print("Sirul nu contine doua valori distincte")
# else:
#     print(f"Maximele sirului de numere sunt {sorted(s)[-1]} si {sorted(s)[-2]}")
# # 1841 27 29424 2842 58343

# # problema 5
# import string
# text = input("Fraza de analizat: ")
# dict1 = {}
# for word in text.split():
#     word1 = word.strip(string.punctuation).lower()
#     if word1 in dict1:
#         dict1[word1] += 1
#     else:
#         dict1[word1] = 1
# dict2 = {}
# for (word, freq) in dict1.items():
#     if freq in dict2:
#         dict2[freq].append(word)
#     else:
#         dict2[freq] = [word]
#
# print(f"Cuvantul \"{sorted(dict2[max(dict2)])[0]}\" a aparut de {max(dict2)} ori, reprezentand maximul.")
# print(f"Cuvantul \"{sorted(dict2[min(dict2)])[0]}\" a aparut de {min(dict2)} ori, reprezentand minimul.")

# # problema 9
# # file = input("Numele fisierului: ")
# file = "text.txt"
# f = open(file)
# words = f.read().split()
# f.close()
# dict1 = {}
# for word in words:
#     if word[-2:] in dict1:
#         dict1[word[-2:]].add(word)
#     else:
#         dict1[word[-2:]] = {word}
#
# g = open("rime.txt", "w")
# for (rhyme, wordList) in dict1.items():
#     if len(wordList) > 1:
#         for word in sorted(wordList):
#             g.write(f"{word} ")
#         g.write("\n")
# g.close()

# # problema 1
# import random
# f = open("date.in")
# names = [x.strip("\n") for x in f.readlines()]
# f.close()
# emails = []
# for name in names:
#     name1 = name.split()
#     emails.append((f"{name1[1].lower()}.{name1[0].lower()}@myfmi.unibuc.ro",
#                    chr(random.randint(0, 25) + ord('A')) +
#                    chr(random.randint(0, 25) + ord('a')) + chr(random.randint(0, 25) + ord('a')) + chr(random.randint(0, 25) + ord('a')) +
#                    str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) ))
# g = open("date.out", "w")
# for email in emails:
#     g.write(f"{email[0]},{email[1]}\n")
# g.close()

# # problema 8
# from string import punctuation
# f = open("bacan.txt")
# text = f.readline()
# f.close()
# chosenWord = "bacan"
# #word = input("Cuvant: ")
# chosenWord = {*chosenWord}
# for word in text.split():
#     word1 = {*word.strip(punctuation)}
#     if chosenWord == word1:
#         print(word.strip(punctuation), end = " ")

# # problema 12
# participants = [(64, 'a', 1), (23, 'b', 2), (53, 'c', 3), (64, 'd', 4)]
# # score, order = int(input("Punctaj:")), 1
# # participants = []
# # while score != -1:
# #     name = input("Nume:")
# #     participants.append((score, name, order))
# #     order += 1
# #     score = int(input("Punctaj:"))
# scores = {x[0] for x in participants}
# print(scores)
# ranking = {}
# for participant in participants:
#     if participant[0] not in ranking:
#         ranking[participant[0]] = [(participant[1], participant[2])]
#     else:
#         ranking[participant[0]].append((participant[1], participant[2]))
#
# for score in sorted(ranking.keys(), reverse=True):
#     # for participant in ranking[score]:
#     #     print(score, participant[0], participant[1])
#     print(f"{score}: {ranking[score]}")

# # problema 13
# def spiral(n):
#     yield from  top_right(0, 0, n - 1, n - 1)
#
# def top_right(x1, y1, x2, y2):
#     if x1 <= x2 and y1 <= y2:
#         for j in range(x1, x2 + 1):
#             yield (y1, j)
#         for i in range(y1 + 1, y2 + 1):
#             yield (i, x2)
#         yield from bottom_left(x1, y1 + 1, x2 - 1, y2)
#
# def bottom_left(x1, y1, x2, y2):
#     if x1 <= x2 and y1 <= y2:
#         for j in range(x2, x1 - 1, -1):
#             yield (y2, j)
#         for i in range(y2 - 1,  y1 - 1, -1):
#             yield (i, x1)
#         yield from top_right(x1 + 1, y1, x2, y2 - 1)
#
# dim = int(input("n: "))
# matrix = [[(row * dim) + col + 1 for col in range(dim)] for row in range(dim)]
# for row in matrix:
#     for col in row:
#         print(col, end="\t")
#     print()
# print()
#
# path = [x for x in spiral(dim)]
# print(path)
# spiralMatrix = [matrix[x][y] for (x, y) in path]
# print(spiralMatrix)

# # problema 14
# f = open("graf_in.txt")
# graphType = 1 if f.readline().lower()[:-1] == "orientat" else 0
# nodesNum = int(f.readline())
# edgesNum = int(f.readline())
# edges = [tuple(int(x) for x in f.readline()[:-1].split()) for i in range (edgesNum)]
# startNode, finishNode = [int(n) for n in f.readline()[:-1].split()]
# f.close()
# """a)"""
# if graphType == 1:
#     print(f"Lista arcelor grafului orientat: {edges}")
# else:
#     print(f"Lista muchiilor grafului neorientat: {edges}")
# """b)"""
# adjacencyLists = {node:[] for node in range(1, nodesNum + 1)}
# for (node1, node2) in edges:
#     adjacencyLists[node1].append(node2)
#     if graphType == 0:
#         adjacencyLists[node2].append(node1)
# ##print("Listele de adiacenta ale grafului sunt:", *[f"\n{int(entry[0])}-{entry[1]}" for entry in adjacencyLists.items()])
# ##print("Listele de adiacenta ale grafului sunt:", *[entry for entry in adjacencyLists.items()])
# print("Listele de adiacenta ale grafului sunt:\n" + "\n".join([": ".join([str(entry[0]), ', '.join([str(x) for x in entry[1]])]) for entry in adjacencyLists.items()]))
# """c)"""
# adjacencyMatrix = [[0 for j in range(nodesNum)] for i in range(nodesNum)]
# for (node1, node2) in edges:
#     adjacencyMatrix[node1 - 1][node2 - 1] = 1
#     if graphType == 0:
#         adjacencyMatrix[node2 - 1][node1 - 1] = 1
# print("Matricea de adiacenta a grafului este:")
# print("\t"+"\t".join([str(i + 1) for i in range(nodesNum)]))
# for i in range(nodesNum):
#     print(i + 1, end="\t")
#     for col in adjacencyMatrix[i]:
#         print(col, end="\t")
#     print()
# """d)"""
# BF = []
# BF.append((startNode, -1))
# left = right = 0
# while left <= right:
#     fatherNode = BF[left][0]
#     for node in adjacencyLists[fatherNode]:
#         if node not in [node for (node, fatherNode1) in BF]:
#             BF.append((node, fatherNode))
#             right += 1
#     left += 1
# print(f"Parcurgerea in latime se face in felul urmator:{', '.join([str(node) for (node, fatherNode) in BF])}")
# """e)"""
# DF = []
# checked = []
# DF.append(startNode)
# checked.append(startNode)
# while DF:
#     fatherNode = DF[-1]
#     for node in adjacencyLists[fatherNode]:
#         if node not in checked:
#             DF.append(node)
#             checked.append(node)
#             break
#     else:
#         DF.pop(-1)
# print(f"Parcurgerea in adancime se face in felul urmator:{', '.join([str(node) for node in checked])}")
# """f)"""
# path = []
# path.append(finishNode)
# while path[-1] != startNode:
#     for (node, fatherNode) in BF:
#         if node == path[-1]:
#             break
#     path.append(fatherNode)
# path.reverse()
# print(path)

# # problema 15
# f = open("persoane.in")
# people = f.readlines()
# f.close()
# dictList = []
# for person in people:
#     person1 = [x.split(":", 1) for x in person[:-1].split(",", 2)]
#     dict = {}
#     for (key, value) in person1:
#         if key != "adresa":
#             dict[key] = value
#         else:
#             dict2 = {}
#             adress = [x.split(":") for x in value[1:-1].split(",")]
#             for (key2, value2) in adress:
#                 dict2[key2] = value2
#             dict[key] = dict2
#     dictList.append(dict)
# print(dictList)
# cityDict = {}
# for person in dictList:
#     oras = person["adresa"]["oras"]
#     if oras not in cityDict:
#         cityDict[oras] = [(person["prenume"], person["nume"])]
#     else:
#         cityDict[oras].append((person["prenume"], person["nume"]))
# print(cityDict)
