pencils = int(input())
markers = int(input())
detergent = int(input())
discount = int(input())/100

pencils_price = 5.80
markers_price = 7.20
detergent_price = 1.2

sum_pencils = pencils * pencils_price
sum_markers = markers * markers_price
sum_detergent = detergent * detergent_price

total = (sum_pencils + sum_markers + sum_detergent) - (sum_pencils + sum_markers + sum_detergent) * discount

print(total)