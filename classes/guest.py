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
    
    def fav_song_matched (self, playlist):
        for song in room:
            if song == self.favourite_song:
                return "Whooo!"
