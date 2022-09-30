"""
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""

# collect data for dictionary
elements_count = int(input())
countries_cities_dict = {}
for i in range(elements_count):
    input_list = input().split(sep=' ')
    countries_cities_dict[input_list[0]] = input_list[1:]

# requests to dictionary
requests_count = int(input())
for i in range(requests_count):
    city_to_search = input()
    for country, cities in countries_cities_dict.items():
        if city_to_search in cities:
            print(country)

