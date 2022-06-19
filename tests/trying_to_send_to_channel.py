import discord

channelid = 988063268172091406
klingzie_token = "452600928076300289"
client = discord.Client()

@client.event
async def verwittigen_discord(message):
    channel = client.get_channel(channelid)
    await channel.send(message)

client.run(klingzie_token)


