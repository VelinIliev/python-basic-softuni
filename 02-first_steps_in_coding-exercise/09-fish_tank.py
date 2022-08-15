length = int(input())
width = int(input())
height = int(input())
percent = float(input())/100

v = length * width * height
v_liters = v * .001

water_needed = v_liters - v_liters*percent

print(water_needed)