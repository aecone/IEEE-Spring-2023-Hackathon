# bot.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

bot = commands.Bot(command_prefix="!")
@bot.command() 
async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send("Hello there " + username)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    


client.run(TOKEN)
