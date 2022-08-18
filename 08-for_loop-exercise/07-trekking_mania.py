iterations = int(input())

peoples_to_musala = 0
peoples_to_monblan = 0
peoples_to_kilimandjaro = 0
peoples_to_k2 = 0
peoples_to_everest = 0

peoples_total = 0

for x in range(iterations):
    number_of_people = int(input())
    peoples_total += number_of_people
    if number_of_people <= 5:
        peoples_to_musala += number_of_people
    elif number_of_people <= 12:
        peoples_to_monblan += number_of_people
    elif number_of_people <= 25:
        peoples_to_kilimandjaro += number_of_people
    elif number_of_people <= 40:
        peoples_to_k2 += number_of_people
    else:
        peoples_to_everest += number_of_people

print(f'{((peoples_to_musala / peoples_total) * 100):.2f}%')
print(f'{((peoples_to_monblan / peoples_total) * 100):.2f}%')
print(f'{((peoples_to_kilimandjaro / peoples_total) * 100):.2f}%')
print(f'{((peoples_to_k2 / peoples_total) * 100):.2f}%')
print(f'{((peoples_to_everest / peoples_total) * 100):.2f}%')