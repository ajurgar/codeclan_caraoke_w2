import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        
        self.song1 = Song("Let It Be")
        self.song2 = Song("Gecko")
        self.song3 = Song("Despacito")

        self.room = Room("Rock", 500)

        self.guest1 = Guest("Michael", "Let It Be", 50)
        self.guest2 = Guest("Alex", "Gecko", 40)
        self.guest3 = Guest("Sandy", "Despacito", 10)

        self.guest_list = [self.guest1, self.guest2, self.guest3]
        

        self.playlist = [self.song1, self.song2, self.song3]


    def test_room_has_name(self):
        self.assertEqual("Rock", self.room.name)
    
    def test_room_has_capacity(self):
        self.assertEqual(100, self.room.capacity)
    
    def test_check_in_guest_to_room(self):
        self.room.add_guest(self.guest)
        self.assertEqual(1, self.room.checked_in())

    def test_check_in_guest_to_room(self):
        self.room.checked_in(self.guest)
        self.assertEqual(1, self.room.guest_count())

    def test_check_out_guest_to_room(self):
        self.room.checked_in(self.guest)
        self.room.checked_out()
        self.assertEqual(0, self.room.guest_count())
    
    def test_add_songs_to_room(self):
        self.room.add_song(self.song1.name)
        self.assertEqual(["Let It Be"], self.room.playlist)
        self.assertEqual(1, len(self.room.playlist))
    
    def test_limit_of_guest_check_ins(self):
        self.room.add_guest(self.guest1)
        self.room.add_guest(self.guest2)
        self.assertEqual(True, room.limit_entry())
    
    
    # def test_pub_cannot_serve_drink(self):
    #     self.pub.add_drink(self.drink_1)
    #     self.pub.add_drink(self.drink_2)
    #     self.pub.serve(self.customer_1, self.drink_1)
    #     self.assertEqual(8.00, self.customer_1.wallet)
    #     self.assertEqual(102.00, self.pub.till)
    #     self.assertEqual(0, self.pub.stock_level(self.drink_1))
