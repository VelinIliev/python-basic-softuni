town = input()
sels = float(input())

commission = -1

if sels > 10000:
    if town == "Sofia":
        commission = sels * .12
    elif town == "Varna":
        commission = sels * .13
    elif town == "Plovdiv":
        commission = sels * .145
elif sels > 1000:
    if town == "Sofia":
        commission = sels * .08
    elif town == "Varna":
        commission = sels * .10
    elif town == "Plovdiv":
        commission = sels * .12
elif sels > 500:
    if town == "Sofia":
        commission = sels * .07
    elif town == "Varna":
        commission = sels * .075
    elif town == "Plovdiv":
        commission = sels * .08
elif sels >= 0:
    if town == "Sofia":
        commission = sels * .05
    elif town == "Varna":
        commission = sels * .045
    elif town == "Plovdiv":
        commission = sels * .055

if commission >= 0:
    print(f'{commission:.2f}')
else:
    print("error")