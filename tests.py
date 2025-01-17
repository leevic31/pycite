"""
pycite's unittests
Author: Nelson Gonzabato
Free Open Source Software
Free and always will be.
"""

import unittest
import os
from pycite.pycite import PyCite

# Make paths to tests

test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "testfiles")

txt_file = os.path.join(test_dir, "testlinks.txt")


class Testpycite(unittest.TestCase):

    def test_pycite(self):
        # Create an object of class PyCite
        test_object = PyCite(txt_file)
        self.assertTrue(isinstance(test_object, PyCite))
        # Check that we have two authors lists for two links
        citations = test_object.cite()
        self.assertEqual(len(citations), 2)


if __name__ == "__main__":
    unittest.main()
