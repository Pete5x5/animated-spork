import random   #Enable random number functionality
print('''RANDOM PIZZA GENERATOR
As the dice will it, it shall be done

How many pizzas would you like generated?''')

while True: #Get number of pizzas to be generated
    pizzas = input()
    try:    #Make sure input is an int
         pizzas = int(pizzas)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if pizzas < 1:  #Can't generate 0 pizzas..
            print('Not enough pizzas')
            continue
        elif pizzas > 12:   #Cap on number of pizzas
            print('That\'s too many pizzas!')
            continue
        else:
            break
        
print('How many toppings are there per pizza?')
while True: #Get number of toppings per pizza
    tops = input()
    try:    #Make sure input is an int
         tops = int(tops)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if tops <= 1:   #Can't have less than 1 topping
            print('Not enough toppings')
            continue
        elif tops > 12: #Cap on number of toppings
            print('That\'s too many toppings!')
            continue 
        else:
            break

print('How many toppings are there to choose from?')
while True: #Get total number of toppings to choose from
    alltops = input()
    try:    #Make sure input is an int
         alltops = int(alltops)
    except ValueError:
        print('Invalid input')
        continue
    else:
        if alltops <= 1:    #Can't have less than 1 topping
            print('Not enough toppings')
            continue
        elif alltops > 99:  #Cap on number of toppings
            print('That\'s too many toppings!')
            continue 
        else:
            break

toplist = []    #Set the variable type to list

def topname():  #Function to get all possible toppings
    global toplist #Use the global version of toplist (above)
    while True:
            currtop = input()
            if len(currtop) > 50:   #Cap on number of characters in topping name
                print('Topping name too long')
                continue
            elif currtop in toplist:    #Check for duplicate toppings in list
                print('You already have that topping')
                continue
            else:
                toplist += [currtop] #Add the topping to the list
                break

for iv1 in range(alltops): #User will enter all possible toppings
    print('Enter topping number ' + str(iv1+1)) #Var starts counting at 0 so must add 1
    topname()   #Function on line 62

listcorrect = 0

while listcorrect < 1:  #Check topping list
    print ("\nIs this topping list correct?")
    for iv112 in range(len(toplist)):
        print (str(iv112+1) + " - " + str(toplist[iv112]))  #Print the topping list to be checked
    print('''
    a - Yes, that's perfect
    b - I need to add a topping
    c - I need to remove a topping\n''')
    while True:
        listconfirm = input()
        if listconfirm == 'a':  #List is OK, move on
            listcorrect = 1
            break
        elif listconfirm == 'b':  #Get additional topping
            print('Please enter the additional topping now:')
            topname()   #Function on line 62
            break
        elif listconfirm == 'c':
            removetop = 0
            print('Which topping number would you like to remove?')
            while True:
                removetop = input()
                try:
                    removetop = int(removetop)
                except ValueError:
                    print('Invalid input')
                    continue
                else:
                    if removetop < 1 or removetop > len(toplist):
                        print('Invalid input')
                        continue
                    else:
                        break
            del toplist[removetop - 1]
            break
        else:
            print('Invalid choice')
            continue

alltops = len(toplist)

if alltops >= tops:
    print('''\nWould you like to allow duplicate toppings?
        a - Yes, that is how the dice will it
        b - No, triple olives is gross\n''')

    while True:
        dupetops = input()
        if dupetops == 'a' or dupetops == 'b':
            break
        else:
            print('Invalid choice')
            continue
else:
    dupetops == 'a'

print('''Would you like to randomize the type of sauce for each pizza?
    a - Yes, true random is the only way
    b - No, I can only handle regular pizza sauce\n''')

while True:
    randsauce = input()
    if randsauce == 'a' or randsauce == 'b':
        break
    else:
        print('Invalid choice')
        continue

if randsauce == 'a':
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

if randsauce == 'a':
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

allpizzas = []  #For later use (saving generated pizzas to file)

for iv2 in range(pizzas):
    pizzagen = []
    selectedtops = 0
    print('\nPizza #' + str(iv2+1))
    if randsauce == 'a':
        print('[sauce = '  + saucelist[random.randint(0,allsauce-1)] + ']')
    while selectedtops < tops:
        temptop = toplist[random.randint(0,alltops-1)]
        if dupetops == 'b' and temptop in pizzagen:
            continue
        else:
            pizzagen += [temptop]
            selectedtops += 1
    allpizzas += [pizzagen] #For later use
    for top in pizzagen:
        print(top)
