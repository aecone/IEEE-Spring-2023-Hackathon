# bot.py
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("The bot is now online!")

@bot.command()
async def hello(ctx):
    username = ctx.message.author.name
    await ctx.send("Hello " + username)

bot.run("MTA4OTIxMjc1NjU0NjMwNjE3OQ.GriBA-.CzaUhc6g3crX3uH-3QtkG9UbuMBWHXmkfRi2X0")