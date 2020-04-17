def get_city_country(city, country, population):
    """ generate a 'City, Country' string, like 'Shantou, China' """
    city_country_population = city + ", " + country + "-population" + population

    return city_country_population.title()