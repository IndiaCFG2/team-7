from twilio.rest import Client


account_sid = 'ACb509d200fbfd37b8d26d99620a61e985'
auth_token = 'b8be08d19afe7ea48dd81af445e2bc12'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="https://google.com",
                     from_='+13344024332',
                     to='+919398756446'
                 )
print(message.sid)