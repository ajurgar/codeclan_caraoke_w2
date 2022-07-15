import unittest

from classes.song import Song

class TestSong (unittest.TestCase):

    def setUp(self):
        
        self.song = Song("Gecko")

    def test_song_has_name(self):

        self.assertEqual("Gecko", self.song.name)