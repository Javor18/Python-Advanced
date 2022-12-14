# from collections import deque
#
# materials = [int(x) for x in input().split()]
# magic_levels = deque(int(x) for x in input().split())
#
# gifts = {
#     'Diamond Jewellery': 0,
#     'Gemstone': 0,
#     'Gold': 0,
#     'Porcelain Sculpture': 0
# }
#
#
# def under_100(material, magic_level):
#
#     if total_sum % 2 == 0:
#         new_mix = (material * 2) + (magic_level * 3)
#
#     else:
#         new_mix = (material + magic_level) * 2
#
#     return new_mix
#
#
# while materials and magic_levels:
#
#     material = materials.pop()
#     magic_level = magic_levels.popleft()
#     total_sum = material + magic_level
#
#     if total_sum < 100:
#         total_sum = under_100(material, magic_level)
#
#     if total_sum > 499:
#         total_sum /= 2
#
#     if 100 <= total_sum <= 199:
#
#         gifts['Gemstone'] += 1
#
#     elif 200 <= total_sum <= 299:
#
#         gifts['Porcelain Sculpture'] += 1
#
#     elif 300 <= total_sum <= 399:
#
#         gifts['Gold'] += 1
#
#     elif 400 <= total_sum <= 499:
#
#         gifts['Diamond Jewellery'] += 1
#
#
# if (gifts['Gemstone'] > 0 and gifts['Porcelain Sculpture'] > 0) or \
#     gifts['Gold'] > 0 and gifts['Diamond Jewellery'] > 0:
#
#     print("The wedding presents are made!")
#
# else:
#     print("Aladdin does not have enough wedding presents.")
#
# if materials:
#
#     print(f"Materials left: {', '.join(str(x) for x in materials)}")
#
# if magic_levels:
#
#     print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")
#
# for present, quantity in gifts.items():
#     #key, value
#
#     if quantity:
#
#         print(f"{present}: {quantity}")


from collections import deque

materials = deque(int(x) for x in input().split())
magic_levels = deque(int(x) for x in input().split())

gemstones = 0
porcelain_sculptures = 0
gold = 0
diamond_jewelleries = 0

while materials and magic_levels:

    material = materials.pop()
    magic = magic_levels.popleft()

    value = material + magic

    if value < 100:

        if value % 2 == 0:

            material *= 2
            magic *= 3
            value = material + magic

        else:
            value *= 2

    elif value > 499:

        value //=2

    if 100 <= value <= 199:

        gemstones += 1

    elif 200 <= value <= 299:

        porcelain_sculptures += 1

    elif 300 <= value <= 399:

        gold += 1

    elif 400 <= value <= 499:

        diamond_jewelleries += 1

if gemstones >= 1 and porcelain_sculptures >= 1 or gold >= 1 and diamond_jewelleries >= 1:

    print("The wedding presents are made!")

else:

    print("Aladdin does not have enough wedding presents.")

if materials:

    print(f"Materials left: {', '.join(str(x) for x in materials)}")

if magic_levels:

    print(f"Magic left: {', '.join(str(x) for x in magic_levels)}")

if diamond_jewelleries:

    print(f'Diamond Jewellery: {diamond_jewelleries}')

if gemstones:

    print(f'Gemstone: {gemstones}')

if gold:

    print(f'Gold: {gold}')

if porcelain_sculptures:

    print(f'Porcelain Sculpture: {porcelain_sculptures}')