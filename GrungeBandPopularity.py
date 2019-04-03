import spotipy
import pprint
import xlwt
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id='', client_secret= '')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)