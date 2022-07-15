class Room:
    def __init__(self, name, till):
        self.name = name
        # self.capacity = capacity
        self.till = till
        self.playlist = []
        self.guest_list = []
    
    def add_guest(self, guest):
        self.guest_list.append(guest)
    
    def checked_out (self):
        self.guest_list.pop()
    
    def guest_count (self):
        return len(self.guest_list)

    def add_song (self, song):
        self.playlist.append(song)

    def checked_in (self, guest):
        if self.guest_count <= 2:
         return self.guest_list.append(guest)
        else:
            return False

    # def limit_entry(self):
    #     self.room.checked_in
    #     if self.capacity > 100:
    #         return True
    #     else:
    #         return False

    

            