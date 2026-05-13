# test_uvicornasgi.py
"""
Tests for UvicornASGI module.
"""

import unittest
from uvicornasgi import UvicornASGI

class TestUvicornASGI(unittest.TestCase):
    """Test cases for UvicornASGI class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UvicornASGI()
        self.assertIsInstance(instance, UvicornASGI)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UvicornASGI()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
