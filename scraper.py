import re
import urllib.parse
import urllib.request
import requests
import csv

with open('agents.txt') as f:
    lines = f.readlines()

	
mys = "/scripts/mgrqispi.dll?APPNAME=IMS&PRGNAME=IMSListingAgentDetail"
myn = "<td valign=\"top\"><a href=\"mailto:"
new = []
emailsT = []
emails = []
for line in lines:
	if mys in line:
		murl = re.findall(r'"([^"]*)"', line)
		str1 = ''.join(murl)
		nurl = "https://members.gallatinrealtors.com" + str1
		new.append(nurl)
		

for page in new:
	page = requests.get(page)
	for line in page.iter_lines():
		if line:
			if b'\t\t<td valign="top"><a href="mailto:' in line:
				print(line.decode("utf-8"))
				emailsT.append(line.decode("utf-8"))
	

	
	
for line in emailsT:
	tmp = re.findall(r'"([^"]*)"', line)
	tmp.pop(0)
	str2 = ''.join(tmp)
	st3 = str2[7:]
	emails.append(st3)

	
with open('output.csv', 'w') as myfile:
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerow(emails)