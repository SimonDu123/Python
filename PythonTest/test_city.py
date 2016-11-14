import unittest
from city_functions import get_city_country
class CityTestCase(unittest.TestCase):
	"""docstring for TestCity"""
	def test_city_country(self):
		city_country = get_city_country('zhuhai','china','1.3B')
		self.assertEqual(city_country,'Zhuhai,China - population 1.3B')
		city_country_no_pop = get_city_country('zhongshan','china')
		self.assertEqual(city_country_no_pop,'Zhongshan,China')
unittest.main()