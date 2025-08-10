from song import Song
from video import Video
from mediaplayer import MediaPlayer
from playable import Playable, MediaInfo

# Comprehensive test case handler
test_case = input()

if test_case == "default_test":
    # Default test case from the original problem
    song = Song("Bohemian Rhapsody", "Queen", 355)
    video = Video("Python Tutorial", "1080p", 1800)
    player = MediaPlayer()

    # Test with song
    player.set_media(song)
    print(player.current_media.get_info())
    print(player.play())
    print(player.pause())
    print(player.stop())
    print()  # Empty line for readability

    # Test with video
    player.set_media(video)
    print(player.current_media.get_info())
    print(player.play())
    print(player.pause())
    print(player.stop())

elif test_case == "empty_player":
    # Test the media player with no media set
    player = MediaPlayer()
    print(player.play())  # Should print "No media set"
    print(player.pause())  # Should print "No media set"
    print(player.stop())  # Should print "No media set"

elif test_case == "time_formatting":
    # Test the time formatting in get_info() method
    song1 = Song("Short Song", "Artist A", 65)  # 1:05
    song2 = Song("Long Song", "Artist B", 3661)  # 61:01
    video1 = Video("Hour Video", "720p", 3600)  # 60:00
    
    print(song1.get_info())
    print(song2.get_info())
    print(video1.get_info())

elif test_case == "interface_compliance":
    # Test that Song and Video properly implement the interfaces
    song = Song("Test Song", "Test Artist", 180)
    video = Video("Test Video", "480p", 240)
    
    # Check interface implementation
    print(f"Song implements Playable: {isinstance(song, Playable)}")
    print(f"Song implements MediaInfo: {isinstance(song, MediaInfo)}")
    print(f"Video implements Playable: {isinstance(video, Playable)}")
    print(f"Video implements MediaInfo: {isinstance(video, MediaInfo)}")
    
    # Test all interface methods
    print(song.play())
    print(song.pause())
    print(song.stop())
    print(song.get_title())
    print(song.get_duration())
    print(song.get_info())
    
    print(video.play())
    print(video.pause())
    print(video.stop())
    print(video.get_title())
    print(video.get_duration())
    print(video.get_info())

elif test_case == "polymorphism":
    # Test polymorphic behavior with a list of different media types
    media_list = [
        Song("Song 1", "Artist 1", 180),
        Video("Video 1", "720p", 300),
        Song("Song 2", "Artist 2", 240),
        Video("Video 2", "1080p", 420)
    ]
    
    player = MediaPlayer()
    
    for media in media_list:
        player.set_media(media)
        print(f"Media: {media.get_title()}")
        print(f"Info: {media.get_info()}")
        print(f"Play: {player.play()}")
        print()

elif test_case == "edge_cases":
    # Test edge cases
    empty_song = Song("", "", 0)
    edge_video = Video("A" * 100, "", -10)  # Very long title, empty resolution, negative duration
    
    print(f"Empty song info: {empty_song.get_info()}")
    print(f"Edge video info: {edge_video.get_info()}")
    
    player = MediaPlayer()
    player.set_media(empty_song)
    print(player.play())
    player.set_media(edge_video)
    print(player.play())

elif test_case == "stress_test":
    # Implement a stress test with many media objects
    songs = [Song(f"Song {i}", f"Artist {i}", i * 30) for i in range(1, 101)]
    videos = [Video(f"Video {i}", f"{i*10}p", i * 60) for i in range(1, 101)]
    
    player = MediaPlayer()
    
    # Test with all songs
    for i, song in enumerate(songs):
        player.set_media(song)
        if i % 10 == 0:  # Print only every 10th to avoid too much output
            print(f"Playing song {i+1}: {player.play()}")
    
    # Test with all videos
    for i, video in enumerate(videos):
        player.set_media(video)
        if i % 10 == 0:  # Print only every 10th to avoid too much output
            print(f"Playing video {i+1}: {player.play()}")
    
    print("Stress test completed successfully!")
