
numbers = [int(x) for x in input().split()]

negative_numbers = []
positive_numbers = []

for number in numbers:

    if number < 0:

        negative_numbers.append(number)

    else:

        positive_numbers.append(number)

sum_positives = sum(positive_numbers)

sum_negatives = sum(negative_numbers)

print(sum_negatives)
print(sum_positives)

if abs(sum_negatives) > sum_positives:

    print("The negatives are stronger than the positives")

else:

    print("The positives are stronger than the negatives")