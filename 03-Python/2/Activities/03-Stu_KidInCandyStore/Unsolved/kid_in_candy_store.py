# The list of candies to print to the screen
candyList = ["Snickers", "Kit Kat", "Sour Patch Kids", "Juicy Fruit", "Swedish Fish",
             "Skittles", "Hershey Bar", "Skittles", "Starbursts", "M&Ms"]

# The amount of candy the user will be allowed to choose
allowance = 5

# The list used to store all of the candies selected inside of
candyCart = []

for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy)

for runtime in range(allowance):
    number_selection = input("Enter a number from 0 to 9 for candy selection.")
    number_selection = int(number_selection)
    #print(type(number_selection))
    candy_selection = candyList[number_selection]
    #print(candy_selection)
    candyCart.append(candy_selection)


print(candyCart)

