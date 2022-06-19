from discord.ext import commands, tasks
from discord import Client
import asyncio

TOKEN = "OTg4MDY0ODk4NzQxMzI5OTQw.GxL5HY.b72blskJiqQwnKdegHZz11AY8Z-hiyYb9E6ntM"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f"{bot.user} succesfully logged in!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content == 'hello':
        await message.channel.send(f"Hi {message.author}")
    if message.content ==  'bye':
        await message.channel.send(f"Goodbye {message.author}")

    await bot.process_commands(message)

bot.run(TOKEN)


