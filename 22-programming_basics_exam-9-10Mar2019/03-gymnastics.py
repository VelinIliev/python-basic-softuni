country = input()
instrument = input()

difficulty_rating = 0
execution_rating = 0

if country == "Russia":
    if instrument == "ribbon":
        difficulty_rating = 9.1
        execution_rating = 9.4
    elif instrument == "hoop":
        difficulty_rating = 9.3
        execution_rating = 9.8
    elif instrument == "rope":
        difficulty_rating = 9.6
        execution_rating = 9.0
elif country == "Bulgaria":
    if instrument == "ribbon":
        difficulty_rating = 9.6
        execution_rating = 9.4
    elif instrument == "hoop":
        difficulty_rating = 9.55
        execution_rating = 9.75
    elif instrument == "rope":
        difficulty_rating = 9.5
        execution_rating = 9.4
elif country == "Italy":
    if instrument == "ribbon":
        difficulty_rating = 9.2
        execution_rating = 9.5
    elif instrument == "hoop":
        difficulty_rating = 9.45
        execution_rating = 9.35
    elif instrument == "rope":
        difficulty_rating = 9.7
        execution_rating = 9.15

total_rating = difficulty_rating + execution_rating

print(f"The team of {country} get {total_rating:.3f} on {instrument}.")
print(f'{(1 - (total_rating / 20)) * 100:.2f}%')