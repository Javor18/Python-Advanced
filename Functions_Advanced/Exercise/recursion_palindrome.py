def palindrome(*args):

    word = args[0]

    new_word = word[::-1]

    if word == new_word:

        return f"{word} is a palindrome"

    else:

        return f"{word} is not a palindrome"

# print(palindrome("abcba", 0))

print(palindrome("peter", 0))