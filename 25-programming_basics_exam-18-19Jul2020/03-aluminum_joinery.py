number_of_window_frames = int(input())
window_frame_size = input()
delivery = input()

window_frame_price = 0

if window_frame_size == "90X130":
    window_frame_price = 110
    if number_of_window_frames > 60:
        window_frame_price *= .92
    elif number_of_window_frames > 30:
        window_frame_price *= .95
elif window_frame_size == "100X150":
    window_frame_price = 140
    if number_of_window_frames > 80:
        window_frame_price *= .9
    elif number_of_window_frames > 40:
        window_frame_price *= .94
elif window_frame_size == "130X180":
    window_frame_price = 190
    if number_of_window_frames > 50:
        window_frame_price *= .88
    elif number_of_window_frames > 20:
        window_frame_price *= .93
elif window_frame_size == "200X300":
    window_frame_price = 250
    if number_of_window_frames > 50:
        window_frame_price *= .86
    elif number_of_window_frames > 25:
        window_frame_price *= .91

total = number_of_window_frames * window_frame_price

if delivery == "With delivery":
    total += 60

if number_of_window_frames > 99:
    total *= .96

if number_of_window_frames < 10:
    print(f'Invalid order')
else:
    print(f'{total:.2f} BGN')