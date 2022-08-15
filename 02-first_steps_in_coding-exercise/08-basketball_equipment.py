training_price = int(input())

sneakers_price = training_price - training_price * .4
outfit_price = sneakers_price - sneakers_price * .2
ball_price = outfit_price / 4
accessoires_price = ball_price / 5

total = training_price + sneakers_price + outfit_price + ball_price + accessoires_price

print(total)