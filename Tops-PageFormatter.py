import os.path
import time
from mako.template import Template

## dd-mm-yyyy format
dated = time.strftime("Tops-%Y-%m-%d.html")
TopDate = time.strftime("%B %d, %Y")

#Creates a new File:
f= open("/var/www/Data/Music/WeeklyRoundup/"+dated,"w+")

#Set the template file to a variable
TemplateOpening = Template(filename='Template-Opening.txt')

#Fill in the variables
FilledTemplateOpening =(TemplateOpening.render(TopDate=TopDate))

#Write data to the file created
f.write(FilledTemplateOpening)

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

#Closes Final files
f.close()

		
#https://www.guru99.com/reading-and-writing-files-in-python.html