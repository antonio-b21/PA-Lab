def calculeaza(n, i, j):
    elem = 0
    n -= 1
    while n+1:
        if i >= 2**n and j >= 2**n:
            elem += 2**(n*2)*3
            i -= 2**n
            j -= 2**n
        elif i >= 2**n:
            elem += 2**(n*2)*2
            i -= 2**n
        elif j >= 2**n:
            elem += 2**(n*2)
            j -= 2**n
        n -=1
    fileOut.write(str(elem+1)+"\n")

file = open("z.in")
# n, k = [int(x) for x in file.readline().split()]
n, k = map(int, file.readline().split())
fileOut = open("z.out", "w")
for x in range(k):
    i, j = [int(a)-1 for a in file.readline().split()]
    calculeaza(n, i, j)

