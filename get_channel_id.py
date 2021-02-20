from apiclient.discovery import build
from config import api_key

youtube_api = build('youtube', 'v3', developerKey=api_key)

# Get channel name
query = input('Enter channel name : ')

# Get channel id
req = youtube_api.search().list(q=query, part='snippet', type='channel', maxResults=10)
res = req.execute()
for item in res['items']:
  print(item['snippet']['title'], item['id']['channelId'])

print('\n Copy the id corresponding to the desired channel and use to get the playlist id')
