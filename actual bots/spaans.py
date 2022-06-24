#selenium necessary

import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import discord
from discord.ext import commands
from discord import client
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed

URL_list = ["https://www.elcorteingles.es/electronica/A43607025-kit-accesorios-dji-para-mini-3-pro-vuela-mas/#"]
URL_available = ["https://www.elcorteingles.es/moda-mujer/A41279639-bandana-blanco-con-estampado-de-lunares/"]


def check_price2(URL_list):
    for URL in URL_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        btn = soup.find("div", {"class": "js-sticky-control js-sticky"})
        print(btn)



        """
        if "Beschikbaar" in btn_text:
            verwittigen(f"drone \n{URL}")
            activate_bot(f"drone \n{URL}")
            #webhook(f"drone \n{URL}")
            webhook_2(soup=soup, url=URL)
        else:
            print('niet beschikbaar')
        """

def verwittigen(message):
    client = Client('ACa8d45d665368dd2f4116fe023ed25ac9', 'e9c73e2f173dafd33bd2e3722274618d')
    client.messages.create(body=message, from_='', to='')


def activate_bot(message):
    TOKEN = "OTg4MDY0ODk4NzQxMzI5OTQw.GR3ZGq.dQeoqo9UyK2Z7KbgQdxhRowYNAnYX2qcjq7aKc"  # new token

    bot = commands.Bot(command_prefix="!")

    @bot.event
    async def on_ready():
        channel = bot.get_channel(988063268172091406)
        await channel.send(message)

    bot.run(TOKEN)


discord_webhook_url = "https://discord.com/api/webhooks/988105584874229841/TAbhr09sV0KdxX8ihk4zQO56CXpd6b1rw5nblcgo0afXxMzmg0cn_UJ3fVvllpPDKPRB"


def webhook(message):
    message_real = {"content": message}
    requests.post(discord_webhook_url, data=message_real)


def webhook_2(soup, url):
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    image_link = images[-1]
    image_link_correct = 'https://' + str(image_link[2:])
    discord_webhook_url = "https://discord.com/api/webhooks/988105584874229841/TAbhr09sV0KdxX8ihk4zQO56CXpd6b1rw5nblcgo0afXxMzmg0cn_UJ3fVvllpPDKPRB"

    webhook = DiscordWebhook(url=discord_webhook_url)
    # add layout
    layout = DiscordEmbed(title='Klik hier', description='De drone is beschikbaar', color='03b2f8', url=url)
    layout.set_author(name='Klingzie')
    layout.set_thumbnail(url=image_link_correct)
    layout.set_timestamp()
    webhook.add_embed(layout)
    response = webhook.execute()

check_price2(URL_list)

#