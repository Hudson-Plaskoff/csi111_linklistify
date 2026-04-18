# csi111_linklistify
Repository for Mini Project 03 for Computer Science 111: Computer Science II.

Group members: Charles Levy, Hudson Plaskoff

Description:
This project uses a doubly linked list in a playlist class to handle and interact with data stored in objects from the song class. By default, the playlist contains three songs, but using methods that can be invoked with a text input, you can add and remove songs, display the playlist, find songs in the playlist by a specific artist, use some advanced features (see below), and more.

Instructions:
1. Run LinkListify.py
2. Read the options of actions to take for the playlist in the printed output
3. Enter the corresponding number into the text input
4. If applicable, enter any further information in subsequent text inputs (e.g. for adding a song)

Division of work:
We communicated regularly over text about the project. We also utilized GitHub to manage everything for this project. We both completed one of the advanced features, and everything else was also split up between the two of us to work on.

Advanced features:
A - Play Mode
D - Playlist Duration and Searching by Artist

LLM Usage for Play Mode: 

    Prompt:
    How can I efficiently implement a ‘previous track’ functionality in a Python music playlist using a doubly linked list? What are the different approaches and their trade-offs (e.g., re-traversing, storing previous)?

    Response:
    Approach 1: True Doubly Linked List (Recommended)
    Each node stores both next and prev pointers — O(1) navigation in both directions.
    pythonclass Song:
        def __init__(self, title, artist, duration):
            self.title = title
            self.artist = artist
            self.duration = duration
            self.next = None
            self.prev = None  # Key addition vs singly linked list

    class MusicPlaylist:
        def __init__(self):
            self.head = None
            self.tail = None
            self.current = None
            self.size = 0

        def add_song(self, title, artist, duration):
            song = Song(title, artist, duration)
            if not self.head:
                self.head = self.tail = song
                self.current = song
            else:
                song.prev = self.tail      # Link backward
                self.tail.next = song      # Link forward
                self.tail = song
            self.size += 1
            return self

        def next_track(self):
            if self.current and self.current.next:
                self.current = self.current.next
                return self.current
            return None  # Already at end

        def previous_track(self):        # ✅ O(1) - Direct pointer jump
            if self.current and self.current.prev:
                self.current = self.current.prev
                return self.current
            return None  # Already at start

        def current_track(self):
            return self.current

        def __repr__(self):
            tracks, node = [], self.head
            while node:
                marker = " ◀ NOW" if node == self.current else ""
                tracks.append(f"  [{node.title} - {node.artist}]{marker}")
                node = node.next
            return "Playlist:\n" + "\n".join(tracks)

    Approach 2: Stack-Based History (for Non-Sequential Playlists)
    Useful when "previous" means last played, not previous in list (e.g., shuffle mode).
    pythonfrom collections import deque

    class HistoryPlaylist:
        def __init__(self):
            self.songs = []          # Main playlist
            self.history = deque()   # Stack of played songs
            self.current_index = -1

        def play(self, index):
            if self.current_index >= 0:
                self.history.append(self.current_index)  # Push current to history
            self.current_index = index

        def previous_track(self):       # ✅ O(1) pop, but uses O(n) memory
            if self.history:
                self.current_index = self.history.pop()
                return self.songs[self.current_index]
            return None  # No history

        def next_track(self):           # For shuffle: pick random, push current
            import random
            self.history.append(self.current_index)
            self.current_index = random.randint(0, len(self.songs) - 1)
            return self.songs[self.current_index]

    Approach 3: Re-Traversal from Head (Naive — Avoid)
    pythondef previous_track_naive(self):    # ❌ O(n) — traverses entire list
        if not self.current or self.current == self.head:
            return None
        node = self.head
        while node.next != self.current:
            node = node.next
        self.current = node
        return self.current

    Approach 4: Circular Doubly Linked List (Seamless Wrap-Around)
    pythondef add_song(self, title, artist, duration):
        song = Song(title, artist, duration)
        if not self.head:
            self.head = self.tail = song
            song.next = song.prev = song   # Points to itself
        else:
            song.prev = self.tail
            song.next = self.head          # Wrap to head
            self.tail.next = song
            self.head.prev = song          # Head wraps back
            self.tail = song
        self.current = self.current or song

    def previous_track(self):             # ✅ O(1) — wraps to tail seamlessly
        if self.current:
            self.current = self.current.prev
            return self.current

    Explanation:
    Based on the LLM’s response, our methods were inspired by the “True Doubly Linked List” approach, which effectively uses the song class’s self.next and self.prev attributes for the next_track and previous_track methods respectively. After this, we implemented how these methods are involved in the main loop.


LLM Usage for Playlist Duration and Searching by Artist:

    Prompt:
    Write a Python function that takes a total number of seconds (integer) and
    returns a formatted string ‘MM:SS’.

    Response:
    def format_time(total_seconds):
        minutes = total_seconds // 60
        seconds = total_seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

    Explanation:
    The LLM helped us to format the math of this method with floor division and modulus being used to get minutes and seconds from the total seconds. We used this to create the complete method that collected all of the durations across all of the songs by traversing the songs of the playlist.
