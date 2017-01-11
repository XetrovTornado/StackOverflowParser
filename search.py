import requests, sys, os, html

keywords = " ".join(sys.argv[1:])

sites = [
	"stackoverflow.com",
	"askubuntu.com",
	"superuser.com",
	"serverfault.com",
	"unix.stackexchange.com"
	]

print("Which website do you want to check?")

for i, site in enumerate(sites):
	print("%d. %s" % (i, site))
print("Type in a number or option: ")
site = input()
try:
	site = sites[int(site)]
except ValueError:
	pass
if site not in sites:
	print("THAT ISN'T A WEBSITE!!!!")
	sys.exit()
else:
	print("Searching " + site)

questions = requests.get("https://api.stackexchange.com/2.2/search/advanced?answers=1&&q="+keywords+"&&site=" + site).json()

if len(questions['items']) == 0:
	print("No results matched your query.")
	sys.exit()

for i, option in enumerate(questions['items']):
	print("%d. %s" % (i, html.unescape(option['title'])))
print("Type in a number or option: ")
q = input()
try:
	q = questions['items'][int(q)]['link']
except:
	pass

os.system('python3 soparser.py ' + q)
