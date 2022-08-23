skumria_price_per_kg = float(input())
caca_price_per_kg = float(input())
palamud_kilograms = float(input())
safrid_kilograms = float(input())
midi_kilograms = int(input())

palamud_price_per_kg = skumria_price_per_kg * 1.6
safrid_price_per_kg = caca_price_per_kg * 1.8
midi_price_per_kg = 7.5

total_palamud = palamud_kilograms * palamud_price_per_kg
total_safrid = safrid_kilograms * safrid_price_per_kg
total_midi = midi_kilograms * midi_price_per_kg

total = total_palamud + total_safrid + total_midi

print(f'{total:.2f}')