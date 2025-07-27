import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Step 1: Spotify Credentials (yaha apna Client ID aur Client Secret daal)
client_id = "b36b68282a4849eab3a2e7101f56b50f"
client_secret = "3e09e6f7122644469e6a6b1724cf8147"

# Step 2: Authentication
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Step 3: Search Playlist
result = sp.search(q="romantic songs", type="playlist", limit=1)

# Step 4: Result Print
playlist = result['playlists']['items'][0]
print("Playlist Name:", playlist['name'])
print("Playlist URL:", playlist['external_urls']['spotify'])
