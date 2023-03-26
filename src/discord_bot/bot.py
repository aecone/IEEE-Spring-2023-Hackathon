# bot.py
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("The bot is now online!")

class MenuButton(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.value = None
        
    @discord.ui.button(label="Easy", style=discord.ButtonStyle.green)
    async def menu(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Here is an easy problem!")
        
    @discord.ui.button(label="Medium", style=discord.ButtonStyle.blurple)
    async def menu2(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Here is an medium problem!")
    
    @discord.ui.button(label="Hard", style=discord.ButtonStyle.red)
    async def menu3(self, button: discord.ui.Button, interaction: discord.Interaction):
        await interaction.response.send_message("Here is an hard problem!")
        
    
@bot.command()
async def problem(ctx):
    view = MenuButton()
    await ctx.reply("Choose your difficulty", view=view) 

#@bot.tree.command(name="buttonmenu")
#async def buttonmenu(interaction: discord.Interaction):
#    await interaction.response.send_message(content="Here's my button menu!", view=MenuButton())

bot.run("MTA4OTIxMjc1NjU0NjMwNjE3OQ.GriBA-.CzaUhc6g3crX3uH-3QtkG9UbuMBWHXmkfRi2X0")