company_name = input()
adult_tickets_number = int(input())
kid_tickets_number = int(input())
net_ticket_price = float(input())
service_fee = float(input())

adult_ticket_price = net_ticket_price + service_fee
kid_ticket_price = net_ticket_price * .3 + service_fee

total_adults = adult_tickets_number * adult_ticket_price
total_kids = kid_tickets_number * kid_ticket_price

total_income = total_adults + total_kids

profit = total_income * .2

print(f'The profit of your agency from {company_name} tickets is {profit:.2f} lv.')