from math import pow
def genPart(part):
    y = part[0]
    if(len(y) > 1):
        low = int(pow(2, len(y)-1))
        upp = int(pow(2, len(y)))
        for i in range (low, upp-1):
            a1, a2 = [], []
            for j in range(len(y)):
                if int(str(bin(i))[2:][j]) == 1:
                    a1.append(y[j])
                else:
                    a2.append(y[j])
            x = [a1, a2] if len(a2) else [a1]
            x.extend(part[1:])
            for j in range(2, len(x)):
                if x[j][0] < x[j-1][0]:
                    break
            else:
                partitions.append(x)
                genPart(x)

set1 = [[x for x in "1234"]]
partitions = [set1]
genPart(set1)
for i in range(len(partitions)):
    print(f"{i+1}:", *partitions[i])