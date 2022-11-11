def even_odd_filter(**kwargs):

    if 'even' in kwargs.keys():
        kwargs['even'] = [int(x) for x in kwargs['even'] if x % 2 == 0]

    if 'odd' in kwargs.keys():

        kwargs['odd'] = [int(x) for x in kwargs['odd'] if x % 2 != 0]

    return kwargs

# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
