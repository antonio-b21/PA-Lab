##problema 1
# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
#
# d = b**2 - 4*a*c
#
# if d < 0:
#    print("nu are nicio radacina")
# elif d == 0:
#    x = (-b)/(2*a)
#    print("are o radacina x=" + str(x))
# else:
#    x1 = (-b + d**0.5)/(2*a)
#    x2 = (-b - d**0.5)/(2*a)
#    print("are doua radacini x1=" + str(x1) + " x2=" + str(x2))

##problema 2
# l1 = int(input("l1="))
# l2 = int(input("l2="))
#
# arie = l1 * l2
# while l1 != l2:
#    if l1 > l2:
#        l1 -= l2
#    else:
#        l2 -= l1
#
# nrPlaci = arie//(l1**2)
#
# print(nrPlaci, "placi avand latura de", l1, "cm")

##problema 3
# x = int(input("x="))
# n = int(input("n="))
# p = int(input("p="))
# m = int(input("m="))
#
# dist = 0
#
# for i in range(m):
#    if i and i%n == 0:
#        x *=1-p/100
#    dist += x
#
# print(dist, "cm")
#

##problema 4
# n = int(input("n="))
# cursIeri = float(input("1curs="))
# crestereMax = 0
#
# for i in range(1, n):
#    cursAzi = float(input(str(i+1)+"curs="))
#    crestereAzi = (cursAzi - cursIeri)
#
#    if crestereAzi > crestereMax:
#        crestereMax = crestereAzi
#        ziCrestereMax = i
#    cursIeri = cursAzi
#
# if crestereMax > 0:
#    print(crestereMax, "intre zilele", ziCrestereMax, ziCrestereMax+1)
# else:
#    print("Nu exista crestere")

##problema 5
# n = int(input("n="))
# max1 = 0
# max2 = 0
#
# for i in range(n):
#    x = int(input(str(i+1)+"x="))
#    if x > max1:
#        max2 = max1
#        max1 = x
#    elif x != max1 and x > max2:
#        max2 = x
#
# if max2:
#    print(max1, max2)
# else:
#    print("Imposibil")

# # problema 6
# n = int(input("n="))
#
# maxim = 0
# for i in range(9, -1, -1):
#     n1 = n
#     contor = 0
#     while n1:
#         if n1 % 10 == i:
#             contor += 1
#         n1 //= 10
#     for j in range(contor):
#         maxim *= 10
#         maxim += i
#
# minim = 0
# n1 = n
# contorZero = 0
# while n1:
#     if n1 % 10 == 0:
#         contorZero += 1
#     n1 //= 10
# for i in range(1, 10):
#     n1 = n
#     contor = 0
#     while n1:
#         if n1 % 10 == i:
#             contor += 1
#         n1 //= 10
#
#     for j in range(contor):
#         if contorZero and minim:
#             while contorZero:
#                 minim *= 10
#                 contorZero -= 1
#
#         minim *= 10
#         minim += i
#
# if contorZero:
#     while contorZero:
#         minim *= 10
#         contorZero -= 1
#
# print(maxim)
# print(minim)
