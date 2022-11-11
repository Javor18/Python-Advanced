number_of_usernames = int(input())

unique_usernames = []

for i in range(number_of_usernames):

    username = input()

    if username not in unique_usernames:

        unique_usernames.append(username)

for username in unique_usernames:

    print(username)