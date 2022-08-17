product = input()
day = input()
quantity = float(input())

prices = {
    "working_days": {
        "banana": 2.5,
        "apple": 1.2,
        "orange": .85,
        "grapefruit": 1.45,
        "kiwi": 2.7,
        "pineapple": 5.5,
        "grapes": 3.85
    },
    "weekends": {
        "banana": 2.7,
        "apple": 1.25,
        "orange": .90,
        "grapefruit": 1.60,
        "kiwi": 3.00,
        "pineapple": 5.6,
        "grapes": 4.20
    },
}
working_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekends = ["Saturday", "Sunday"]



if day in working_days and product in prices["working_days"]:
    price = round(prices["working_days"][product] * quantity, 2)
    print(f'{price:.2f}')
elif day in weekends and product in prices["weekends"]:
    price = round(prices["weekends"][product] * quantity, 2)
    print(f'{price:.2f}')
else:
    print("error")