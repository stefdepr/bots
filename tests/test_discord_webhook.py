import requests

discord_webhook_url = "https://discord.com/api/webhooks/988105584874229841/TAbhr09sV0KdxX8ihk4zQO56CXpd6b1rw5nblcgo0afXxMzmg0cn_UJ3fVvllpPDKPRB"

message = {"content": "Hello"}

requests.post(discord_webhook_url, data=message)