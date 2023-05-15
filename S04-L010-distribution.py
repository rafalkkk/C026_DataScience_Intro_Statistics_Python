from random import randint
import matplotlib.pyplot as plt

#### 1 dice

dice = []
trials = 100

for i in range(trials):
    dice.append(randint(1,6))

min_result = trials
max_result = 0
for i in range(1,7):
    result = dice.count(i)
    print(f"{i} - {result}")
    if min_result > result:
        min_result = result
    elif max_result < result:
        max_result = result

print(f'Difference: {max_result - min_result}')

plt.bar(list(range(1,7)), [dice.count(r) for r in range(1,7)], color='g')
plt.show()


#### 2 dices

dice = []
trials = 100

for i in range(trials):
    dice.append(randint(1,6) + randint(1,6))

min_result = trials
max_result = 0
for i in range(2,13):
    result = dice.count(i)
    print(f"{i} - {result}")
    if min_result > result:
        min_result = result
    elif max_result < result:
        max_result = result

print(f'Difference: {max_result - min_result}')

plt.bar(list(range(2,13)), [dice.count(r) for r in range(2,13)], color='g')
plt.show()


#### 3 dices


dice = []
trials = 100

for i in range(trials):
    dice.append(randint(1,6) + randint(1,6)+ randint(1,6))

min_result = trials
max_result = 0

for i in range(3,19):
    result = dice.count(i)
    print(f"{i} - {result}")
    if min_result > result:
        min_result = result
    elif max_result < result:
        max_result = result

print(f'Difference: {max_result - min_result}')

plt.bar(list(range(3,19)), [dice.count(r) for r in range(3,19)], color='g')
plt.show()





