class SongNode:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next = None

class MusicPlaylist:
    def __init__(self):
        self.head = None

    def create_playlist(self):
        self.head = None
        print("A new empty playlist has been successfully created.")

        def insert_song(self, title, artist):

     new_song = SongNode(title, artist)
        
            if not self.head:
            self.head = new_song
            print(f"'{title}' added as the first song.")
            return
        
        current = self.head
        while current.next:
            current = current.next
        current.next = new_song
        print(f"'{title}' added to the playlist.")

    
    def delete_song(self, title):
        if not self.head:
            print("The playlist is empty. Nothing to delete.")
            return

        if self.head.title.lower() == title.lower():
            print(f"Removed: '{self.head.title}' by {self.head.artist}")
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.title.lower() == title.lower():
                print(f"Removed: '{current.next.title}' by {current.next.artist}")
                current.next = current.next.next
                return
            current = current.next

        print(f"Song '{title}' not found in the playlist.")
        
    def display_playlist(self):
        if not self.head:
            print("\n--- Playlist is currently empty ---")
            return

        print("\n--- Current Music Playlist ---")
        current = self.head
        index = 1
        while current:
            print(f"{index}. '{current.title}' by {current.artist}")
            current = current.next
            index += 1
        print("------------------------------")

if __name__ == "__main__":
    my_playlist = MusicPlaylist()

    while True:
        print("\n*** MUSIC PLAYLIST MANAGER ***")
        print("1. Create New Playlist")
        print("2. Insert Song")
        print("3. Deletion of Song")
        print("4. Display Playlist")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            my_playlist.create_playlist()

        elif choice == '2':
            title = input("Enter song title: ").strip()
            artist = input("Enter artist name: ").strip()
            if title and artist:
                my_playlist.insert_song(title, artist)
            else:
                print("Song title and artist cannot be empty!")

        elif choice == '3':
            title = input("Enter the title of the song to delete: ").strip()
            if title:
                my_playlist.delete_song(title)
            else:
                print("Song title cannot be empty!")

        elif choice == '4':
            my_playlist.display_playlist()

        elif choice == '5':
            print("Exiting playlist manager. Goodbye!")
            break

        else:
            print("Invalid choice! Please select an option between 1 and 5.")
