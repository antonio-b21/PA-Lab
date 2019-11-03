# # Problema 1
# prop = input("Propoziia:")
# sirGresit = input("Sir gresit:")
# sirCorect = input("Sir corect:")
#
# prop = prop.replace(sirGresit, sirCorect)
# print(prop)
#
# # Problema 2
# sir = input("Sir:")
# sirNou = ""
# cuvinte = sir.split()
#
# for cuvant in cuvinte:
#    sirNou += cuvant.capitalize()
#    sirNou += " "
# sirNou.strip()
# print(sirNou)
#
# #Problema 3   DE COMPLETAT
# sir = "Ana care arem mere ,are pere"#input("Propoziia:")
# s = "are"#input("Cuvant inlocuit:")
# t = "n-are"#input("Cuvant oinlocuitor:")
# k = len(s)
# poz = sir.find(s)
#
#
#
# while poz != -1:
#    if (poz == 0 or sir[poz-1].isalpha() == False) and (poz+k == len(sir) or sir[poz + k].isalpha() == False):
#        sir = sir[:poz] + sir[poz:].replace(s,t,1)
#    poz = sir.find(s, poz+k)
#
# print(sir)
#
# #problema 4
# sir1 = input("sir1:")
# sir2 = input("sir2:")
# sir2Copie = sir2
# for caracter in sir1:
#    if caracter in sir2Copie:
#        poz = sir2Copie.find(caracter)
#        sir2Copie = sir2Copie[:poz] + sir2Copie[poz+1:]
#    else:
#        print("Nu sunt anagrame")
#        break
#
# else:
#    print("Sunt anagrame")
#
#
# # Problema 5
# def criptare(cheie, sir):
#     sirCriptat = ""
#     for caracter in sir:
#         t = 0
#         if caracter.islower():
#             t += ord(caracter)
#             t -= ord('a')
#             t += k
#             t %= 26
#             t += ord('a')
#         elif caracter.isupper():
#             t += ord(caracter)
#             t -= ord('A')
#             t += k
#             t %= 26
#             t += ord('A')
#         caracterNou = chr(t)
#         sirCriptat += caracterNou
#     return sirCriptat
#
#
# sir = input("Text:")
# k = int(input("Cheia:"))
#
# sirCriptat = criptare(k, sir)
# print("Sir criptat: ", sirCriptat)
#
# k = -k
# sirDecriptat = criptare(k, sirCriptat)
# print("Sir decriptat: ", sirDecriptat)
#
# # problema 6
# sir = input("Text:")
# sir = "Astăzi am cumpărat pâine de 5 RON, pe lapte am dat 10 RON, iar de 15 RON am cumpărat niște " \
#       "cașcaval. De asemenea, mi-am cumpărat și niște papuci cu 50 RON!"
# cuvinte = sir.split()
# suma = 0
# for i in range(len(cuvinte) - 1):
#     print(cuvinte[i], cuvinte[i + 1].find("RON"))
#     if cuvinte[i].isnumeric() and cuvinte[i + 1].find("RON") == 0:
#         suma += int(cuvinte[i])
# print(suma)
#
# #problema 7
# dateStr = input("Data:").lower()
# day = 0
# date = tuple(dateStr.split())
#
# def leap_year(year):
#     if year % 400 == 0:
#         return True
#     if year % 100 == 0:
#         return False
#     if year % 4 == 0:
#         return True
#     return False
#
# for i in range(1703, int(date[2])):
#     if leap_year(i):
#         day = (day + 366) % 7
#     else:
#         day = (day + 365) % 7
# if int(date[2]) > 1702:
#     day = (day + 1) % 7
#
# months = {"jan":0, "feb":1, "mar":2, "apr":3, "may":4, "jun":5, "jul":6, "aug":7, "sep":8, "oct":9, "nov":10, "dec":11}
# if date[1].isalpha():
#     date = (int(date[0]), months[date[1]], int(date[2]))
# daysInMonth = {0:31, 1:28, 2:31, 3:30, 4:31, 5:30, 6:31, 7:31, 8:30, 9:31, 10:30, 11:31}
# for i in range(date[1]):
#     day = (day + daysInMonth[i]) % 7
# if date[1] > 1 and leap_year(date[2]):
#     day = (day + 1) % 7
#
# day = (day - 1 + date[0]) % 7
# days = {0:"Duminica", 1:"Luni", 2:"Marti", 3:"Miercuri", 4:"Joi", 5:"Vineri", 6:"Sambata"}
# print(days[day])
#
# # problema 8

# #a)
# sir = input("Text:")
# n = len(sir)
# i = 0
# while i < n:
#     if sir[i] in "aeiouAEIOU":
#         sir = sir[:i+1] + "p" + sir[i].lower() + sir[i+1:]
#         i += 2
#         n += 2
#     i += 1
# print(sir)
# import string
# sir = input("Text:")
# cuv = sir.split()
# cuvinte = [x.split("-") for x in cuv]
# sirNou = ""
# sirNou2 = ""
# for cuvant in cuvinte:
#     for silaba in cuvant:
#         if silaba[-1].isalpha():
#             sirNou += silaba + "p" + silaba[-1].lower() + "-"
#             sirNou2 += silaba + "p" + silaba[-1].lower()
#         else:
#             sirNou += silaba[:-1] + "p" + silaba[-2].lower() + silaba[-1] + "-"
#             sirNou2 += silaba[:-1] + "p" + silaba[-2].lower() + silaba[-1]
#     sirNou = sirNou[:-1] + " "
#     sirNou2 += " "
# sirNou = sirNou.strip()
# sirNou2 = sirNou2.strip()
# print(sirNou)
# print(sirNou2)
#
#
# n = len(sirNou)
# i = 2
# while i < n:
#     if sirNou[i] == "-":
#         sirNou = sirNou[:i-2] + sirNou[i+1:]
#         i -= 3
#         n -= 3
#     elif sirNou[i] in string.punctuation+" ":
#         sirNou = sirNou[:i - 2] + sirNou[i:]
#         i -= 2
#         n -= 2
#         if i < n-1 and sirNou[i+1] == " ":
#             i += 1
#     i += 1
# print(sirNou)

# # problema 9
# import string
# sir = input("Text:")
# cuvinte = sir.split()
# sume = []
# for cuvant in cuvinte:
#     if "$" in cuvant:
#         sume.append(cuvant.strip(string.punctuation))
# print(f"Primele oferte au fost {sume[0]} si {sume[1]}", end= "")
# if sume[-1] == sume[-2]:
#     print(f", iar cele doua persoane s-au inteles la pretul de {sume[-1]}.")
# else:
#     print(", iar cele doua persoane nu s-au inteles asupra unui pret.")

# # problema 11
# import string
# sir = input("text:")
# propozitii = []
# start = 0
# i = 2
# while i < len(sir):
#     if sir[i] in string.ascii_uppercase and sir[i-2] == ".":
#         propozitii.append(sir[start: i-1])
#         start = i
#     i += 1
# propozitii.append(sir[start: i])
# print(propozitii)

# # problema 12
# sir = input("Text:")
# sir2 = input("Text:")
# print(sir, sir2)
# while (len(sir) >= 1 and len(sir2) >= 1) and sir[-1] == sir2[0]:
#     while len(sir) >= 2 and sir[-2] == sir[-1]:
#         sir = sir[:-1]
#         print(sir, sir2)
#     while len(sir2) >= 2 and sir2[1] == sir2[0]:
#         sir2 = sir2[1:]
#         print(sir, sir2)
#     sir = sir[:-1]
#     sir2 = sir2[1:]
#     print(sir, sir2)