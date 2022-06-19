import requests
import discord_webhook
from bs4 import BeautifulSoup
from discord_webhook import DiscordWebhook, DiscordEmbed

url = "https://www.vandenborre.be/toebehoren-drones/dji-fly-more-kit-mini-3-pro?gclid=CjwKCAjw77WVBhBuEiwAJ-YoJNGWvR3ByBEHzQKIks4Bw9fGXPs07A-DeyaRJzkwlCtvWEXEMClYgBoCmcAQAvD_BwE"

#get images
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')
images = []
for img in soup.findAll('img'):
    images.append(img.get('src'))
image_link = images[-1]
image_link_correct = 'https://' + str(image_link[2:])

discord_webhook_url = "https://discord.com/api/webhooks/988105584874229841/TAbhr09sV0KdxX8ihk4zQO56CXpd6b1rw5nblcgo0afXxMzmg0cn_UJ3fVvllpPDKPRB"

webhook = DiscordWebhook(url=discord_webhook_url)
#add layout
layout = DiscordEmbed(title='Klik hier', description='De drone is beschikbaar', color='03b2f8', url=url)
layout.set_author(name='Klingzie')
layout.set_thumbnail(url=image_link_correct)
layout.set_timestamp()
webhook.add_embed(layout)
response = webhook.execute()