from random import randint
import matplotlib.pyplot as plt

####  5 dices

dice = []
trials = 1000000

for i in range(trials):
    dice.append(randint(1,6) + randint(1,6)+ randint(1,6)+ randint(1,6)+ randint(1,6))

min_result = trials
max_result = 0

for i in range(5,31):
    result = dice.count(i)
    print(f"{i} - {result}")
    if min_result > result:
        min_result = result
    elif max_result < result:
        max_result = result

print(f'Difference: {max_result - min_result}')

plt.bar(list(range(5,31)), [dice.count(r) for r in range(5,31)], color='g')
plt.show()