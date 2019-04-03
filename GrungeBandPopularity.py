import spotipy
import pprint
import xlwt
from spotipy.oauth2 import SpotifyClientCredentials


def writeTracksToExcel(query, artist):
    wb = xlwt.Workbook()
    sheet = wb.add_sheet("New Sheet")
    count = 1
    for i in query['tracks']['items']:
        sheet.write(count, 0, i['name'])
        sheet.write(count, 1, i['popularity'])
        sheet.write(count, 2, i['album']['name'])
        count += 1

    wb.save(artist + '.xls')

# Setup authorization token to access spotify api
client_credentials_manager = SpotifyClientCredentials(client_id='926b2b6950e745cc80d89ed6037db878', client_secret= 'd745522d16f747c79e15c2a4648b388f')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# search spotify for top fifty tracks by given artist
results = sp.search(q='artist:' + 'alice in chains', type='track', limit=50)
results2 = sp.search(q='artist:' + 'pearl jam', type='track', limit=50)
results3 = sp.search(q='artist:' + 'soundgarden', type='track', limit=50)

writeTracksToExcel(results, 'Alice in Chains')
writeTracksToExcel(results2, 'Pearl Jam')
writeTracksToExcel(results3, 'Soundgarden')