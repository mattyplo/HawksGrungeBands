# HawksGrungeBands
This is an example of utilizing the Spotify api with Python and the spotipy wrapper.  
The script setups up an authorization token so that the spotify api can be accessed.
Three calls are made to the api searching for tracks by a particular artist.  
Each result is passed to a method which takes the track name, album the track is from, and the spotify popularity of the track and puts those items into an excel spreadsheet.  
The result is three spreadsheets of a particular artists tracks and their popularity.

Create a cred.py file with your apps Client_ID and Client_Secret and place it into the HawksGrungeBands directory
It should look like this with the appropriate fields filled in.

CLIENT_ID='your_client_id'
CLIENT_SECRET='your_client_secret'

Requirements:
You will need to download and install spotipy and xlwt
This can be done with the following commands:
pip install spotipy
pip install xlwt

