def even_odd(*args):

    if "even" in args:

        numbers = [int(x) for x in args[:len(args) - 1] if x % 2 == 0]

    elif "odd" in args:

        numbers = [int(x) for x in args[:len(args) - 1] if x % 2 != 0]

    return numbers

# print(even_odd(1, 2, 3, 4, 5, 6, "even"))

print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))