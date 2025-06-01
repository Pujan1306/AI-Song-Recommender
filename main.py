from gemini import SongRecommender
from youtube import YouTubeSearch

song_input = input("Enter the mood of song or any thing you want to search: ")

prompt = f"""Recommend one hindi song that perfectly fits the following mood. Respond with only the song name (including the artist), and nothing else.

Mood: {song_input}
"""

gemini = SongRecommender()
response = gemini.GenerateSong(prompt)

youtube = YouTubeSearch()
youtube.search(response)

