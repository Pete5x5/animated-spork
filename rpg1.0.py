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

if alltops >= tops:
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
else:
    dupetops == '1'

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

print('''Would you like to randomize the type of sauce for each pizza?
1 - Yes, true random is the only way
2 - No, I can only handle regular pizza sauce\n''')

while True:
    randsauce = input()
    if randsauce == '1' or randsauce == '2':
        break
    else:
        print('Invalid choice')
        continue

if randsauce == '1':
    print('How many sauces are there to choose from?')
    while True:
        allsauce = input()
        try:
            allsauce = int(allsauce)
        except ValueError:
            print('Invalid input')
            continue
        else:
            if allsauce <= 1:
                print('No need to randomize with only that many sauces to choose from')
                randsauce = '2'
                break
            elif allsauce > 10:
                print('That\'s too many sauces!')
                continue 
            else:
                break

if randsauce == '1':
    saucelist = []
    for iv12 in range(allsauce):
        print('Enter sauce number ' + str(iv12+1))
        while True:
            currsauce = input()
            if len(currsauce) > 50:
                print('Sauce name too long')
                continue
            elif currsauce in saucelist:
                print('You already have that sauce')
                continue
            else:
                saucelist += [currsauce]
                break

allpizzas = []

for iv2 in range(pizzas):
    pizzagen = []
    selectedtops = 0
    print('\nPizza #' + str(iv2+1))
    if randsauce == '1':
        print('[sauce = '  + saucelist[random.randint(0,allsauce-1)] + ']')
    while selectedtops < tops:
        temptop = toplist[random.randint(0,alltops-1)]
        if dupetops == '2' and temptop in pizzagen:
            continue
        else:
            pizzagen += [temptop]
            selectedtops += 1
    allpizzas += [pizzagen]
    for top in pizzagen:
        print(top)
