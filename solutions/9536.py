n = int(input())
for j in range(n):
    test = list(map(str, input().split()))
    checklist = []
    while True:
        animal_saying = input().split()
        checklist.append(animal_saying[2])
        if len(animal_saying) > 3:
            break

    for i in range(len(checklist)):
        while checklist[i] in test:
            test.remove(checklist[i])

    print(' '.join(test))
