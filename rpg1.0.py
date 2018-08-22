import random
print('''RANDOM PIZZA GENERATOR 1.0
As the dice will it, it shall be done

How many pizzas would you like generated?''')

while True:
    pizzas = input()
    try:
         pizzas = int(pizzas)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if pizzas < 1:
            print('Not enough pizzas')
            continue
        elif pizzas > 12:
            print('That\'s too many pizzas!')
            continue
        else:
            break
        
print('How many toppings are there per pizza?')
while True:
    tops = input()
    try:
         tops = int(tops)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if tops <= 1:
            print('Not enough toppings')
            continue
        elif tops > 12:
            print('That\'s too many toppings!')
            continue 
        else:
            break

print('How many toppings are there to choose from?')
while True:
    alltops = input()
    try:
         alltops = int(alltops)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if alltops <= 1:
            print('Not enough toppings')
            continue
        elif alltops > 99:
            print('That\'s too many toppings!')
            continue 
        else:
            break

print('''Would you like to allow duplicate toppings?
1 - Yes, that is how the dice will it
2 - No, triple olives is gross\n''')

while True:
    dupetops = input()
    if dupetops == '1' or dupetops == '2':
        break
    else:
        print('Invalid choice')
        continue

toplist = []

for iv1 in range(alltops):
    print('Enter topping number ' + str(iv1+1))
    while True:
        currtop = input()
        if len(currtop) > 50:
            print('Topping name too long')
            continue
        elif currtop in toplist:
            print('You already have that topping')
            continue
        else:
            toplist += [currtop]
            break

allpizzas = []

for iv2 in range(pizzas):
    pizzagen = []
    print('\nPizza #' + str(iv2+1))
    for iv3 in range(tops):
        pizzagen += [toplist[random.randint(0,alltops-1)]]
    for top in pizzagen:
        print(top)
    