from twilio.rest import Client
client =Client()
FromWhatsappNumber = 'whatsapp:+917283876336'
ToWhatsappNumber = 'whatsapp:+919664876062'

client.messages.create(body = "Hey Gandu",from_ = FromWhatsappNumber,to = ToWhatsappNumber)