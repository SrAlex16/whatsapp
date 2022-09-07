from random import random, choice
from twilio.rest import Client
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests

app = Flask(__name__)

# Frase por defecto que sale en https://5fb4-78-136-67-170.eu.ngrok.io
@app.route("/")
def hello():
    return "Hello, World!"

# Respuesta automatica

@app.route("/whatsapp", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""

    # Fetch the message
    msg = request.form.get('Body')

    # Create reply
    resp = MessagingResponse()
    resp.message("Has dicho: {}".format(msg))

    if msg == "/meme":
        print("mando meme")
        mensaje = resp.message("Meme")
        mandarMeme()
    if msg =="/mandarMemeUri":
        mandarMemeUri()
    else:
        print("comando no reconocido")
        mensaje = resp.message("Comando no reconocido")

    return str(resp)

def mandarMeme():
    print("mandarMeme()")
    # COJO EL MEME ALEATORIO
    memeUrl = choice(open('./memes_url.txt').read().splitlines())

    print("URL MEME: " + memeUrl)
    message = client.messages.create(
        media_url=memeUrl,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

def mandarMemeUri():
    print("mandarMeme()")
    # COJO EL MEME ALEATORIO
    memeUrl = choice(open('./memes_url.txt').read().splitlines())

    print("URL MEME: " + memeUrl)
    message = client.messages.create(
        media_uri="C:\\Users\\aleja\\OneDrive\\Documentos\\GitHub\\whatsapp_bot\\images\\1.png",
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

    media = Client.media("C:\\Users\\aleja\\OneDrive\\Documentos\\GitHub\\whatsapp_bot\\images\\1.png")

def mandarFrase():
    print("mandarFrase()")
    # COJO EL MEME ALEATORIO
    fraseGlados = choice(open('./glados_frases.txt').read().splitlines())

    print("URL MEME: " + fraseGlados)
    message = client.messages.create(
        media_url=fraseGlados,
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )

# DATOS PARA CONECTARME A LA API
account_sid = "AC2255b4363e83ab0b722e73963b07fd7f"
auth_token = "2beeff695a1adce85170878d684e27c2"

client = Client(account_sid, auth_token)

from_whatsapp_number = "whatsapp:+14155238886"
to_whatsapp_number = "whatsapp:+34674742564"

message = client.messages.create(
         body="[Pon /meme]",
         from_=from_whatsapp_number,
         to=to_whatsapp_number
     )



if __name__ == "__main__":
    app.run(debug=False)