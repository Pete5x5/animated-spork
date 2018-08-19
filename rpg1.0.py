import random
print('RANDOM PIZZA GENERATOR 1.0')
print('As the dice will it, it shall be done')
print('')
tops = 0
pizzas = 0
print('How many pizzas would you like generated?')

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

totaltops = alltops
ontop = 1
toplist = ['a'] * alltops

while alltops > 0:
    print('Enter topping number' + str(ontop))
    while True:
        currtop = input()
        if len(currtop) > 50:
            print('Topping name too long')
            continue
        else:
            toplist[ontop-1] = currtop
            break
    ontop = ontop + 1
    alltops = alltops - 1

numtops = tops

currpizza = 1

while pizzas > 0:
    print('')
    print('Pizza #' + str(currpizza))
    while numtops > 0:
        print(toplist[random.randint(0,totaltops-1)])
        numtops = numtops - 1
    numtops = tops
    currpizza = currpizza + 1
    pizzas = pizzas - 1
    