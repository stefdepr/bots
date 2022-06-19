import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import discord

URL_list = [
    "https://www.vandenborre.be/toebehoren-drones/dji-fly-more-kit-mini-3-pro?gclid=CjwKCAjw77WVBhBuEiwAJ-YoJNGWvR3ByBEHzQKIks4Bw9fGXPs07A-DeyaRJzkwlCtvWEXEMClYgBoCmcAQAvD_BwE", ]
URL_available = "https://www.vandenborre.be/lcd-led-oled-tv/jvc-hd-24-inch-lt-24fd100"
client = discord.Client()
client.run("your token here") #token begrijkpk nie echt goe

def check_price2(URL_list):
    for URL in URL_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.find("div", {"class": "margin-top-5-md margin-top-20"}).text
        text = text.strip()
        # print('1')
        # print(text)
        # print('1')
        if 'Beschikbaar' in text:
            verwittigen(f"drone f{URL}")
            verwittegen_discord(f"drone f{URL}")
        else:
            print('niet beschikbaar')


"""
links voor twilioshit
https://www.freecodecamp.org/news/20-lines-of-python-code-get-notified-by-sms-when-your-favorite-team-scores-a-goal/
https://www.twilio.com/
"""


def verwittigen(message):
    client = Client('ACa8d45d665368dd2f4116fe023ed25ac9', 'e9c73e2f173dafd33bd2e3722274618d')
    client.messages.create(body=message, from_='', to='')

channelid = 0 #get channel id numbers
@client.event
async def verwittegen_discord(message):
    channel = client.get_channel(channelid)
    await channel.send(message)



check_price2(URL_list)
