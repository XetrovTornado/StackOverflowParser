import requests, sys, os, html

def exit(msg="Invalid option."):
	print(msg)
	sys.exit()

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
except IndexError:
	site = "gheuipoklagopiahgoeqhhriszxljjsahjlvhlishuifwrhuighiulhuishuliguea"
if site not in sites:
	exit()
else:
	print("Searching " + site)

page = 1
lastpage = 0


while True:
	if not lastpage == page:
		lastpage = page
		questions = requests.get("https://api.stackexchange.com/2.2/search/advanced?sort=relevance&&answers=1&&q="+keywords+"&&site=" + site + "&&page=" + str(page)).json()['items']
	if len(questions) == 0:
		exit("No results matched your query.")
	for i, option in enumerate(questions):
		print("%d. %s" % (i, html.unescape(option['title'])))
	if len(questions) == 30:
		print(str(len(questions)) + ". Next Page")
	if page > 1:
		print(str(len(questions)+int(len(questions) == 30)) + ". Previous Page")
	print("Type in a number or option: ")
	q = input()
	try:
		q = questions[int(q)]['link']
	except ValueError:
		exit()
	except IndexError:
		if int(q) == 30:
			q = "Next Page"
			if q.lower().startswith("next"):
				page += 1
		elif int(q) == len(questions) + int(len(questions)== 30):
			q = "Previous Page"
			if q.lower().startswith("previous"):
				page -= 1
		else:
			exit()
	else:
		os.system('python3 soparser.py ' + q)
		break
