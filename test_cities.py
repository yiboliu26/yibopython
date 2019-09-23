import unittest
from city_functions import city_country

class Test_citycountry(unittest.TestCase):
    def test_city_country(self):
        format = city_country('santiago', 'chile')
        self.assertEqual(format, 'Santiago, Chile')
    def test_city_country_population(self):
        format = city_country('santiago', 'chile', population = 5000000)
        self.assertEqual(format, 'Santiago, Chile - Population 5000000')
unittest.main()
