import os.path
import time
from mako.template import Template

#This program assembles the final page for the weekly top music round-up. Using Mako, it first reads the opening template, then
#a file with notes (if any), the weekly roundup (created by WeeklyRoundup.py), then a file for any multimedia adds (Instagram, Twitter etc)
#Then finally the closing template. It then creates a unique filename for the current week. 


## dd-mm-yyyy format
dated = time.strftime("Tops-%Y-%m-%d.html")
TopDate = time.strftime("%B %d, %Y")

#Creates a new File:
f= open("/var/www/Data/Music/WeeklyRoundup/"+dated,"w+")

#The name of file
NewWeeklyReport = "/Data/Music/WeeklyRoundup/"+dated

#Set the template file to a variable
TemplateOpening = Template(filename='/var/www/Data/Music/code/WeeklyRoundup/Template-Opening.txt')

#Fill in the variables
FilledTemplateOpening =(TemplateOpening.render(TopDate=TopDate))

#Write data to the file created
f.write(FilledTemplateOpening)

#Opens and reads Notes (If Any)
fNotes= open("/var/www/Data/Music/code/WeeklyRoundup/WeeklyMusicNotes.txt", "r")
Notes =fNotes.read()
f.write(Notes)
fNotes.close()

#Resets the fNotes file
fNotes= open("/var/www/Data/Music/code/WeeklyRoundup/WeeklyMusicNotes.txt", "w")
fNotes.write("<!--Uncomment below to add notes<br><b>Notes:</b>-->")
fNotes.close

#Opens Weekly Roundup (Compiled by another program)
f2= open("/var/www/Data/Music/WeeklyRoundup.txt", "r")

#Reads Weekly Roundup
Content =f2.read()

#Write data to the file created
f.write(Content)
f2.close()

#Opens and reads in Multimedia Adds (If Any)
fMultiMedia= open("/var/www/Data/Music/code/WeeklyRoundup/WeeklyMusicMultimediaAdds.txt", "r")
MultiMedia =fMultiMedia.read()
f.write(MultiMedia)
fMultiMedia.close()
#Resets the fNotes file
fMultiMedia= open("/var/www/Data/Music/code/WeeklyRoundup/WeeklyMusicMultimediaAdds.txt", "w")
fMultiMedia.write("<!--Uncomment below to add notes<br><b>Multimedia:</b>-->")
fMultiMedia.close()


#Opens "Template Closing"
TemplateClosing =open("/var/www/Data/Music/code/WeeklyRoundup/Template-Closing.txt", "r")

#Reads Weekly Roundup
Content =TemplateClosing.read()

#Write data to the file created
f.write(Content)

#Closes Final files
f.close()

#Now to add to the index. Open the weekly index
OldIndex=open("/var/www/Data/Music/WeeklyRoundup/WeeklyRoundupArchive.txt", "r")
 
 #Reads Weekly Roundup
ContentIndex=OldIndex.read()
OldIndex.close()

#Writes in the new week
BigIndex=open("/var/www/Data/Music/WeeklyRoundup/WeeklyRoundupArchive.txt", "w")
BigIndex.write("<tr><td><a href="+dated+">"+TopDate+"</a></td></tr>")
BigIndex.write("\r\n")
BigIndex.write(ContentIndex)
BigIndex.close()

		
#https://www.guru99.com/reading-and-writing-files-in-python.html
