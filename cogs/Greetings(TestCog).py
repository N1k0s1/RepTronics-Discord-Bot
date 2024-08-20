id = [1261831251254317066]

import discord
from discord.ext import commands

class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="goodbye", description="Says Goodbye!", guild_ids= id)
    async def goodbye(self, ctx):
        await ctx.respond('Goodbye!')

    @discord.slash_command(name="hello", description="Says hello to a member of your choice", guild_ids= id)
    async def greet(self, ctx, member: discord.Member):
        await ctx.respond(f'{ctx.author.mention} says hello to {member.mention}!')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Welcome to the server!')

def setup(bot):
    bot.add_cog(Greetings(bot))