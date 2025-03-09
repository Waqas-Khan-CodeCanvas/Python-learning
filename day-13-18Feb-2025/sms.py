# from twilio.rest import Client

# # Twilio credentials (replace with your actual details)
# ACCOUNT_SID = ""
# AUTH_TOKEN = ""
# TWILIO_PHONE_NUMBER = ""  # Your Twilio number
# TO_PHONE_NUMBER = ""  # Your mobile number

# def send_sms():
#     client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
#     message = client.messages.create(
#         body="Hello! This is a test message from Twilio using Python.",
#         from_=TWILIO_PHONE_NUMBER,
#         to=TO_PHONE_NUMBER
#     )
    
#     print(f"Message sent! SID: {message.sid}")

# if __name__ == "__main__":
#     send_sms()

# from twilio.rest import Client

# account_sid = ''
# auth_token = ''
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#   from_='+14178073525',
#   body='your for using our calculaiton system',
#   to='+923454640859'
# )

# print(message.sid)