deposit_sum = float(input())
deposit_period = int(input())
deposit_rate = float(input()) / 100

sum = deposit_sum + deposit_period * ((deposit_sum * deposit_rate) / 12)
print(sum)