from mailjet_rest import Client
import os

API_KEY = "222608684c590c76a082499702d4e21d"		# username
SECRET_KEY = "1a1e2806664c9775bc131029024094a2"		# password

SENDER_EMAIL = "2019503059@smartinternz.com"
RECIPIENT_EMAIL = "pvs1135.3@gmail.com"
USERNAME = "pvs"

mailjet = Client(auth=(API_KEY, SECRET_KEY), version='v3.1')
data = {
  'Messages': [
				{
						"From": {
								"Email": SENDER_EMAIL,
								"Name": "Team: PNT2022TMID35705"
						},
						"To": [
								{
										"Email": RECIPIENT_EMAIL,
										"Name": USERNAME
								}
						],
						"Subject": "Welcome to Personal Expense Tracker",
						"TextPart": "Greetings from Team: PNT2022TMID35705",
						"HTMLPart": "<h3>Dear customer, welcome to Personal Expense Tracker</h3> <br /> Track your daily, monthly and yearly expenses!"
				}
		]
}
result = mailjet.send.create(data=data)
print (result.status_code)
print (result.json())

