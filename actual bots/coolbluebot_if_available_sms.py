import requests
from bs4 import BeautifulSoup
import smtplib
import time
import re
from twilio.rest import Client

list_URL = ["https://www.coolblue.be/nl/product/906024/dji-mini-3-pro-smart-controller.html"]


def check_price2(URL_list):
    for URL in URL_list:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0'}
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        text = soup.find("div", {"class": "section--3"}).text
        text = text.strip()
        # print('1')
        print(text)
        # print('1')
        if text == 'Tijdelijk uitverkocht':
            pass
        else:
            verwittigen(message=f"drone kopen, link: {URL}")


"""
links voor twilioshit
https://www.freecodecamp.org/news/20-lines-of-python-code-get-notified-by-sms-when-your-favorite-team-scores-a-goal/
https://www.twilio.com/
"""
def verwittigen(message):
    client = Client('ACa8d45d665368dd2f4116fe023ed25ac9', 'e9c73e2f173dafd33bd2e3722274618d')
    client.messages.create(body=message, from_='+18507714732',to='+32468117544')

