from pytube import YouTube
from apiclient.discovery import build
from config import api_key

youtube_api = build('youtube', 'v3', developerKey=api_key)

# Get Playlist Id
playlist_id = input('Enter Playlist ID: ')

# Get ids for all videos in the Playlist
video_ids = []

req = youtube_api.playlistItems().list(playlistId=playlist_id, part='snippet', maxResults=50)
res = req.execute()
for item in res['items']:
  obj = (item['snippet']['title'],item['snippet']['resourceId']['videoId'])
  video_ids.append(obj)

# Download Video Audios
for obj in video_ids:
  title, id = obj
  video_url = 'https://youtu.be/' + id

  try:
    yt_obj = YouTube(video_url)
    yt_obj.streams.get_audio_only().download(output_path='Podcasts', filename=title)
    print(title, ': YouTube video audio downloaded successfully')
  except Exception as e:
    print(e)