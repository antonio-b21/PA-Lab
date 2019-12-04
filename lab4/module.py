def citire():
    n = int(input("n: "))
    v = [int(input(f"v[{i+1}]: ")) for i in range(n)]
    return n, v

def afisare(v):
    print(*v)

def valpoz(v):
    vp = [x for x in v if x > 0]
    return vp

def semn(v):
    vs = [-x for x in v]
    return vs