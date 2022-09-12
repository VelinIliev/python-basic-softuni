desired_height = int(input())
starting_height = desired_height - 30
jumps_counter = 0

keep_trying = True

while keep_trying:
    attempt_counter = 0

    while attempt_counter < 4:
        attempt_height = int(input())
        jumps_counter += 1
        attempt_counter += 1
        if attempt_height > starting_height:
            if attempt_height > desired_height and starting_height == desired_height:
                print(f'Tihomir succeeded, he jumped over {starting_height}cm after {jumps_counter} jumps.')
                keep_trying = False
            starting_height += 5
            break
        elif attempt_height <= starting_height and attempt_counter == 3:
            print(f'Tihomir failed at {starting_height}cm after {jumps_counter} jumps.')
            keep_trying = False
            break
