from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import pandas as pd

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


# Initialize Spotify client
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_artist_data(artist_id):
    artist = sp.artist(artist_id)
    return artist

def get_artist_top_tracks(artist_id):
    top_tracks = sp.artist_top_tracks(artist_id)
    return top_tracks['tracks']

# Example usage
artistId = '0L8ExT028jH3ddEcZwqJJ5'  # Replace with the artist's Spotify ID
artistData = get_artist_data(artistId)
top_tracks = get_artist_top_tracks(artistId)
df = pd.DataFrame(top_tracks)

# Display the DataFrame
print(df[['duration_ms', 'name']])
