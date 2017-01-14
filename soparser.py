import urllib.request as u
from html.parser import HTMLParser
import sys

# Get a website from either the command line or a sample web page
try:
	website = sys.argv[1]
except IndexError:
	print("No webpage was provided.")
	sys.exit()
try:
	# Extract the html from the webpage
	html = u.urlopen(website).read().decode('utf-8')
except ValueError:
	print("Invalid option.")
	sys.exit()

# Parse the data
class DataFinder(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.startfound = False
		self.tagsfound = 0
		self.tag = ""
		self.type = ""
		self.value = ""
		self.text = ""
		self.returnlist = []
	def find(self, stuff, tag, findtype, value):
		self.tag = tag
		self.type = findtype
		self.value = value
		self.text = ""
		self.returnlist = []
		self.feed(stuff)
		return self.returnlist
	def handle_starttag(self, tag, attrs):
		# print("found starttag, tag=" + tag + " attrs=" + str(attrs))
		if tag == self.tag and len(attrs) > 0 and (self.type, self.value) in attrs:
			self.startfound = True
		if tag == self.tag and self.startfound:
			self.tagsfound += 1
		# show links attached to words
		if tag == "a" and self.startfound:
			self.text += "(%s)" % attrs[0][1]
	def handle_endtag(self, tag):
		if tag == "div" and self.startfound:
			self.tagsfound -= 1
			self.startfound = False
			self.returnlist.append(self.text)
			self.text = ""
	def handle_data(self, data):
		if not data.strip() == "" and self.startfound:
			self.text += data
		pass

df = DataFinder()
posts = df.find(html, "div", "class", "post-text")
times = df.find(html, "div", "class", "user-action-time")
postindex = 0
while postindex < len(posts):
	print(posts[postindex] + times[postindex])
	postindex += 1
	print("\n------------------")
	continu = input("Next post? ")
	if continu.startswith("n"):
		sys.exit()
		break
