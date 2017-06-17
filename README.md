# LastFM-RSS-Reader
This is Python program that parses the RSS feed from Last.FM for personal music stats

This Python program pulls the top albums, artists, and tracks captured by LastFM RSS feed in the json format 
(run "pprint" for json taxonomy). The program puts the data  in a blank "WeeklyRoundup.txt" file with some HTML 
formatting so it can be embedded into an HTML file

It runs on Python 2.6.6 and up on Python 2.* 

The main program requires the Environs.py library of environmental variables (a blank template is included here), 
or create your own more secure way of bringing in variables

Example of the output, for my own account, can be found here: http://joabj.com/Data/Music/WeeklyRoundup.html

Here are some of the supporting documents I used:

https://pythonspot.com/en/json-encoding-and-decoding-with-python/
http://www.last.fm/api/show/user.getWeeklyTrackChart
http://www.last.fm/api/show/user.getWeeklyArtistChart
http://www.last.fm/api/show/user.getWeeklyAlbumChart
http://stackoverflow.com/questions/5141559/unicodeencodeerror-ascii-codec-cant-encode-character-u-xef-in-position-0
http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
http://stackoverflow.com/questions/7361253/how-to-determine-whether-a-substring-is-in-a-different-string
http://www.last.fm/api/show/user.getTopAlbums
http://stackoverflow.com/questions/3437059/does-python-have-a-string-contains-substring-method
