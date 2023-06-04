import re
calc = input()
calc = re.findall(r'\d+|[+=-]', calc)
for i in range(len(calc)):
    try:
        calc[i] = int(calc[i])
    except:
        pass
calc = list(map(str, calc))
calc = ''.join(calc)

calc = calc.split('-')
for i in range(len(calc)):
    calc[i] = eval(calc[i])

calc_sum = calc[0]

for i in range(1, len(calc)):
    calc_sum -= calc[i]

print(calc_sum)
