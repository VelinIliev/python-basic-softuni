user_name = input()
password = input()

true_password = False

while not true_password:
    user_try = input()
    if user_try == password:
        true_password = True
        print(f'Welcome {user_name}!')