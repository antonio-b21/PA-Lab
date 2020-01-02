# # problema 1
# from math import sqrt, pow
# def ipotenuza(a, b):
#     return sqrt(pow(a, 2) + pow(b, 2))
# g = open("pitagoriene.txt", "wt")
# b = int(input("b= "))
# for a in range(1, b):
#     c = ipotenuza(a, b)
#     if c.is_integer():
#         c = int(c)
#         g.write(str(a) + " " + str(b) + " " + str(c) + "\n")
# g.close()

# # problema 2
# from math import pi
# def lungime_arie_cerc(r):
#     return 2 * pi * r, pi * r * r
# r = int(input("r= "))
#
# print(f"Pentru un cerc de raza {r}, circumferinta este egala cu {lungime_arie_cerc(r)[0]} si aria este egala cu {lungime_arie_cerc(r)[1]}")

# # problema 3
# def min_max(*numbers):
#     if(len(numbers) < 1):
#         return None
#     minim = maxim = numbers[0]
#     for number in numbers:
#         if number < 0:
#             raise ValueError
#         minim = number if number<minim else minim
#         maxim = number if number>maxim else maxim
#     return minim, maxim
# try:
#     f = open("numere.txt")
#     numList = [int(x) for x in f.readline().split()]
#     f.close()
#     a,b =(min_max(*numList))
#     g = open("impartire.txt", "wt")
#     g.write(str(b/a))
#     g.close()
# except FileNotFoundError as e1:
#     print(e1.__doc__)
# except ValueError as e2:
#     print("List of pozitive integers was expected.")
# except TypeError as e3:
#     print("Not empty list was expected")
# except ZeroDivisionError as e4:
#     print(e4.__doc__)

# # problema 4
# def prime_number_generator():
#     n: int = 2
#     while True:
#         for i in range(2, n):
#             if n % i == 0:
#                 break
#         else:
#             yield n
#         n += 1
# i = 0
# for prime in prime_number_generator():
#     i += 1
#     print(prime)
#     if i == 10:
#         break

# # problema 5
# def negative_pozitive(numbers):
#     negative = []
#     pozitive = []
#     for x in numbers:
#         if x < 0:
#             negative.append(x)
#         elif x > 0:
#             pozitive.append(x)
#     return negative, pozitive
# list1 = [70, 39, -14, 13, -68, -29, -78, 99, -41, 57]
# print(negative_pozitive(list1))

# # problema 6
# from module import *
# afisare(semn(citire()[1]))

# # problema 7
# L = ["zi", "ana", "sac", "acadea", "bac", "nori", "zar", "mi", "abur"]
# print(sorted(L, reverse=True))
# print(sorted(sorted(L), key=len))
# print(sorted(L, key=len))

# # problema 8
# def a():
#     name = input()
#     for employee in info:
#         if employee[0] == name:
#             print(employee)
# def b():
#     maxSalary = 0
#     for employee in info:
#         maxSalary = max(maxSalary, employee[2])
#     maxSalaryEmployees = [x[0] for x in info if x[2] == maxSalary]
#     print(maxSalaryEmployees)
# def c():
#     averageSalary = 0
#     for employee in info:
#         averageSalary += employee[2]
#     averageSalary //= len(info)
#     print(averageSalary)
# def d():
#     print(sorted(info))
# def age(x):
#     return x[1]
# def e():
#     print(sorted(sorted(info), key=age, reverse=True))
# f = open("angajati.txt")
# info = []
# for employee in f.readlines():
#     x = employee[:-1].split(",")
#     info.append((x[0], int(x[1]), int(x[2])))
# print(info)
# e()

# # problema 9
# def read():
#     n = int(input("n:"))
#     numbers = [int(input(f"x[{i+1}]:")) for i in range(n)]
#     return n, numbers
# def pos(x, i, j, num):
#     for k in range(i, j):
#         if num[k] > x:
#             return k
#     return -1
#
# numb = [5, 4, 3, 2, 3]
# n = len(numb)
# for i in range(n):
#     if pos(numb[i]-1, i+1, n, numb) != -1:
#         print("NU")
#         break
# else:
#     print("DA")

# # problema 10
# def situatie(lista, c):
#     listaNoua = []
#     for x in lista:
#         sit = "Promovat" if x[2] >= c else "Nepromovat"
#         y = (x[0], x[1], x[2], sit)
#         listaNoua.append(y)
#     return listaNoua
# def groupKey(student):
#     return student[1]
# def creditKey(student):
#     return student[2]
# lista = [("Mig", 146, 352), ("Alt", 135, 432), ("Bim", 146, 298), ("Ion", 142, 352), ("Dan", 135, 526), ("Mai", 142, 298), ("Fou", 135, 245)]
# lista.sort(key=creditKey, reverse=True)
# lista.sort(key=groupKey)
# print(lista)

# # problema 11
# def number(*numbers):
#     returned = 0
#     for number in numbers:
#         maxDigit = 0
#         while number:
#             maxDigit = max(maxDigit, number%10)
#             number //= 10
#         returned = returned*10 + maxDigit
#     return returned
# def verifica(a, b, c):
#     n = number(a, b, c)
#     n = number(n)
#     print(n<2)
# verifica(1001, 17, 100)

# # problema 12
# def cmpValori(i, j, L):
#     return(L[i] == L[j])
# def cautare(x, L, cmpValori):
#     pos = None
#     for i in range(len(L)):
#         if L[i] == x:
#             pos = i
#     return pos
# # de continuat

# # problema 13
# from string import punctuation
# def cautare(cuv, fisOut, *fisiere):
#     g = open(fisOut, "w")
#     for fisIn in fisiere:
#         f = open(fisIn)
#         g.write(fisIn + " ")
#         lineNo = 0
#         ok = False
#         for line in f.readlines():
#             lineNo += 1
#             cuvinte = [x.strip(punctuation) for x in line.split()]
#             if cuv in cuvinte:
#                 g.write(str(lineNo) + " ")
#                 ok = True
#         if ok == False:
#             g.write("Nu exista")
#         g.write("\n")
#         f.close()
# cautare("lac","rez.txt", "eminescu.txt", "bacovia.txt")

# # problema 14
# def fileDict(fileName):
#     f = open(fileName)
#     routes = []
#     for line in f.readlines():
#         info = line.split()
#         route = {}
#         route["plecare"] = info[0]
#         route["sosire"] = info[2]
#         route["oraPlecare"] = info[3]
#         route["oraSosire"] = info[4]
#         routes.append(route)
#     return routes
# import datetime
# def tripTime(departure, arrival):
#     departureTime = datetime.datetime.strptime(departure, "%H:%M")
#     arrivalTime = datetime.datetime.strptime(arrival, "%H:%M")
#     trip = arrivalTime - departureTime
#     return str(trip)[:-3]
# def trip(routes):
#     newRoutes = []
#     for route in routes:
#         if route["plecare"] == "Bucuresti" or route["sosire"] == "Brasov":
#             newRoutes.append(route)
#     return newRoutes
# def routePlanner(routes):
#     g = open("traseu.txt", "w")
#     n = len(routes)
#     for route in routes:
#         if route["plecare"] != "Bucuresti":
#             continue
#         if route["sosire"] == "Brasov":
#             departure = route["oraPlecare"]
#             arrival = route["oraSosire"]
#             trip = tripTime(departure, arrival).split(":")
#             trip = str(trip[0])+"h" if trip[1] == "00" else str(trip[0])+"h "+str(trip[1])+"m"
#             g.write(f"Plecare la ora {departure} sosire ora {arrival} durata {trip}\n")
#         else:
#             for route2 in routes:
#                 if route2["plecare"] != route["sosire"] or route2["sosire"] != "Brasov":
#                     continue
#                 departure = route["oraPlecare"]
#                 arrival = route2["oraSosire"]
#                 trip = tripTime(departure, arrival).split(":")
#                 trip = str(trip[0]) + "h" if trip[1] == "00" else str(trip[0]) + "h " + str(trip[1]) + "m"
#                 g.write(f"Plecare la ora {departure} sosire ora {arrival} durata {trip}\n")
#     g.close()
# def leastTime(routes):
#     n = len(routes)
#     bestRoute = None
#     for route in routes:
#         if route["plecare"] != "Bucuresti":
#             continue
#         if route["sosire"] == "Brasov":
#             departure = route["oraPlecare"]
#             arrival = route["oraSosire"]
#             trip = tripTime(departure, arrival)
#         else:
#             for route2 in routes:
#                 if route2["plecare"] != route["sosire"] or route2["sosire"] != "Brasov":
#                     continue
#                 departure = route["oraPlecare"]
#                 arrival = route2["oraSosire"]
#                 trip = tripTime(departure, arrival)
#         trip = datetime.datetime.strptime(trip, "%H:%M")
#         if bestRoute is None:
#             if route["sosire"] == "Brasov":
#                 bestRoute = (trip, ["Bucuresti", "Brasov"])
#             else:
#                 bestRoute = (trip, ["Bucuresti", route["sosire"], "Brasov"])
#         elif trip < bestRoute[0]:
#             if route["sosire"] == "Brasov":
#                 bestRoute = (trip, ["Bucuresti", "Brasov"])
#             else:
#                 bestRoute = (trip, ["Bucuresti", route["sosire"], "Brasov"])
#     print(*bestRoute[1])
#
# routes = fileDict("program.txt")
# leastTime(routes)

# problema 15