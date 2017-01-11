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

page = 1
lastpage = 1
while True:
	if lastpage not == page:
		lastpage = page
		questions = requests.get("https://api.stackexchange.com/2.2/search/advanced?answers=1&&q="+keywords+"&&site=" + site + "&&page=" + page).json()['items']

	if len(questions) == 0:
		print("No results matched your query.")
		sys.exit()

	for i, option in enumerate(questions):
		print("%d. %s" % (i, html.unescape(option['title'])))
	print("30. Next Page")
	print("Type in a number or option: ")
	q = input()
	try:
		q = questions[int(q)]['link']
	except ValueError:
		if int(q) == 30:
			q = "Next Page"
		pass
	if q == "Next Page":
		page += 1
	elif q not in questions:
		print("Invalid option.")
		continue
	else:
		os.system('python3 soparser.py ' + q)
		break
