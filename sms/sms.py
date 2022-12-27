from email import message
from http import client
from twilio.rest import Client
import keys

Client = Client(keys.account_sid, keys.auth_token)

message = Client.messages.create(
    body= "Segue o email do curso: ""<p>https://programadorfaixapreta.club.hotmart.com/t</p>",
    from_= keys.twilio_number,
    to= keys.target_number
)
print(message.body)