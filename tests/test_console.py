import unittest
import sys
import io
from unittest.mock import patch
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


class Test_HBNBCommand(unittest.TestCase):
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
        """Unittests for testing the do_create
        method of the HBNBCommand class"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            output = f.getvalue().strip()
            self.assertNotEqual(output, "")

    def test_do_create_with_invalid_class(self):
        """Unittests for testing the do_create method of
        the HBNBCommand class with non existing class"""
        msg = "** class doesn't exist **"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create InvalidClass")
            output = f.getvalue().strip()
            self.assertEqual(output, msg)

    def test_do_create_without_args(self):
        """Unittests for testing the do_create method
        of the HBNBCommand class with missing class name"""
        msg = "** class name missing **"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("create ")
            output = f.getvalue().strip()
            self.assertEqual(output, msg)

    def test_do_quit(self):
        """Unittests for testing the do_quit method of the HBNBCommand class"""
        with patch('sys.stdout', new=io.StringIO()) as f:
            self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_help_quit(self):
        """Unittests for testing the help_quit
        method of the HBNBCommand class"""
        msg = "Exits the program with formatting\n\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help quit")
            output = f.getvalue()
            self.assertEqual(output, msg)

    def test_do_EOF(self):
        """Unittests for testing the do_EOF method of the HBNBCommand class"""
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    def test_help_EOF(self):
        """Unittests for testing the help_EOF method
        of the HBNBCommand class"""
        msg = "Exits the program without formatting\n\n"
        with patch('sys.stdout', new=io.StringIO()) as f:
            HBNBCommand().onecmd("help EOF")
            output = f.getvalue()
            self.assertEqual(output, msg)


if __name__ == '__main__':
    unittest.main()
