import urllib.request as u
from html.parser import HTMLParser
import sys

# Get a website from either the command line or a sample web page
try:
	website = sys.argv[1]
except IndexError:
	print("No webpage was provided.")
	sys.exit()

# Extract the html from the webpage
html = u.urlopen(website).read().decode('utf-8')

# Parse the data
class WebScraper(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.startfound = False
		self.divsfound = 0
	def handle_starttag(self, tag, attrs):
		# print("found starttag, tag=" + tag + " attrs=" + str(attrs))
		if tag == "div" and len(attrs) > 0 and ("class", "post-text") in attrs:
			#print("start found")
			self.startfound = True
		if tag == "div" and self.startfound:
			#print("div found: " + str(self.divsfound))
			self.divsfound += 1
		if tag == "a" and self.startfound:
			print("(%s)" % attrs[0][1], end="")
	def handle_endtag(self, tag):
		if tag == "div" and self.startfound:
			#print("end div found")
			self.divsfound -= 1
			if self.divsfound <= 0:
				print("\n------------------")
				continu = input("Next post? ")
				if continu.startswith("n"):
					sys.exit()
				self.startfound = False
	def handle_data(self, data):
		if not data.strip() == "" and self.startfound:
			print(data, end="")
		pass

WebScraper().feed(html)

