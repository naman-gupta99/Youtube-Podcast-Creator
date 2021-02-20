from apiclient.discovery import build
from config import api_key

youtube_api = build('youtube', 'v3', developerKey=api_key)

# Get Channel Id
channel_id = input('Enter Channel ID: ')

# Get Playlist id
req = youtube_api.playlists().list(part = "snippet",channelId = channel_id, maxResults = 50)
res = req.execute()

while req is not None:
  res = req.execute()
  for i in res["items"]:
    print(i['snippet']['title'], i['id'])
  cont = input('Display more playlists? (y/n)?')
  if cont == 'y' or cont == 'Y':
    break  
  req = youtube_api.playlists().list_next(req, res)

print('\n Copy the id corresponding to the desired playlist and use to download audios')