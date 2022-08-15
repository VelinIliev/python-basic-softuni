protector_price = 1.50
paint_price = 14.50
thinner_price = 5

protector = int(input())
paint = int(input()) 
thinner = int(input())
hours = int(input())
bags = 0.4

protector += 2
paint += paint * 0.1

total_materials = protector*protector_price + paint*paint_price + thinner*thinner_price + bags

painters_price = total_materials*.3
sum_painters = painters_price * hours

total = total_materials + sum_painters

print(total)