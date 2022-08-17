product = input()
town = input()
quantity = float(input())

products = {
    "Sofia":
    {
        "coffee": .5,
        "water": .8,
        "beer": 1.2,
        "sweets": 1.45,
        "peanuts": 1.6
    },
    "Plovdiv":
    {
        "coffee": .4,
        "water": .7,
        "beer": 1.15,
        "sweets": 1.30,
        "peanuts": 1.50
    },
    "Varna":
    {
        "coffee": .45,
        "water": .70,
        "beer": 1.10,
        "sweets": 1.35,
        "peanuts": 1.55
    }
}
total = round(products[town][product] * quantity, 4)

print(total)