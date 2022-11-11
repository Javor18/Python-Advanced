def rectangle(length, width):

    if not ( isinstance(length, int) and isinstance(width, int) ):

        return "Enter valid values!"


    def area():

        return f"Rectangle area: {width * length}"

    def perimeter():

        return f"Rectangle perimeter: {width * 2 + length * 2}"

    return area() + "\n" + perimeter()

print(rectangle(2, 10))