import pprint
import sys
import os
#os.system("export SPOTIPY_CLIENT_ID='b886776f24d34fea8498023c9bb5841e'")
#os.system("export SPOTIPY_CLIENT_SECRET='6c5d81174e884d15bcbe7337d7de67f9'")
#os.system("export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'")

import spotipy
import spotipy.util as util

if len(sys.argv) > 3:
	username = sys.argv[1]
	playlist_id = sys.argv[2]
	filename = sys.argv[3]
else:
	print("Usage: %s [username] [playlist_id] [songs file]" % (sys.argv[0],))
	sys.exit()

scope = 'playlist-modify-public'
token = util.prompt_for_user_token(username, scope)


if token:
	sp = spotipy.Spotify(auth=token)
	sp.trace = False
	track_ids = list()
	songs = open(filename)


	for song in songs.readlines():
		searchResult = sp.search(song)
		i = 0
		print searchResult
		gotArtist = searchResult["tracks"]["items"][i]["artists"][0]["name"].lower()
		givenArtist = song.split(",")[0].lower()
		print gotArtist
		print givenArtist
		
		"""while (gotArtist != givenArtist):
			gotArtist = searchResult["tracks"]["items"][i]["artists"][0]["name"].lower()
			print gotArtist
		
		track_ids.append(searchResult["tracks"]["items"][i]["uri"])
		"""

	for track_id in track_ids:
		print "[*] Adding " + sp.track(track_id)["name"] + " by " + sp.track(track_id)["artists"][0]["name"]
		idinlist = [track_id,]
		res = sp.user_playlist_add_tracks(username, playlist_id, idinlist)
		if res:
			print "[+] Song added to playlist\n"
		else:
			print "[-] Song not added to playlist\n"
			
			
	songs.close()

else:
	print "Can't get token"
