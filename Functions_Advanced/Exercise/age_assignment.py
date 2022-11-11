def age_assignment(*args, **kwargs):

    people = {}

    result = ''

    for key, value in kwargs.items():

        for name in args:

            if key == name[0]:

                people[name] = value

    sorted_people = dict(sorted(people.items(), key = lambda x : x[0] ))

    for name, age in sorted_people.items():

        result += f"{name} is {age} years old." + '\n'

    return result

# print(age_assignment("Peter", "George", G=26, P=19))

print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))