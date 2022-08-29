months = int(input())

water_bill = 20
internet_bill = 15

electricity_bill_total = 0
water_bill_total = 0
internet_bill_total = 0
others_bills_total = 0

for month in range(months):
    new_electricity_bill = float(input())
    electricity_bill_total += new_electricity_bill
    water_bill_total += water_bill
    internet_bill_total += internet_bill
    others_bills_total += (new_electricity_bill + water_bill + internet_bill) * 1.2

print(f'Electricity: {electricity_bill_total:.2f} lv')
print(f'Water: {water_bill_total:.2f} lv')
print(f'Internet: {internet_bill_total:.2f} lv')
print(f'Other: {others_bills_total:.2f} lv')
total_bills = electricity_bill_total + water_bill_total + internet_bill_total + others_bills_total
print(f'Average: {total_bills / months :.2f} lv')