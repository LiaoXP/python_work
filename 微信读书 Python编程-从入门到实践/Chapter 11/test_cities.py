import unittest
from city_functions import get_city_country

class test_cities(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country("shantou", "china")

        self.assertEqual(city_country, "Shantou, China")
    def test_city_country_population(self):
        city_country_population = get_city_country("shantou", "china", "5000000")

        self.assertEqual(city_country_population, "Shantou, China-Population5000000")
unittest.main()

