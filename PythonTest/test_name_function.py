import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
	"""Can we handle names such Janis_Joplin""" 
	# def test_first_last_name(self):
	# 	formatted_name = get_formatted_name('janis','joplin')
	# 	self.assertEqual(formatted_name,'Janis Joplin')
	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('simon','st','du')
		self.assertEqual(formatted_name,'Simon St Du')
unittest.main()