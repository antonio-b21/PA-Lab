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

# problema

