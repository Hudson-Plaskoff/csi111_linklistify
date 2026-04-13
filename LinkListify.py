class Song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.next = None
        self.prev = None

    def __str__(self):
        return f"'{self.title}' by {self.artist}"
    
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head == None:
            return True # true if self.head doesn't exist
        return False # false if self.head exists

    def add_song_at_end(self, title, artist, duration):
        new_song = Song(title,artist,duration)
        if self.is_empty(): # if playlist empty, add as first and last song
            self.head = new_song
            self.tail = self.head
            return
        else: # if playlist not empty, add as last song
            current = self.head
            while current.next:
                current = current.next
            current.next = new_song
            new_song.prev = current
            self.tail = new_song

    def add_song_at_beginning(self, title, artist, duration):
        new_song = Song(title,artist,duration)
        if self.is_empty(): # if playlist empty, add as first song and last song
            self.head = new_song
            self.tail = self.head
            return
        else: # if playlist not empty, add as first song
            new_song.next = self.head
            self.head.prev = new_song
            self.head = new_song

    def remove_song_by_title(self, title):
        if self.is_empty():     # checks if playlist is empty, if it is, return without doing anything
            print("Playlist is empty.")
            return
        current = self.head
        while current:
            if current.title == title:
                if current.prev: # if song is not the first song, set prior song's next to current' next
                    current.prev.next = current.next
                else: # if song is the first song, set head to current's next
                    self.head = current.next
                if current.next: # if not last song, set next song's prev to current's prev
                    current.next.prev = current.prev
                else: # if song is the last song, set tail to current's prev
                    self.tail = current.prev

                print(f"'{title}' removed from playlist.")
                return
            
            current = current.next
        print(f"'{title}' not found in playlist.")


    def remove_last_song(self):
        if self.head == None:
            print("Playlist is empty.")
            return
        if self.head.next == None:
            print(f"'{self.head.title}' has been removed from playlist.")
            self.head = None
            self.tail = None
            return
        
        current = self.tail # set current to tail
        print(f"'{current.title}' has been removed from playlist.")
        self.tail = current.prev # set new tail to song before old tail
        self.tail.next = None 

    def display_playlist(self):
        if self.is_empty():
            print("Playlist is empty.")
            return
        current = self.head
        count = 1
        while current:
            print(f"{count}. {current}")
            current = current.next
            count += 1

    def count_songs(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
    

    def find_song(self, title):
        current = self.head
        while current:
            if current.title == title:
                return current
            current = current.next
        return None

    def reverse_playlist(self):
        current = self.head
        prev = None
        while current:
            next_song = current.next 
            current.next = prev  # reverse the next pointer to point to the previous song
            current.prev = next_song # reverse the prev pointer to point to the next song
            prev = current # move prev to current
            current = next_song 
        self.head, self.tail = self.tail, self.head # swap head and tail after reversing the playlist
        if self.head:
            self.head.prev = None
        if self.tail:
            self.tail.next = None



