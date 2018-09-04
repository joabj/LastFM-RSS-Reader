import os.path
import time
from mako.template import Template

## dd-mm-yyyy format
dated = time.strftime("Tops-%Y-%m-%d.html")

#Creates a new File:
f= open(dated,"w+")

#Opens "Template Opening"
TemplateOpening =open("Template-Opening.txt", "r")

#Reads Weekly Roundup
Content =TemplateOpening.read()

#Write data to the file created
f.write(Content)
TemplateOpening.close()

#Opens Weekly Roundup (Compiled by another program)
f2= open("/var/www/Data/Music/WeeklyRoundup.txt", "r")

#Reads Weekly Roundup
Content =f2.read()

#Write data to the file created
f.write(Content)
f2.close()

#Opens "Template Closing"
TemplateClosing =open("Template-Closing.txt", "r")

#Reads Weekly Roundup
Content =TemplateClosing.read()

#Write data to the file created
f.write(Content)
TemplateOpening.close()


#Closes Final files
f.close()

		
#https://www.guru99.com/reading-and-writing-files-in-python.html
