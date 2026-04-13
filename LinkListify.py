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
        pass

    def remove_last_song(self):
        if self.head == None:
            return
        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        current = self.tail # set current to tail
        self.tail = current.prev # set new tail to song before old tail
        current.next = None # remove song after new tail (remove the song that was the old tail)

    def display_playlist(self):
        pass

    def count_songs(self):
        pass

    def find_song(self, title):
        pass

    def reverse_playlist(self):
        pass