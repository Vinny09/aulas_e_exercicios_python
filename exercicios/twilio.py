from twilio.rest import Client

# Substitua com suas credenciais do Twilio
account_sid = 'AC29bdcaa1923e3e01741367d15fb9a62d'
auth_token = '8c2f0cb391c08bf24b881bcbb8ee7ba3'

# Inicialize o cliente do Twilio
client = Client(account_sid, auth_token)

# Envie uma mensagem do WhatsApp
message = client.messages.create(
    body='Olá, em breve entraremos em contato contigo!',
    from_='whatsapp:+14155238886',
    to='whatsapp:+5511989781139'
)

print(message.sid)