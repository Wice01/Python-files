def print_alphabet(first, last):
    b = ""
    while b != chr(last):
        b = chr(first)
        first = first + 1
        print(b, end="")
