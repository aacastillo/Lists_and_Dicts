
#Alan Castillo
#02/18/2021

#part 1
entreePrice = 27.38
drinkPrice = 3
dessertPrice = 11.20
mealsTax = 0.625
tipsPerccentage = 0.15
restaurantName = "110 Grill"
serverName = "Java"

print(restaurantName)
print("Your server was: " + str(serverName) + "\n")

print("Entrée:      $" + str(entreePrice))
print("Drink:       $" + str(drinkPrice))
print("Dessert:     $" + str(dessertPrice) + "\n")

subtotal = entreePrice + drinkPrice + dessertPrice
print("Subtotal:    $" + str(subtotal))

tax = round(subtotal * mealsTax, 2)
print("Tax:         $" + str(tax))

total = round(subtotal + tax, 2)
print("Total bill:  $" + str(total) +"\n")

tip = round(total * tipsPerccentage, 2)
print("Tip:         $" + str(tip))

paid = tip + total
print("Paid:        $" + str(paid))


#part2
#1. Create a list in Python with the following values ['Red',
#'Green', 'White', 'Black', 'Pink', 'Yellow'].
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

#a. print the first and last elements in the same line
print(colors[0], colors[-1])

#b. print the third letter of the third element
print(colors[2][2])

#c. print the last 3 letters of the last element
print(colors[-1][-3] + colors[-1][-2] + colors[-1][-1])

#2. Make a dictionary that stores the sales tax amounts from
#each New England state (Vermont, New Hampshire, Maine,
#Massachusetts, Connecticut, Rhode Island).
states =  {'Vermont':0.06, 'New Hampshire': 0, 'Maine':0.055,
'Massachusetts':0.0625, 'Connecticut':0.0635, 'Rhode Island':0.07}

#a. Make a list of 3 item prices.
itemPrices = [12, 75.30, 1.99]

#b. Print the total cost of the first item with Vermont sales tax.
print(itemPrices[0] * states['Vermont'] + itemPrices[0])

#c. Print the total cost of the second item with New Hampshire sales tax.
print(itemPrices[1] * states['New Hampshire'] + itemPrices[1])

#d. Print the total cost of the third item with Connecticut sales tax.
print(itemPrices[2] * states['Connecticut'] + itemPrices[2])


#Part 3
stud_db = {'course': {'students':[ 
    {'name': 'Mike', 'grades':
        { 'physics':70, 'history': 80, 'math': 80}}, 
    {'name': 'Yi', 'grades':
        {'physics': 90,'history': 70, 'math': 85}}, 
    {'name': 'Laura', 'grades': 
        {'physics': 80,'math':100}}]}}

#1. Print out Mike’s history grade.
print(stud_db['course']['students'][0]['grades']['history'])

#2. Add another student to the database who is taking history and math.
Alan = {'name':'Alan', 'grades':{'history': 99, 'math':89}}
stud_db['course']['students'].append(Alan)

#3. Print out the names of all students.
for student in stud_db['course']['students']:
    print(student['name'])