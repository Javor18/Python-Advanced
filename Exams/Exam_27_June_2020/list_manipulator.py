def list_manipulator(list, *args):

    if args[0] == "remove":

        if args[1] == "end":

            if len(args) > 2:

                num = args[2]

                return list[:-num]

            else:
                return list[:-1]

        elif args[1] == "beginning":

            if len(args) > 2:

                num = args[2]

                return list[num:]

            else:
                return list[1:]



    elif args[0] == "add":

        if args[1] == "end":

            for num in args[2::]:
                list.append(num)

            return list

        elif args[1] == "beginning":

            old_list = []
            new_list = []

            for num in list:
                old_list.append(num)

            for num in args[2:]:
                new_list.append(num)

            for num in old_list:
                new_list.append(num)

            return new_list

print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))