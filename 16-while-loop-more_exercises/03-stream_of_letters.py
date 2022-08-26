c_count = 0
o_count = 0
n_count = 0
word = ""

while True:
    symbol = input()
    if symbol == "End":
        break
    if chr(97) <= symbol <= chr(122) or chr(65) <= symbol <= chr(90):
        if symbol == "c" and c_count == 0:
            c_count += 1
        elif symbol == "o" and o_count == 0:
            o_count += 1
        elif symbol == "n" and n_count == 0:
            n_count += 1
        else:
            word += symbol
    if c_count + o_count + n_count == 3:
        print(f"{word}", end = " ")
        c_count = 0
        o_count = 0
        n_count = 0
        word = ""
