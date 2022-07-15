import unittest

from classes.guest import Guest

class TestGuest (unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Michael", "Let It Be")
    
    def test_guest_has_name(self):
        self.assertEqual("Michael", self.guest.name)
    
    def test_guest_has_favourite_song(self):
        # self.favourite_song = "Let It Be"
        self.assertEqual("Let It Be", self.guest.favourite_song)