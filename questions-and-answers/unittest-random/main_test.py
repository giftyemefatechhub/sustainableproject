#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit testing."""

import unittest
import main


class TestSomeClass(unittest.TestCase):
    """Test the class."""

    def test_check_without_randomize(self):
        """Verify that the exception is raised."""
        obj = main.SomeClass()
        with self.assertRaises(Exception):
            obj.check_number()

    def test_check_number_being_13(self):
        """Verify that the exception is raised."""
        obj = main.SomeClass()
        obj.randomize_number()
        obj.magic_number = 13
        with self.assertRaises(ValueError):
            obj.check_number()

    def test_check_number_not_being_13(self):
        """Verify that the code works."""
        obj = main.SomeClass()
        obj.randomize_number()
        obj.magic_number = 42
        obj.check_number()
