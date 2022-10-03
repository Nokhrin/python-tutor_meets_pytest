"""
Дан список стран и городов каждой страны.
Затем даны названия городов.
Для каждого города укажите, в какой стране он находится.
"""

def get_country_for_city(input_count: str, country_cities: list, requests_count: str, request_cities: list) -> list:
    """
    Return country for requested city.

    :param input_count: number of input of country and it's cities
    :param country_cities: list of strings <country> <city 1> <city 2> ... <city N>
    :param requests_count: number of following requests
    :param request_cities: list of str requests as <city>
    :return: list of country names, one for each city request
    """
    # collect data for dictionary
    elements_count = int(input_count)
    countries_cities_dict = {}
    for i in range(elements_count):
        input_list = country_cities[i].split(sep=' ')
        countries_cities_dict[input_list[0]] = input_list[1:]

    # requests to dictionary
    requests_count = int(requests_count)
    countries_list = []
    for i in range(requests_count):
        city_to_search = request_cities[i]
        for country, cities in countries_cities_dict.items():
            if city_to_search in cities:
                countries_list.append(country)
    return countries_list
