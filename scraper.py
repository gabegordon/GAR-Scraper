import re
import urllib.parse
import urllib.request
import requests
import csv

with open('agents.txt') as f:
    lines = f.readlines()

agentURL = "/scripts/mgrqispi.dll?APPNAME=IMS&PRGNAME=IMSListingAgentDetail"
mailToString = "<td valign=\"top\"><a href=\"mailto:"
agentURLS = []
emails = []
emailsFormatted = []


for line in lines:
	if agentURL in line:
		mURL = re.findall(r'"([^"]*)"', line)
		strURL = ''.join(mURL)
		fullURL = "https://members.gallatinrealtors.com" + str1
		agentURLS.append(fullURL)
		

for url in agentURLS:
	page = requests.get(url)
	for line in page.iter_lines():
		if b'\t\t<td valign="top"><a href="mailto:' in line:
			print(line.decode("utf-8"))
			emails.append(line.decode("utf-8"))
	
	
for line in emails:
	mailto = re.findall(r'"([^"]*)"', line)
	mailto.pop(0)
	mailtoStr = ''.join(mailto)
	email = str2[7:]
	emailsFormatted.append(email)

	
with open('output.csv', 'w') as out:
	wr = csv.writer(out, quoting=csv.QUOTE_ALL)
	wr.writerow(emailsFormatted)