# Tip_calculator
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
num_of_split = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))

amount = round((bill/num_of_split)*(1+tip/100), 2)

print("Each person should pay: ${}".format(str(amount)))


# Type conversiont
num = input("Type a two digit number: ")
(first, second) = (int(num[0]), int(num[1]))
print(first+second)