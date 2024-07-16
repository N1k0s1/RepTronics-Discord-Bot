id = [1261831251254317066]

import discord
from discord.ext import commands
import json

with open('data.json') as f:
    data = json.load(f)

class Buttons(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot

class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎") # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!") # Send a message when the button is clicked

@discord.slash_command(guild_id = id) # Create a slash command
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView()) # Send a message with our View class that contains the button

def setup(bot):
    bot.add_cog(Buttons(bot))