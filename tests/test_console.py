import unittest
import sys
from io import StringIO
from console import HBNBCommand
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class TestHBNBCommand(unittest.TestCase):
    """Unittest Cases for the HBNBCommand class"""

    @classmethod
    def setUp(self):
        """Setting up necessary resources for the test"""
        self.hbnb = HBNBCommand()
        self.io_capture = StringIO()
        sys.stdout = self.io_capture

    @classmethod
    def tearDown(self):
        """Frees up resources after the test is done"""
        sys.stdout = sys.__stdout__
   
    def test_do_create(self):
        """Unittests for testing the do_create method of the HBNBCommand class"""
        self.hbnb.do_create("BaseModel")
        self.assertNotEqual(sys.stdout.getvalue().strip(), "")

    def test_do_create_with_invalid_class(self):
        """Unittests for testing the do_create method of the HBNBCommand class with non existing class"""
        self.hbnb.do_create("InvalidClass")
        self.assertEqual(sys.stdout.getvalue().strip(), "** class doesn't exist **")

    def test_do_create_without_args(self):
        """Unittests for testing the do_create method of the HBNBCommand class with missing class name"""
        self.hbnb.do_create("")
        self.assertEqual(sys.stdout.getvalue().strip(), "** class name missing **")

    def test_do_create_invalid_class(self):
        """Unittests for testing the do_create method of the HBNBCommand class with invalid class name"""
        self.hbnb.do_create("InvalidClass")
        self.assertEqual(sys.stdout.getvalue().strip(), "** class doesn't exist **")
    
    def test_do_quit(self):
        """Unittests for testing the do_quit method of the HBNBCommand class"""
        self.assertTrue(self.hbnb.do_quit(""))

    def test_help_quit(self):
        """Unittests for testing the help_quit method of the HBNBCommand class"""
        msg = "Exits the program with formatting\n\n"
        result = self.hbnb.help_quit()
        self.assertEqual(sys.stdout.getvalue(), msg)
    
    def test_do_EOF(self):
        """Unittests for testing the do_EOF method of the HBNBCommand class"""
        self.assertTrue(self.hbnb.do_EOF(""))

    def test_help_EOF(self):
        """Unittests for testing the help_EOF method of the HBNBCommand class"""
        msg = "Exits the program without formatting\n\n"
        result = self.hbnb.help_EOF()
        self.assertEqual(sys.stdout.getvalue(), msg)
    
    def test_preloop(self):
        """Unittests for testing the preloop method of the HBNBCommand class"""
        sys.__stdin__ = StringIO("")
        self.hbnb.preloop()
        self.assertEqual(sys.stdout.getvalue().strip(), "(hbnb)")


if __name__ == '__main__':
    unittest.main()
