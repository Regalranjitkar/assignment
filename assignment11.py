num = [1,3,5,7,8,3,5,1,7]
See = {}
for i in num:
    if i not in See:
        See[i] = 1
    else:
        See[i] += 1

for key, value in See.items():
    if value == 1:
        print(key)
