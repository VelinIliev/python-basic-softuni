num_tabs_opend = int(input())
salary = float(input())

facebook = 150
instagram = 100
reddit = 50

for x in range(num_tabs_opend):
    tab = input()
    if tab == "Facebook":
        salary = salary - facebook
    elif tab == "Instagram":
        salary = salary - instagram
    elif tab == "Reddit":
        salary = salary - reddit

    if salary <= 0:
        print("You have lost your salary.")
        break

if salary > 0:
    print(int(salary))