def get_city_country(city, country, population = ""):
    """ generate a 'City, Country' string, like 'Shantou, China' """
    
    if population == "":
        city_country = city + ", " + country

        return city_country.title()
    else:
        city_country_population = city + ", " + country + "-population" + population

        return city_country_population.title()