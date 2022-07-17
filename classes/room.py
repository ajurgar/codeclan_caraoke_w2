class Room:
    def __init__(self, name, capacity, fee, till):
        self.name = name
        self.capacity = capacity
        self.till = till
        self.fee = fee
        self.playlist = [] 
        self.guest_list = []
    
    def checked_in (self, guest):
            if self.limit_reached():
                self.guest_list.append(guest)

    def checked_out (self, guest):
        self.guest_list.remove(guest)
    
    def guest_count (self):
        return len(self.guest_list)

    def add_song (self, song):
        self.playlist.append(song)
    
    def charge_fee(self, fee):
        self.till += fee
    
    def limit_reached (self):
        return self.guest_count() < self.capacity