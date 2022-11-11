from collections import deque

males = deque(int(x) for x in input().split())
females = deque(int(x) for x in input().split())

matches = 0

while males and females:

    female_value = females.popleft()
    male_value = males.pop()

    # if female_value <= 0 or male_value <= 0:
    #
    #     if female_value <= 0:
    #         males.append(male_value)
    #     else:
    #         females.appendleft(female_value)
    #
    #     continue

    if female_value <= 0:
        males.append(male_value)
        continue

    if male_value <= 0:
        females.appendleft(female_value)
        continue

    #
    # if female_value % 25 == 0 or male_value == 0:
    #
    #     if female_value % 25 == 0:
    #
    #         females.popleft()
    #
    #     if male_value % 25 == 0:
    #
    #         males.pop()
    #
    #     continue

    if female_value % 25 == 0:

        females.popleft()
        continue

    if male_value % 25 == 0:
        males.pop()
        continue

    if female_value == male_value:

        matches += 1

    else:
        male_value -= 2
        males.appendleft(male_value)



print(f"Matches: {matches}")

if males:

    print(f"Males left: {', '.join(str(x) for x in males)}")

else:

    print("Males left: none")

if females:

    print(f"Females left: {', '.join(str(x) for x in females)}")

else:

    print("Females left: none")

# males = deque(int(x) for x in input().split())
# females = deque(int(x) for x in input().split())
#
# matches = 0
#
# while males and females:
#
#     female_value = females.popleft()
#     male_value = males.pop()
#
#     if female_value <= 0 or male_value <= 0:
#
#         if female_value <= 0:
#             males.append(male_value)
#         else:
#             females.appendleft(female_value)
#
#         continue
#
#     if female_value / 25 == 0:
#
#         females.popleft()
#
#     if male_value / 25 == 0:
#
#         males.pop()
#
#     if female_value != male_value:
#
#         male_value -= 2
#         males.appendleft(male_value)
#
#     else:
#
#         matches += 1
#
# print(f"Matches: {matches}")
#
# if not males:
#
#     print("Males left: none")
#
# else:
#
#     print(f"Males left: {', '.join(str(x) for x in males)}")
#
# if not females:
#
#     print("Females left: none")
#
# else:
#
#     print(f"Females left: {', '.join(str(x) for x in females)}")