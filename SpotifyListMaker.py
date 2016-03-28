import urllib
import urllib2
import json
import os 


def getSongURI(title): 	
	
	url = "https://api.spotify.com/v1/search?q=" + "+".join(title.split(" ")) + "&type=track&market=HU"

	uriReq = urllib2.Request(url)

	uriReq.add_header('Accept', "application/json")
	res = urllib2.urlopen(uriReq)

	plainJSON = res.read()
	parsedJSON = json.loads(plainJSON)
	res.close()

	try:
		currentSong = parsedJSON["tracks"]["items"][0]["uri"]
		return currentSong
		
	except IndexError:
		print "song not found"
		return

def fillExistingPlaylist(songs, playlistID, username):

	OAuthToken = "BQBnKDn_4KTbrjFaG9EKX0WB3EwTDadzOCZp7YaNQZL-K6Eme19oQI99PnIQD98cvErQ2VtcUSGnzxStnNlDMpTRRf-uCSBAN_pb9eHjfwvZbCEMGILlblRMyVpSAfFnKXiwmTTnncREHAKsIE3q8E3iGCWVmyL-cxDsb-96dWgAq2VB17_r5gya"
	
	for song in songs:
		if song:
			"""url = "https://api.spotify.com/v1/users/" + username + \
					"/playlists/" + playlistID + "/tracks?uris=" + \
					"%3A".join(song.split(":"))
			data = urllib.urlencode({"Accept" : "application/json", "Authorization" : "Bearer " + OAuthToken})

			plReq = urllib2.Request(url, data)
			
			plReq.add_header("Accept", "application/json")
			plReq.add_header("Authorization", "Bearer " + OAuthToken)
			
			
			
			res = urllib2.urlopen(plReq, data)
			if res:
				print res.read()
			else:
				print "Couldn't add song to playlist"
			
			res.close()
			"""
			post_cmd = 'curl -X POST "https://api.spotify.com/v1/users/' + \
			           username + '/playlists/' + playlistID +'/tracks?uris=' + \
			           '%3A'.join(song.split(":")) + '" -H "Accept: application/json" ' + \
			           '-H "Authorization: Bearer ' + OAuthToken + '"'
			print post_cmd
			os.system(post_cmd)

def main():
	songs = list()
	
	filename = raw_input("File name of the songs: ")
	listfile = open(filename)
	for i in listfile.readlines():
		print i.rstrip()
		songuri = getSongURI(i.rstrip())
		songs.append(songuri)
	
	
	username = raw_input("Feed me the username: ")
	playlistID = raw_input("Feed me the id of the wished playlist (will be automated later): ")
	
	fillExistingPlaylist(songs, playlistID, username)
	
#--------------

if __name__ == "__main__":
	main()	
