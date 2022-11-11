def operate(operator, *args):

    if operator == "+":

        return  sum(args)

    elif operator == "*":
        result = 1

        for num in args:

            result *= num

        return result

    # elif operator == "-":
    #
    #     result = 0
    #
    #     for num in args:
    #
    #         result -= num
    #
    #     return result
    #
    # elif operator == "/":
    #
    #     result = 1
    #
    #     for num in args:
    #
    #         result /= num
    #
    #     return result


# print(operate("+", 1, 2, 3))

print(operate("*", 3, 4))