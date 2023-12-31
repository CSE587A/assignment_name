import logging
import unittest
from gradescope_utils.autograder_utils.decorators import weight
from cse587Autils.configure_logging import configure_logging
from assignment_name.assignment import square

configure_logging(logging.WARN)


class Testassignment_name(unittest.TestCase):
    
    @weight(10)
    def test_square(self):
        
        # Test with an empty list
        with self.assertRaises(ValueError):
            square('two')
        
        self.assertEqual(square(2), 4)
