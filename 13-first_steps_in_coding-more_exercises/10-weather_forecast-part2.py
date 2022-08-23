celsius = float(input())

if celsius >= 5 and celsius <= 11.9:
    print("Cold")
elif celsius >= 12 and celsius <= 14.9:
    print("Cool")
elif celsius >= 15 and celsius <= 20:
    print("Mild")
elif celsius >= 20.1 and celsius <= 25.9:
    print("Warm")
elif celsius >= 26 and celsius <= 35:
    print("Hot")
else:
    print("unknown")