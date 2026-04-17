# classes for song and playlist

class Song:
    def __init__(self,title,artist,duration):
        self.title = title
        self.artist = artist
        self.duration = duration # in seconds
        self.next = None
        self.prev = None

    def __str__(self):
        return f"'{self.title}' by {self.artist}"
    
class Playlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current_song = None

    def is_empty(self):
        if self.head == None:
            return True # true if self.head doesn't exist
        return False # false if self.head exists

    def add_song_at_end(self, title, artist, duration):
        new_song = Song(title,artist,duration)
        if self.is_empty(): # if playlist empty, add as first and last song
            self.head = new_song
            self.tail = self.head
            self.current_song = self.head
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
            self.current_song = self.head
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
            print(f"{count}. {current} (Duration: {current.duration}s)")
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

    def total_duration(self):
        total_seconds = 0
        current = self.head
        while current:
            total_seconds += current.duration
            current = current.next
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"
    
    def find_songs_by_artist(self, artist_name):
        songs = []
        current = self.head
        while current:
            if current.artist == artist_name:
                songs.append(current)
            current = current.next
        return songs
    
    def play_current_song(self):    
        if self.current_song is None:
            print("No song is currently playing.")
        else:
            print(f"Now playing: {self.current_song}")

    def next_song(self):
        if self.current_song is None:
            print("No song is currently playing.")
        elif self.current_song.next is None:
            print("You are at the end of the playlist.")
        else:
            self.current_song = self.current_song.next
            self.play_current_song()
    
    def previous_song(self):
        if self.current_song is None:
            print("No song is currently playing.")
        elif self.current_song.prev is None:
            print("You are at the beginning of the playlist.")
        else:
            self.current_song = self.current_song.prev
            self.play_current_song()

# main loop

playlist = Playlist() # create playlist
playlist.add_song_at_end("In the Air Tonight","Phil Collins",299) # 299 from 4*60 + 59
playlist.add_song_at_end("Allentown","Billy Joel",232) # 232 from 3*60 + 52
playlist.add_song_at_end("Abacab","Genesis",422) # x from 7*60 + 2

while True:
    print("Select a number to make a change...")
    print("1: Add song")
    print("2: Remove song")
    print("3: Display playlist")
    print("4: Count songs")
    print("5: Find a song")
    print("6: Reverse playlist")
    print("7: Display playlist duration")
    print("8: Find songs by arist")
    print("9: Play song")
    print("10: Next song")
    print("11: Previous song")
    print("0: Exit")
    n = int(input("What would you like to do?"))

    if n == 1:
        title = input("Enter song title: ")
        artist = input("Enter song's artist: ")
        duration = int(input("Enter song duration: "))
        playlist.add_song_at_end(title,artist,duration)
        print("{title} has been added")
    elif n == 2:
        title = input("Enter song title:")
        playlist.remove_song_by_title(title)
    elif n == 3:
        playlist.display_playlist()
    elif n == 4:
        song_count = playlist.count_songs()
        print(f"There are {song_count} songs")
    elif n == 5:
        title = input("Enter song title: ")
        position = playlist.find_song(title)
        if position == None:
            print("Song not found")
        else:
            print(f"Song found: {position}")
    elif n == 6:
        playlist.reverse_playlist()
        print("Playlist has been reversed")
    elif n == 7:
        duration = playlist.total_duration()
        print(f"Total duration: {duration}")
    elif n == 8:
        song_artist = input("Enter artist name: ")
        songs = playlist.find_songs_by_artist(song_artist)
        print(f"{song_artist}:")
        for song in songs:
            print(song)
    elif n == 9:
        playlist.play_current_song()
    elif n == 10:
        playlist.next_song()
    elif n == 11:
        playlist.previous_song()
    elif n == 0:
        break
    else:
        print("Invalid input.")