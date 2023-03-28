customer = str(input("Customer's Name:"))
print ("Welcome to our store")
print ("This is our products")
print ("Orange 0.5$")
print ("Apple 1$")
print ("Grape 0.5$")
print ("Banana 0.5$")
prices = {"orange":0.5,"apple":1,"grape":0.5,"banana":0.5}# I added this so we can access the prices later on
#chooseproducts= int(input("What do you want to buy: "))
# The code below this is what I added to calculate the cost.
productnum = input("How many things do you want to buy: ") # This is for finding the number of different fruits the buyer wants
while not productnum.isdigit():
    productnum = input("How many different products do you want to buy: ")
productnum = int(productnum)
totalprice = 0
totalfruit = 0
print('         BILL')
for i in range(productnum):
    chosenproduct = input("What do you want to buy: ").lower()
    while not chosenproduct in ['orange','apple','banana','grape']:
        chosenproduct = input("What do you want to buy: ").lower()
    fruitnum = input("How many of that do you want to buy: ")
    while not fruitnum.isdigit():
        fruitnum = input("How many of that do you want to buy: ")
    fruitnum = int(fruitnum)
    totalfruit += fruitnum
    price = fruitnum * prices[chosenproduct]
    totalprice += price
    startspaces = ' ' * (11 - len(chosenproduct))
    endspaces = ' ' * (5 - len(str(fruitnum)))
    print(chosenproduct.capitalize() + startspaces + str(fruitnum) + endspaces + str(price) + '$')

print('Total:     ' + str(totalfruit) + ' ' * (5 - len(str(totalprice))) + str(totalprice) + '$')