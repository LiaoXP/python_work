import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """ test name_function.py """
    def test_first_last_name(self):
        """ can process name like 'Janis Joplin'? """
        formatted_name = get_formatted_name("janis", "joplin")

        self.assertEqual(formatted_name, "Janis Joplin")

unittest.main()