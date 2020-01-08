# # problema 1
# def tis(inp):
#     time = 0
#     totalTime = 0
#     for client in inp:
#         time += client[1]
#         totalTime += time
#         print(f"{client[0]} \t{client[1]} \t{time}")
#     print(f"timp mediu: {round(totalTime/len(inp), 2)}")
# def byTime(pair):
#     return pair[1]
# f = open("tis.txt")
# inp = f.readline().split()
# queue = [(i, int(inp[i])) for i in range(len(inp))]
# tis(queue)
# queue.sort(key=byTime)
# tis(queue)

# # problema 2
# def byEndTime(event):
#     endTime = event[1]
#     return endTime
#
# f = open("spectacole.txt")
# events = []
# for line in f.readlines():
#     x = line.split("-", 1)
#     y = x[1].split(" ", 1)
#     event = (x[0], y[0], y[1][:-1])
#     events.append(event)
#
# events.sort(key=byEndTime)
# print(events)
# plannedEvents = [events[0]]
# for event in events[1:]:
#     if event[0] >= plannedEvents[-1][1]:
#         plannedEvents.append(event)
# for event in plannedEvents:
#     print(f"{event[0]}-{event[1]} {event[2]}")

# # problema 3
# f = open("cuburi.txt")
# cubesNo = int(f.readline())
# cubes =[]
# for i in range(cubesNo):
#     x = f.readline().split()
#     cube = (int(x[0]), x[1])
#     cubes.append(cube)
#
# cubes.sort(reverse=True)
# tower = [cubes[0]]
# for cube in cubes[1:]:
#     if cube[1] != tower[-1][1]:
#         tower.append(cube)
# height = 0
# for cube in tower:
#     print(cube[0], cube[1])
#     height += cube[0]
# print(f"\ninaltime totala: {height}")

# # problema 4
# f = open("bani.txt")
# bills = [int(x) for x in f.readline().split()]
# money = int(f.readline())
# billing = []
# for bill in bills[::-1]:
#     if money > bill:
#         billsNo = money // bill
#         money -= bill * billsNo
#         billing.append((bill, billsNo))
# billingStr = " + ".join(["*".join(x) for x in [(str(a), str(b)) for (a, b) in billing]])
# print(f"{money} = {billingStr}")

# # problema 5
# f = open("activitati.txt")
# tasksNo = int(f.readline())
# tasks = []
# for i in range(tasksNo):
#     task = [int(x) for x in f.readline().split()]
#     tasks.append(task)
#
# time = 0
# maxLateness = 0
# from operator import itemgetter
# tasks.sort(key=itemgetter(1))
# for task in tasks:
#     startTime = time
#     endTime = time + task[0]
#     lateness = max(0, endTime - task [1])
#     maxLateness = max(maxLateness, lateness)
#     time += task[0]
#     print(f"({startTime} --> {endTime})\t{task[1]} \t{lateness}")
#
# print(f"Intarzierea maxima: {maxLateness}")

# # problema 6
# f = open("evenimente.txt")
# events = []
# for line in f.readlines():
#     x = line.split("-", 1)
#     y = x[1].split(" ", 1)
#     event = (x[0], y[0], y[1][:-1])
#     events.append(event)
#
# from operator import itemgetter
# events.sort(key=itemgetter(1))
# rooms = []
# for event in events:
#     for room in rooms:
#         if event[0] >= room[-1][1]:
#             room.append(event)
#             break
#     else:
#         room = [event]
#         rooms.append(room)
#
# for room in rooms:
#     print(", ".join(["("+str(a)+"-"+str(b)+" "+str(c)+")" for (a, b, c) in room]))

# # problema 7
# def byVpW(obj):
#     return obj[0]/obj[1]
# def weight(knapsack):
#     wgt = 0
#     for obj in knapsack:
#         if obj[2] == 1:
#             wgt += obj[1]
#         else:
#             wgt += obj[1] * obj[2]
#     return round(wgt)
# def value(knapsack):
#     val = 0
#     for obj in knapsack:
#         if obj[2] == 1:
#             val += obj[0]
#         else:
#             val += obj[0] * obj[2]
#     return round(val)
# f = open("obiecte.txt")
# objNo = int(f.readline())
# objs = []
# for i in range(objNo):
#     obj = tuple([int(a) for a in f.readline().split()])
#     objs.append(obj)
# weightLeft = int(f.readline())
# objs.sort(key=byVpW, reverse=True)
# knapsack = []
# for obj in objs:
#     if weightLeft == 0:
#         break
#     elif weightLeft >= obj[1]:
#         weightLeft -= obj[1]
#         knapsack.append((obj[0], obj[1], 1))
#     else:
#         fraction = weightLeft / obj[1]
#         weightLeft = 0
#         knapsack.append((obj[0], obj[1], fraction))
#         break
#
# print(str(weight(knapsack))+" = "+" + ".join([("("+str(round(c, 2))+")*"+str(b) if c != 1 else str(b)) for (a, b ,c) in knapsack]))
# print(str(value(knapsack))+" = "+" + ".join([("("+str(round(c, 2))+")*"+str(a) if c != 1 else str(a)) for (a, b ,c) in knapsack]))

# # problema 8
# f = open("proiecte.txt")
# projects = [(a, int(b), int(c)) for (a, b, c) in [line.split() for line in f.readlines()]]
# from operator import itemgetter
# projects.sort(key=itemgetter(2), reverse=True)
# schedule = {}
# for project in projects:
#     time = project[1]
#     while time:
#         if time not in schedule:
#             schedule[time] = project
#             break
#         else:
#             time -= 1
#
# sched = []
# for i in range(min(schedule), max(schedule)+1):
#     sched.append(schedule[i])
# print(sched)