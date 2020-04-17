import unittest
from city_functions import get_city_country

class test_cities(unittest.TestCase):
    def test_city_country(self):
        city_country = get_city_country("shantou", "china")

        self.assertEqual(city_country, "Shantou, China")

unittest.main()

