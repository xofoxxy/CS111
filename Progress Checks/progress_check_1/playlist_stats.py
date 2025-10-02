"""
### Task 1: Playlist Length

Count the number of songs in the playlist.

Your output for this task should be written in one line:

```
The playlist has 38 songs.
```

### Task 2: Display Song Titles and Artists

After reading the CSV file, print the title and artist of the first and last
songs in the playlist.

Your output for this task should be written in two lines, with the first line
showing the first song and the second line showing the last song:

```
The first song is Zoltraak by Evan Call.
The last song is You Can Call Me Al by Paul Simon.
```

### Task 3: Most Popular Song

Find the song that has been played the most times. If there is a tie, return the
first song in the list with that play count. The song title and number of plays
should both be output:

```
The most played song was Defying Gravity, which was played 31 times.
```

### Task 4: Playlist Duration

Calculate the total length of the playlist in hours, minutes, and seconds (e.g.
`3:05:56` for 3 hours, 5 minutes, and 56 seconds).

Your output for this task should be written in one line:

```
The playlist is 3:05:56 long.
"""


def task1(playlist):
    print("The playlist has " + str(len(playlist)) + " songs.")


def task2(playlist):
    print("The first song is "+playlist[0]["title"]+" by "+playlist[0]["artist"]+".")
    print("The last song is "+playlist[-1]["title"]+" by "+playlist[-1]["artist"]+".")


def task3(playlist):
    max_plays = 0
    max_song = ""
    for song in playlist:
        if int(song["plays"]) > max_plays:
            max_plays = int(song["plays"])
            max_song = song["title"]
    print(max_song + " was played the most times at "+str(max_plays)+" plays.")


def task4(playlist):
    total_seconds = 0
    for song in playlist:
        minutes, seconds = song["duration"].split(":")
        total_seconds += int(minutes) * 60 + int(seconds)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    print("The playlist is "+str(hours)+":"+str(minutes)+f":{seconds:2.0f} long.")


def read_csv(playlist_location):
    playlist = []
    for line in open(playlist_location, "r"):
        song = {}
        # Title,Artist,Album,Duration,Genre,Plays
        title, artist, album, duration, genre, plays = line.split(",")
        song["title"] = title
        song["artist"] = artist
        song["album"] = album
        song["duration"] = duration
        song["genre"] = genre
        song["plays"] = plays
        playlist.append(song)
    return playlist


if __name__ == "__main__":
    playlist_location = input()
    playlist = read_csv(playlist_location)
    task1(playlist)
    task2(playlist)
    task3(playlist)
    task4(playlist)

