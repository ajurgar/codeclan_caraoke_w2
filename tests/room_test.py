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
        self.room2 = Room("EDM", 2, 20, 500)
        self.room3 = Room("Pop", 2, 30, 500)

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
        self.room.checked_in(self.guest2)
        self.room.checked_out(self.guest1)
        self.assertEqual(1, self.room.guest_count())
    
    def test_add_songs_to_room(self):
        self.room.add_song(self.song1.name)
        self.assertEqual(["Let It Be"], self.room.playlist)
        self.assertEqual(1, len(self.room.playlist))

    def test_charge_fee_to_guest(self):
        self.room.charge_fee(self.room.fee)
        self.guest1.pay_fee(self.room.fee)
        self.assertEqual(520, self.room.till)
        self.assertEqual(30, self.guest1.wallet)

    def test_limit_reached(self):
        self.room.checked_in(self.guest1)
        self.assertEqual(True, self.room.limit_reached())
    
    def test_limit_of_guest_check_ins(self):
        self.room.checked_in(self.guest1)
        self.room.checked_in(self.guest2)
        self.room.checked_in(self.guest3)
        self.assertEqual(2, self.room.guest_count())
    
  
    # def test_can_track_expenses_of_guest(self):
    #     # self.room.checked_in(self.guest1)
    #     # self.room.charge_fee(self.room.fee)
    #     # self.guest1.pay_fee(self.room.fee)
    #     self.room.charged_after_checked_in(self.room.fee, self.guest)