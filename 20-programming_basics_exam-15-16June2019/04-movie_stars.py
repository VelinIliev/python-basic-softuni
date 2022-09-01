budget_for_actors = float(input())
rest_of_budget = budget_for_actors

while True:
    actor_name = input()

    if actor_name == "ACTION":
        print(f'We are left with {rest_of_budget:.2f} leva.')
        break

    if len(actor_name) > 15:
        actor_pay = rest_of_budget * .2
        rest_of_budget -= actor_pay
    else:
        actor_pay = float(input())
        rest_of_budget -= actor_pay

    if rest_of_budget < 0:
        print(f'We need {abs(rest_of_budget):.2f} leva for our actors.')
        break


