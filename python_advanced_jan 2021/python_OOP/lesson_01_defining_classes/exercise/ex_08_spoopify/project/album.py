from project.song import Song
from project.band import Band


class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song in self.songs:
            return "Song is already in the album."
        if self.published:
            return "Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"

        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return 'Cannot remove songs. Album is published.'
        for song in self.songs:
            if song_name == song.name:
                self.songs.remove(song)
                return f"Removed song {song.name} from album {self.name}."
        else:
            return f"Song is not in the album."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already puplished."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        res = '\n'.join(f"== {s.get_info()}" for s in self.songs)
        return f"Album {self.name}\n" \
               f"{res}"




song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

from project.song import Song
from project.album import Album
from project.band import Band

import unittest


class SongTest(unittest.TestCase):
    def test_song_init(self):
        song = Song("A", 3.15, False)
        message = song.get_info()
        expected = "A - 3.15"
        self.assertEqual(message, expected)

    def test_album_init(self):
        album = Album("The Sound of Perseverance")
        message = album.details()
        expected = "Album The Sound of Perseverance\n"
        self.assertEqual(message, expected)

    def test_add_song_working(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        message = album.add_song(song)
        expected = "Song Scavenger of Human Sorrow has been added to the album The Sound of Perseverance."
        self.assertEqual(message, expected)

    def test_add_song_already_added(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        message = album.add_song(song)
        expected = "Song is already in the album."
        self.assertEqual(message, expected)

    def test_add_song_single(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, True)
        message = album.add_song(song)
        expected = "Cannot add Scavenger of Human Sorrow. It's a single"
        self.assertEqual(message, expected)

    def test_add_song_published_album(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.publish()
        message = album.add_song(song)
        expected = "Cannot add songs. Album is published."
        self.assertEqual(message, expected)

    def test_remove_song_working(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        message = album.remove_song("Scavenger of Human Sorrow")
        expected = "Removed song Scavenger of Human Sorrow from album The Sound of Perseverance."
        self.assertEqual(message, expected)

    def test_remove_song_not_in_album(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        message = album.remove_song("Scavenger of Human Sorrow")
        expected = "Song is not in the album."
        self.assertEqual(message, expected)

    def test_remove_song_album_published(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        album.publish()
        message = album.remove_song("Scavenger of Human Sorrow")
        expected = "Cannot remove songs. Album is published."
        self.assertEqual(message, expected)

    def test_publish(self):
        album = Album("The Sound of Perseverance")
        message = album.publish()
        expected = album.published
        self.assertTrue(expected)

    def test_publish_message(self):
        album = Album("The Sound of Perseverance")
        message = album.publish()
        expected = "Album The Sound of Perseverance has been published."
        self.assertEqual(message, expected)

    def test_details(self):
        album = Album("The Sound of Perseverance")
        song = Song("Scavenger of Human Sorrow", 6.56, False)
        album.add_song(song)
        message = album.details()
        expected = "Album The Sound of Perseverance\n== Scavenger of Human Sorrow - 6.56\n"

    def test_init(self):
        band = Band("Death")
        message = f"{band.name} - {len(band.albums)}"
        expected = "Death - 0"
        self.assertEqual(message, expected)

    def test_add_album_working(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        message = band.add_album(album)
        expected = "Band Death has added their newest album The Sound of Perseverance."
        self.assertEqual(message, expected)

    def test_add_album_already_added(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        band.add_album(album)
        message = band.add_album(album)
        expected = "Band Death already has The Sound of Perseverance in their library."
        self.assertEqual(message, expected)

    def test_remove_album_working(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        band.add_album(album)
        message = band.remove_album("The Sound of Perseverance")
        expected = "Album The Sound of Perseverance has been removed."
        self.assertEqual(message, expected)

    def test_remove_album_not_found(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        message = band.remove_album("The Sound of Perseverance")
        expected = "Album The Sound of Perseverance is not found."
        self.assertEqual(message, expected)

    def test_remove_album_published(self):
        band = Band("Death")
        album = Album("The Sound of Perseverance")
        album.publish()
        band.add_album(album)
        message = band.remove_album("The Sound of Perseverance")
        expected = "Album has been published. It cannot be removed."
        self.assertEqual(message, expected)

    def test_details(self):
        band = Band("Death")
        message = band.details()
        expected = "Band Death\n"
        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()