def forecast(*args):

    output, result = "", {"Sunny": [], "Cloudy": [], "Rainy": []}

    for line in args:

        location, weather = line

        if location not in result[weather]:

            result[weather].append(location)

    for s_weather in result:

        if len(result[s_weather]) > 0:

            for city in sorted(result[s_weather]):

                output += f"{city} - {s_weather}\n"

    return output

# print(forecast(
#     ("Sofia", "Sunny"),
#     ("London", "Cloudy"),
#     ("New York", "Sunny")))


# print(forecast(
#     ("Beijing", "Sunny"),
#     ("Hong Kong", "Rainy"),
#     ("Tokyo", "Sunny"),
#     ("Sofia", "Cloudy"),
#     ("Peru", "Sunny"),
#     ("Florence", "Cloudy"),
#     ("Bourgas", "Sunny")))


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
