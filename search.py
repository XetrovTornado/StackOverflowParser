import requests, sys, os, html

keywords = " ".join(sys.argv[1:])

questions = requests.get("https://api.stackexchange.com/2.2/search/advanced?answers=1&&q="+keywords+"&&site=askubuntu&&page=2").json()

for i, option in enumerate(questions['items']):
	print("%d. %s" % (i, html.unescape(option['title'])))
print("Type in a number or option: ")
q = input()
try:
	q = questions['items'][int(q)]['link']
except:
	pass

os.system('python3 soparser.py ' + q)
