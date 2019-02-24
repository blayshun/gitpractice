import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client

account_sid = 'ACf0bf41663308316c7256a1c0278db1af'
auth_token = 'eb2900084815ee4632f7c295f658bacd'
client = Client(account_sid, auth_token)
tnumber = '+15405546517'
cnumber = '+16789824773'

while True:
	html = requests.get('https://owlexpress.kennesaw.edu/prodban/bwckschd.p_disp_detail_sched?term_in=201901&crn_in=12124')

	soup = BeautifulSoup(html.text, 'html.parser')

	for caption in soup.find_all('caption'):
		if caption.get_text() == 'Registration Availability':
			table = caption.find_parent('table', {'class': 'datadisplaytable'})

	for tr in table.find_all('tr')[1:]:
		available = tr.find_all('td')[2].text.strip()

	if available == '0':
		print('CLASS IS UNAVAILABLE')
		time.sleep(5)

	elif available != '0':
		message = client.messages \
						.create(
							body ="YOUR CLASS IS AVAILABLE!!!",
							from_= tnumber,
							to = cnumber
						)
		print('''
		||||||||||||||||||||||||||||||||
		vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv

		YOUR CLASS IS AVAILABLE!!!

		^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
		|||||||||||||||||||||||||||||||||
		''')
		break
