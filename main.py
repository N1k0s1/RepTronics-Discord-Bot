id = [1261831251254317066]
import discord
bot = discord.Bot()
#Testing
import json 
with open('data.json') as f:
    data = json.load(f)
from embed import genembed, sellerembed

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    await bot.sync_commands()
    print(f"Succesfully synced commands")

@bot.slash_command(name="loadcog", description= "Loads a cog of the users choosing", guild_id = id)
async def cogs(ctx, cogs):
    if cogs in cogs:
        bot.load_extension(f'cogs.{cogs}')
        await ctx.respond(f"Successfully loaded {cogs}")
    else:
        await ctx.respond("Cog not found")
#    elif:
        
@bot.slash_command(name="unloadcog", description= "Unloads a cog of the users choosing", guild_id = id)
async def cogs(ctx, cogs):
    if cogs in cogs:
        bot.unload_extension(f'cogs.{cogs}')
        await ctx.respond(f"Successfully unloaded {cogs}")
    else:
        await ctx.respond("Cog not found")
#    elif:

@bot.slash_command(guild_id = id)
async def ping(ctx):
    await ctx.respond(f"Pong! ({bot.latency*1000}ms)")

@bot.slash_command(guild_id = id)
async def sync(ctx): 
    await bot.sync_commands()
    await ctx.respond(f"Succesfully synced commands")

# TESTING!!!

class MyView(discord.ui.View):
    @discord.ui.button(label="Click me!", style=discord.ButtonStyle.primary, emoji="😎")
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("You clicked the button!")

@bot.slash_command(name="button", description= "Uses a button of the users choosing", guild_id = id)
async def button(ctx):
    await ctx.respond("This is a button!", view=MyView())



class Gen2View(discord.ui.View):
    def __init__(self):
        super().__init__()

    @discord.ui.button(label='JL', custom_id='JL')
    async def on_button1(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | JL", "gen2jl")
        await interaction.response.send_message('JL', embed=embed1, ephemeral=True)

    @discord.ui.button(label='Airoha 1562U', custom_id='1562U')
    async def on_button2(self, button: discord.ui.Button, interaction: discord.Interaction):
        embed1 = genembed("Gen 2 | Airoha 1562U", "gen21562u")
        await interaction.response.send_message('1562U', embed=embed1, ephemeral=True)
    # Repeat for the other buttons

@bot.slash_command(name="gen2test", description="Show the gen 2 menu", guild_id = id)
async def gen2test(ctx):
    await ctx.respond('Gen 2 chips - Choose an option:', view=Gen2View())





bot.run('')