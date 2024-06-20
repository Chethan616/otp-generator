import random
from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from encrypt.env file
load_dotenv(dotenv_path='encrypt.env')

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

if not account_sid or not auth_token:
    raise ValueError("Twilio account SID and auth token must be set as environment variables.")

number = input("Enter phone number: ")
otp = random.randint(1000, 9999)
client = Client(account_sid, auth_token)

msg = client.messages.create(
    body=f"Your OTP is {otp}",
    from_="++17744794828",
    to=f"+91{number}"
)

enterOtp = input("Enter the OTP: ")

if enterOtp.isdigit() and int(enterOtp) == otp:
    print("OTP is correct")
else:
    print("Incorrect OTP, please try again.")
