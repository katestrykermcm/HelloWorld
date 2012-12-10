'''With the URL provided by the user, this program retrieves all of the images on the website and saves them to a file'''
__author__ = "Kate McManus" 
__version__ = "1.0"

import urllib2
import sys
from os.path import join as pjoin
import re
# had lots of issues with recognizing the commands import HTMLParser for option 3

class extractImages:

	def __init__(self):
		self.myList = []
		self.text = " "

	def openURL(self):
		'''Retrieves the raw HTML information from the URL entered at the command line'''
		url = sys.argv[1] # from command line, already in type string
		pullin = urllib2.urlopen(url)
		self.text = pullin.read()
		pullin.close()

	def findPicData(self):
		'''Fills list with all of the URLs of the images on the desired website, using regular expressions to find the indexes of the start and finish of the url'''
		pattern = '<img src=".*?(")'
		for match in re.finditer(pattern, self.text):
    			s = match.start() + 10
    			e = match.end() - 1
    			#print 'Found %s at %d:%d' % (text[s:e], s, e)
    			self.myList.append(self.text[s:e])

	def listInfo(self):
		'''Creates and writes to a file with the images found on the desired website'''
		for x in range(0, len(self.myList)):
			filename = str(x) + ".jpg"
			f = open(filename, "w")
			f.write(urllib2.urlopen(self.myList[x]).read())
			f.close()

if __name__ == '__main__':

	imageExtracter = extractImages()
	imageExtracter.openURL()
	imageExtracter.findPicData()
	imageExtracter.listInfo()
