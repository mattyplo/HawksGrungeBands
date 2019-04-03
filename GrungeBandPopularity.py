import spotipy
import pprint
import xlwt
from spotipy.oauth2 import SpotifyClientCredentials


def writeTracksToExcel(query):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("New Sheet")
    count = 1
    for i in query['tracks']['items']:
        print(i['name'] + ' ', i['popularity'])
        name = i['name']
        print(str(name))
        sheet.write(count, 1, i['name'])
        count += 1

    wb.save('newSheet.xls')

# Setup authorization token to access spotify api
client_credentials_manager = SpotifyClientCredentials(client_id='926b2b6950e745cc80d89ed6037db878', client_secret= 'd745522d16f747c79e15c2a4648b388f')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# search spotify for top fifty tracks by given artist
results = sp.search(q='artist:' + 'alice in chains', type='track', limit=50)

writeTracksToExcel(results)