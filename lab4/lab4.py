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

# problema 4
def prime_number_generator():
    primes = []
    n = 2
    while True:
        for x in primes:
            if n % x == 0:
                break
        else:
            primes.append(n)
            yield n
        n += 1
i = 0
for prime in prime_number_generator():
    i += 1
    print(prime)
    if i > 20:
        break