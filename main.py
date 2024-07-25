id = [1261831251254317066]
allowed_users = [1136290556591485039, 978886408964026378]
import discord
bot = discord.Bot()
import asyncio
from embedbuttons import Gen2View, Gen3View, Pro1View, Pro2View, MaxesView, SellersView
from discord.ext import tasks
import json 
with open('data.json') as f:
    data = json.load(f)

@tasks.loop()
async def status_task() -> None:
    await bot.change_presence(status="Reading the Ultimate Guide", activity=discord.Streaming(name="Ultimate Guide", url="https://weare.reptronics.top/blog/"))
    await asyncio.sleep(60)

@bot.event
async def on_ready():
    status_task.start()
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

@bot.slash_command(name="quiz", description="Sends link to quiz", guild_id = id)
async def quiz(ctx):
    await ctx.respond("https://weare.reptronics.top/category/quiz/")

@bot.slash_command(guild_id = id)
async def ping(ctx):
    await ctx.respond(f"Pong! ({bot.latency*1000}ms)")

@bot.slash_command(guild_id = id)
async def sync(ctx):
    if ctx.author.id in allowed_users:
        await bot.sync_commands()
        await ctx.respond("Successfully synced commands")
    else:
        await ctx.respond("You do not have permission to use this command.")

# COMMANDS FOR THE CHIP MENU

@bot.slash_command(name="gen2", description="Show the gen 2 menu", guild_id = id)
async def gen2(ctx):
    await ctx.respond('Gen 2 chips - Choose an option:', view=Gen2View())

@bot.slash_command(name="gen3", description="Show the gen 3 menu", guild_id = id)
async def gen3(ctx):
    await ctx.respond('Gen 3 chips - Choose an option:', view=Gen3View())

@bot.slash_command(name="pro1", description="Show the pro 1 menu", guild_id = id)
async def pro1(ctx):
    await ctx.respond('Pro 1 chips - Choose an option:', view=Pro1View())

@bot.slash_command(name="pro2", description="Show the pro 2 menu", guild_id = id)
async def pro2(ctx):
    await ctx.respond('Pro 2 chips - Choose an option:', view=Pro2View())

@bot.slash_command(name="maxes", description="Show the maxes menu", guild_id = id)
async def maxes(ctx):
    await ctx.respond('Maxes Models - Choose an option:', view=MaxesView())

# COMMAND FOR SELLERS
@bot.slash_command(name="sellers", description="Information about sellers", guild_id = id)
async def sellers(ctx):
    await ctx.respond('Sellers: Choose an option.', view=SellersView())

@bot.slash_command(name='ts', description='Sends the user a survey', guild_id = id)
async def send_survey(ctx, user: discord.Member):
    survey_data = data['misc']['survey_message']
    embed = discord.Embed(
        title=survey_data['title'],
        description=survey_data['description'].replace('[user_mention]', user.mention),
        color=discord.Color.blue()
    )
    await user.send(embed=embed)
    await ctx.send(f"Survey sent to {user.display_name}.")

bot.run('')