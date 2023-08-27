truck = []
pay = []
bill = 0
a, b, c = map(int, input().split())
pay.append(0)
pay.append(a)
pay.append(b * 2)
pay.append(c * 3)


for i in range(3):
    p, q = map(int, input().split())
    truck.append(p)
    truck.append(q)
k = max(truck)

timetable = []
for i in range(3):
    timetable.append([truck[2 * i], truck[2 * i + 1]])

for i in range(1, k + 1):
    truck = 0
    currenttime = i
    for j in range(3):
        if timetable[j][0] < currenttime <= timetable[j][1]:
            truck += 1
    bill += pay[truck]

print(bill)
