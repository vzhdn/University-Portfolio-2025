from twilio.rest import Client



def notification(o2,bpm):
    account_sid= '****'
    auth_token= '****'
    client= Client(account_sid,auth_token)
    message= client.messages \
        .create(
             body='ENG103<<JJ, Brendan, Vatslav>> Health Alert: Oxegen level is' + int(o2) + 'and BPM is'+ int(bpm) + '.',
             from_='****',
             to='***'
    )
    print(message.sid)

notification(10,20)
