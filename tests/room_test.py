import unittest

from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):

    def setUp(self):
        
        self.song1 = Song("Let It Be")
        self.song2 = Song("Gecko")
        self.song3 = Song("Despacito")

        self.room = Room("Rock", 2, 20, 500)

        self.guest1 = Guest("Michael", "Let It Be", 50)
        self.guest2 = Guest("Alex", "Gecko", 40)
        self.guest3 = Guest("Sandy", "Despacito", 10)

        self.guest_list = [self.guest1, self.guest2, self.guest3]
        

        self.playlist = [self.song1, self.song2, self.song3]


    def test_room_has_name(self):
        self.assertEqual("Rock", self.room.name)
    
    def test_room_has_money_in_till(self):
        self.assertEqual(500, self.room.till)

    def test_room_has_entry_fee(self):
        self.assertEqual(20, self.room.fee)
    
    def test_check_in_guest_to_room(self):
        self.room.checked_in(self.guest1)
        self.assertEqual(1, self.room.guest_count())

    def test_check_out_guest_to_room(self):
        self.room.checked_in(self.guest1)
        self.room.checked_out()
        self.assertEqual(0, self.room.guest_count())
    
    def test_add_songs_to_room(self):
        self.room.add_song(self.song1.name)
        self.assertEqual(["Let It Be"], self.room.playlist)
        self.assertEqual(1, len(self.room.playlist))

    def test_charge_fee_to_guest(self):
        self.room.charge_fee(self.room.fee)
        self.guest1.pay_fee(self.room.fee)
        self.assertEqual(520, self.room.till)
        self.assertEqual(30, self.guest1.wallet)
    
    def test_limit_of_guest_check_ins(self):
        # self.guest.guest_count(98)
        self.room.checked_in(self.guest1)
        self.room.checked_in(self.guest2)
        self.room.checked_in(self.guest3)
        # self.assertEqual(False, room.checked_in(self.guest3))
        self.assertEqual(2, self.room.guest_count())
    
    def test_if_favourite_song_is_in_playlist(self):
        self.guest = Guest("Jamie", "Let It Be", 50)
        self.room.add_song(self.song1)
        self.room.add_song(self.song2)
        self.room.add_song(self.song3)
        self.guest.fav_song_matched(self.song1)
        # self.room.fav_song_matched(self.song1)
        self.assertEqual("Whooo!", self.room.fav_song_matched(self.song1))
    
    

    # def test_pub_cannot_serve_drink(self):
    #     self.pub.add_drink(self.drink_1)
    #     self.pub.add_drink(self.drink_2)
    #     self.pub.serve(self.customer_1, self.drink_1)
    #     self.assertEqual(8.00, self.customer_1.wallet)
    #     self.assertEqual(102.00, self.pub.till)
    #     self.assertEqual(0, self.pub.stock_level(self.drink_1))
