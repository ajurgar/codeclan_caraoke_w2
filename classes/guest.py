from classes.room import Room

class Guest:
    def __init__(self, name, favourite_song, wallet):
        self.name = name
        self.favourite_song = favourite_song
        self.wallet = wallet
    
    def pay_fee(self, fee):
        if self.sufficient_money(fee):
            self.wallet -= fee
        
    def sufficient_money(self, fee):
        return self.wallet >= fee
    
    def fav_song_in_room (self, room, fav_song):
        for song in room:
            if fav_song == song.name:
                return "Whooo!"
# def check_if_fav_song_is_in_room(self, room, fav_song):
#         for song in room:
#             if fav_song == song.name:
#              return "Whoo"