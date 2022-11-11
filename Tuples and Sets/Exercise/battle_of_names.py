n = int(input())

odd_set = set()

even_set = set()

for row in range(1, n + 1):

    name = input()

    current_sum = sum([ord(el) for el in name]) // row

    if current_sum % 2 == 0:

        even_set.add(current_sum)

    else:

        odd_set.add(current_sum)

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)

even_set = {str(i) for i in even_set}
odd_set = {str(i) for i in odd_set}

if sum_even_set == sum_odd_set:

    modified_set = [str(el) for el in even_set.union(odd_set)]

    print(f"{', '.join(modified_set)}")

elif sum_odd_set > sum_even_set:

    modified_set = [str(el) for el in odd_set.difference(even_set)]

    print(f"{', '.join(modified_set)}")

else:

   modified_set = [str(el) for el in even_set.symmetric_difference(odd_set)]

   print(f"{', '.join(modified_set)}")