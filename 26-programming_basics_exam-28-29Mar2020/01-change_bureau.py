bitcoins = int(input())
chinese_uan = float(input())
commission = float(input())

bitcoin_exchange = 1168
chinese_uan_to_usd = .15
usd = 1.76
euro = 1.95

chinese_uan_exchange = usd * chinese_uan_to_usd

total_bitcoins = bitcoins * bitcoin_exchange
total_chinese_uan = chinese_uan * chinese_uan_exchange
total = total_bitcoins + total_chinese_uan
total_in_euro = total / euro
commission_total = total_in_euro * commission / 100

money_to_receive = total_in_euro - commission_total

print(f'{money_to_receive:.2f}')

