#This program pulls the top albums, artists and tracks captured by LastFM in the json format (run "pprint" for json taxonomy)
#It requires the WeeklyRoundup.html file to complete the formatting.

import datetime
import json
import requests
from sys import argv
from pprint import pprint
#The small library with the environmental settings...
import Environs


#Some API boilerplate we'll need soon
RequestPrefix='http://ws.audioscrobbler.com/2.0/?method='
RequestServiceUser='&user=' + Environs.User
RequestPersonalKey='&api_key='+ Environs.PersonalKey
RequestSuffix='&format=json'

#Open File for writing (Set in Environs library)
target = open(Environs.WriteFile, 'w')

#Artists
RequestService='user.getweeklyartistchart'
AssembledRequest = RequestPrefix+RequestService+RequestServiceUser+RequestPersonalKey+RequestSuffix
#Debugging:
#print AssembledRequest
response = requests.get(AssembledRequest)
data = response.json()
x = 0
ChartPlacement = 1 

target.write("<h3>Top Artists</h3>")
target.write("<table><tr><th><b>#</b></th><th>Artist</th><th>Tracks Played</th></tr>")

while x < 10:
	ArtistName =  data[u'weeklyartistchart'][u'artist'][x][u'name']
	ArtistPlaycount = data[u'weeklyartistchart'][u'artist'][x][u'playcount']
		
	Number = "<tr><td>#" + str(ChartPlacement) + "   </div></td>"
	ArtistNameString = "<td><div class=\"album\"><b>" + ArtistName + "</b></div></td>"
	ArtistPlaycountString = "<td><div class=\"Playcount\">" + ArtistPlaycount + "</div></td></tr>"
	
	
	target.write(Number)
	target.write(ArtistNameString.encode('ascii', 'ignore'))
	target.write("\n")
	target.write(ArtistPlaycountString)
	target.write("\n")
	target.write("\n")
	
	ChartPlacement = ChartPlacement + 1
	x = x + 1 

target.write("</table>")
target.write("<img id=ImageCenter src=/Tilde-Color.jpg  height=27 width=60><p>")	

#Weekly Album ChartPlacement
RequestService='user.getweeklyalbumchart'
AssembledRequest = RequestPrefix+RequestService+RequestServiceUser+RequestPersonalKey+RequestSuffix
#Debugging:
#print "\n"
#print AssembledRequest
response = requests.get(AssembledRequest)
data = response.json()
x = 0
ChartPlacement = 1 
				
target.write("<h3>Top Albums</h3>")
target.write("<table><tr><th><b>#</b></th><th>Name</th><th>Artist</th></tr>")

while x < 10:
	AlbumName =  data[u'weeklyalbumchart'][u'album'][x][u'name']
	AlbumPlaycount = data[u'weeklyalbumchart'][u'album'][x][u'playcount']
	if AlbumName.find("SXSW") == -1:
		AlbumArtist = data[u'weeklyalbumchart'][u'album'][x][u'artist'][u'#text']
	else: 
		AlbumArtist = "Various"
		
	Number = "<tr><td>#" + str(ChartPlacement) + "   </div></td>"
	AlbumNameString = "<td><div class=\"album\"><b>" + AlbumName + "</b></div></td>"
	AlbumArtistString = "<td><div class=\"artist\">" + AlbumArtist + "</div></td></tr>"
		
	target.write(Number)
	target.write(AlbumNameString.encode('ascii', 'ignore'))
	target.write("\n")
	target.write(AlbumArtistString.encode('ascii', 'ignore'))
	target.write("\n")
	target.write("\n")
	
	ChartPlacement = ChartPlacement + 1
	x = x + 1 

target.write("</table>")
target.write("<img id=ImageCenter src=/Tilde-Color.jpg  height=27 width=60><p>")	

#Top 5 Tracks
RequestService='user.getweeklytrackchart'
AssembledRequest = RequestPrefix+RequestService+RequestServiceUser+RequestPersonalKey+RequestSuffix
response = requests.get(AssembledRequest)
data = response.json()
x = 0
ChartPlacement = 1 

target.write("<h3>Top Tracks</h3>")
target.write("<table><tr><th><b>#</b></th><th>Song</th><th>Artist</th><th>Times Played</th></tr>")

while x < 5:
	TrackName =  data[u'weeklytrackchart'][u'track'][x][u'name']
	TrackArtist =  data[u'weeklytrackchart'][u'track'][x][u'artist'][u'#text']
	TrackPlaycount = data[u'weeklytrackchart'][u'track'][x][u'playcount']

		
	Number = "<tr><td>#" + str(ChartPlacement) + "   </div></td>"
	AlbumNameString = "<td><div class=\"album\"><b>" + TrackName + "</b></div></td>"
	AlbumArtistString = "<td><div class=\"artist\">" + TrackArtist + "</div></td>"
	AlbumPlaycountString = "<td><div class=\"Playcount\">" + TrackPlaycount + "</div></td></tr>"
	
	
	target.write(Number)
	target.write(AlbumNameString.encode('ascii', 'ignore'))
	target.write("\n")
	target.write(AlbumArtistString.encode('ascii', 'ignore'))
	target.write("\n")
	target.write(AlbumPlaycountString)
	target.write("\n")
	target.write("\n")
	
	ChartPlacement = ChartPlacement + 1
	x = x + 1 

target.write("</table></center>")	
target.write("<img id=ImageCenter src=/Tilde-Color.jpg  height=27 width=60><p>")	
target.close()




#For printing the JSON taxonomy
#pprint(data)
