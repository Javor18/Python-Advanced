# main_string = input()
#
# my_dict = {}
#
# for char in main_string:
#
#     if char in my_dict.keys():
#
#         my_dict[char] += 1
#
#     else:
#
#         my_dict[char] = 1
#
# for key, count in my_dict.items():
#
#     print(f"{key}: {count} time/s")


chars = input()

my_dict = {}

for char in chars:

    if char in my_dict.keys():

        my_dict[char] += 1

    else:
        my_dict[char] = 1

for key, value in my_dict.items():

    print(f"{key}: {value} time/s")