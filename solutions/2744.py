test = list(input())

for i in range(len(test)):
    if test[i].isupper() is True:
        test_lower = test[i].lower()
        test[i] = test[i].replace(test[i], test_lower)
    else:
        test_upper = test[i].upper()
        test[i] = test[i].replace(test[i], test_upper)

print(''.join(test))