number_of_element = int(input())

unique_elements = set()

for i in range(number_of_element):

    chemical_elements = input().split()

    for chemical_element in chemical_elements:

        if chemical_element not in unique_elements:

            unique_elements.add(chemical_element)


for chemical_element in unique_elements:
    print(chemical_element)