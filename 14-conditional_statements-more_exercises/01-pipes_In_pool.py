pool_volume = int(input())
pipe1_debit = int(input())
pipe2_debit = int(input())
worker_missing_hours = float(input())

pipe1 = pipe1_debit * worker_missing_hours
pipe2 = pipe2_debit * worker_missing_hours
pool_filled = pipe1 + pipe2

if pool_volume < pool_filled:
    print(f'For {worker_missing_hours:.2f} hours the pool overflows with {pool_filled - pool_volume:.2f} liters."')
else:
    print(f'The pool is {pool_filled / pool_volume * 100:.2f}% full. Pipe 1: {pipe1 / pool_filled * 100:.2f}%. Pipe 2: {pipe2 / pool_filled * 100:.2f}%.')