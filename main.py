import discord
from discord.ext import commands, tasks
import os
import asyncio
import json
from embed import create_survey_embed
from embedbuttons import Gen2View, Gen3View, Pro1View, Pro2View, MaxesView, SellersView
from dotenv import load_dotenv
import logging

# Load environment variables
load_dotenv("token.env")
bot_token = os.getenv("DISCORD_BOT_TOKEN")

# Load data from JSON file
with open('data.json') as f:
    data = json.load(f)

# Load IDs from ids.json
with open('ids.json') as f:
    ids = json.load(f)

# Constants
id = ids["id"]
allowed_users = ids["allowed_users"]
allowed_channel_id = ids["allowed_channel_id"]
admin = ids["admin"]
ts_users = ids["ts_users"]
channel_exempt = ids["channel_exempt"]

# Initialize bot
bot = commands.Bot()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[
    logging.FileHandler("bot.log"),
    logging.StreamHandler()
])

@tasks.loop(seconds=20)
async def status_task() -> None:
    guild = bot.get_guild(id)
    if guild:
        member_count = guild.member_count
        await bot.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name=f"{member_count} members!"))
        await asyncio.sleep(20)
        await bot.change_presence(status=discord.Status.online, activity=discord.Streaming(name="Ultimate Guide", url="https://weare.reptronics.top/blog/"))
    else:
        logging.warning("Guild not found")

@bot.event
async def on_ready():
    status_task.start()
    print(f"We have logged in as {bot.user}")
    await bot.sync_commands()
    print(f"Succesfully synced commands")
    try:
        user = await bot.fetch_user(admin)
        if user:
            embed = discord.Embed(title="Bot Status", description="The RepTronics discord bot is currently online!!", color=discord.Color.green())
            embed.set_footer(text="Bot created by apringle", icon_url="https://styles.redditmedia.com/t5_38xyy/styles/communityIcon_mk1i0se5yboa1.png")
            await user.send(embed=embed)        
        else:
            print("User not found")
    except Exception as e:
        print(f"Error fetching user: {e}")

async def notify_admin(ctx, message):
    try:
        user = await bot.fetch_user(admin)
        if user:
            embed = discord.Embed(title="Notification", description=message, color=discord.Color.blue())
            await user.send(embed=embed)
    except Exception as e:
        print(f"Error notifying admin: {e}")

@bot.slash_command(name="loadcog", description="Loads a cog of the user's choosing", guild_id=id)
async def loadcog(ctx, *, cog: str):
    if ctx.author.id in allowed_users:
        try:
            bot.load_extension(f"cogs.{cog}")
            await ctx.send(f"Successfully loaded cog: {cog}")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        except Exception as e:
            await ctx.send(f"Error while loading cog: {cog}\n{e}")
        await notify_admin(ctx, f"{ctx.author} used the loadcog command.")
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)
        embed = discord.Embed(title="Permission Error", description=f"{ctx.author} tried to use the loadcog command without permission.", color=discord.Color.red())
        await notify_admin(ctx, embed=embed)

@bot.slash_command(name='unloadcog', description= "Unloads a cog of the users choosing", guild_id = id)
async def unload(ctx, *, cog: str):
    if ctx.author.id in allowed_users:
        try:
            bot.unload_extension(f"cogs.{cog}")
            await ctx.send(f"Unloaded cog: {cog}")
        except commands.ExtensionNotFound:
            await ctx.send("Cog not found")
        except Exception as e:
            await ctx.send(f"Error while unloading cog: {cog}\n{e}")
        await notify_admin(ctx, f"{ctx.author} used the unloadcog command.")
    else:
        await ctx.send("You do not have permission to use this command.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the unloadcog command without permission.")

@bot.slash_command(name="quiz", description="Sends link to quiz", guild_id=id)
async def quiz(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        embed = discord.Embed(title="AirPod Quizzes", description="Click [here](https://weare.reptronics.top/category/quiz/) to take the quiz!", color=discord.Color.green())
        embed.set_footer(text="Bot created by apringle", icon_url="https://styles.redditmedia.com/t5_38xyy/styles/communityIcon_mk1i0se5yboa1.png")
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the quiz command in the wrong channel.")

@bot.slash_command(guild_id = id)
async def ping(ctx):
    embed = discord.Embed(title="Pong!", description=f"Latency: {bot.latency*1000}ms", color=discord.Color.green())
    embed.set_footer(text="Bot created by apringle", icon_url="https://styles.redditmedia.com/t5_38xyy/styles/communityIcon_mk1i0se5yboa1.png")
    await ctx.respond(embed=embed)

@bot.slash_command(guild_id = id)
async def sync(ctx):
    if ctx.author.id in allowed_users:
        await bot.sync_commands()
        await ctx.respond("Successfully synced commands")
        await notify_admin(ctx, f"{ctx.author} used the sync command.")
    else:
        await ctx.respond("You do not have permission to use this command.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the sync command without permission.")

# COMMANDS FOR THE CHIP MENU

@bot.slash_command(name="gen2", description="Show the gen 2 menu", guild_id = id)
async def gen2(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        await ctx.respond('Gen 2 chips - Choose an option:', view=Gen2View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the gen2 command in the wrong channel.")

@bot.slash_command(name="gen3", description="Show the gen 3 menu", guild_id = id)
async def gen3(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        await ctx.respond('Gen 3 chips - Choose an option:', view=Gen3View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the gen3 command in the wrong channel.")

@bot.slash_command(name="pro1", description="Show the pro 1 menu", guild_id = id)
async def pro1(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        await ctx.respond('Pro 1 chips - Choose an option:', view=Pro1View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the pro1 command in the wrong channel.")

@bot.slash_command(name="pro2", description="Show the pro 2 menu", guild_id = id)
async def pro2(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        await ctx.respond('Pro 2 chips - Choose an option:', view=Pro2View())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the pro2 command in the wrong channel.")

@bot.slash_command(name="maxes", description="Show the maxes menu", guild_id = id)
async def maxes(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        await ctx.respond('Maxes Models - Choose an option:', view=MaxesView())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the maxes command in the wrong channel.")

# COMMAND FOR SELLERS
@bot.slash_command(name="sellers", description="Information about sellers", guild_id = id)
async def sellers(ctx):
    if ctx.channel.id == allowed_channel_id or ctx.author.id in channel_exempt:
        await ctx.respond('Sellers: Choose an option.', view=SellersView())
    else:
        await ctx.respond("This command can only be used in a specific channel.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the sellers command in the wrong channel.")

@bot.slash_command(name='ts', description='Sends the user a survey', guild_id=id)
async def send_survey(ctx, user: discord.Member):
    if ctx.author.id in ts_users:
        survey_data = data['misc']['survey_message']
        embed = create_survey_embed(user, survey_data)
        await user.send(embed=embed) 
        embed1 = discord.Embed(title="Ticket Survey", description=f"Ticket Survey sent to {user.display_name}.", color=discord.Color.green())
        await ctx.respond(embed=embed1)
        await notify_admin(ctx, f"{ctx.author} used the send_survey command.")
    else:
        await ctx.respond("You do not have permission to use this command.", ephemeral=True)
        await notify_admin(ctx, f"{ctx.author} tried to use the send_survey command without permission.")

        @bot.event
        async def on_message(message):
            if "AR Sellers Websites" in message.content:
                seller = "example_seller"
                response = f"Hey there, we've noticed you're referencing AR. Our website for {seller} is example_website.com"
                await message.channel.send(response)
            elif "AR Versioning" in message.content:
                version = "example_version"
                response = f"Hey there, we've noticed you're referencing AR. Our versioning for that chip is {version}"
                await message.channel.send(response)
            await bot.process_commands(message)

# @bot.slash_command(name="modmail" description="Sends a message to the modmail channel", guild_id=id)
#

bot.run(bot_token)