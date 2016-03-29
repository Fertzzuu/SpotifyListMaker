import pprint
import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 3:
	username = sys.argv[1]
	playlist_id = sys.argv[2]
	filename = sys.argv[3]
else:
	print("Usage: %s username playlist_id track_id ..." % (sys.argv[0],))
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
		track_ids.append(searchResult["tracks"]["items"][0]["uri"])


	#results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
	#print results

	for track_id in track_ids:
		print "[*] Adding " + sp.track(track_id)["name"] + " by " + sp.track(track_id)["artists"][0]["name"]
		idinlist = [track_id,]
		res = sp.user_playlist_add_tracks(username, playlist_id, idinlist)
		if res:
			print "[+] Song added to playlist\n"
		else:
			print "[-] Song not added to playlist\n"

else:
	print "Can't get token"
