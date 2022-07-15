import unittest

from classes.guest import Guest
from classes.room  import Room

class TestGuest (unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Michael", "Let It Be", 50)
        self.room = Room("EDM", 3, 30, 400)
    
    def test_guest_has_name(self):
        self.assertEqual("Michael", self.guest.name)

    
    def test_guest_has_favourite_song(self):
        # self.favourite_song = "Let It Be"
        self.assertEqual("Let It Be", self.guest.favourite_song)
    
    def test_guest_has_money_in_wallet(self):
        self.assertEqual(50, self.guest.wallet)
    
    def test_guest_can_pay_fee_if_they_have_money(self):
        self.guest.pay_fee(self.room.fee)
        self.assertEqual(20, self.guest.wallet)

    def test_guest_can_pay_fee_if_they_dont_have_money(self):
        guest = Guest("Gustavo", "Rock", 10)
        guest.pay_fee(self.room.fee)
        self.assertEqual(10, guest.wallet)


    # def test_sufficient_money_for_fee(self):
    #     self.assertEqual(True, self.customer.sufficient_money())