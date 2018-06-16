import discord
import os
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import pip
import random
import textwrap
from contextlib import redirect_stdout
from discord.ext import commands
import json
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),description="Specialized bot made for HWCWL.\n\nHelp Commands",owner_id=277981712989028353)
bot.remove_command("help")
cmds = 0


def cleanup_code(content):
    # remove ```py\n```
    if content.startswith('```') and content.endswith('```'):
        return '\n'.join(content.split('\n')[1:-1])

    return content.strip('` \n')
    
  
@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    await bot.change_presence(activity=discord.Game(name="with HWCWL! | .help"))


@bot.event
async def on_command(ctx):
	cmds += 1


@bot.command()
async def help(ctx, command=None):
	if command is None:
		color = discord.Color(value=0x00ff00)
		em = discord.Embed(color=color, title='HWCWL Bot')
		em.description = 'Thank you for using the HWCWL Discord bot. Here are a list of commands to use for me.'
		em.add_field(name="ping", value="Gets the bot's websocket latency.")
		# em.add_field(name="clanlist", value="Gets the list of clans added to this bot.")
		# em.add_field(name="claninfo [clan name]", value="Gets information of a clan by its clan name.")
		# em.add_field(name="warinfo [clan name]", value="Gets information of a clan's current war, by its name.")
		em.add_field(name="info", value="Get info related to HWCWL.")
		em.add_field(name="divisionsinfo", value="Get information related to the divisions in HWCWL.")
		em.add_field(name="rules", value="Gets the HWCWL S2 rules and league structure.")
		em.add_field(name="s2gfx", value="Gets GFX links for season 2 HWCWL.")
		em.add_field(name="dates", value="Important dates for season 2!")
		em.add_field(name="signup", value="Get the form to sign up.")
		em.add_field(name="stats", value="Stats of me!")
		em.add_field(name="invite", value="Invite link to bring me to your server!")
		em.add_field(name="s2hogslegacy", value="Brackets and schedule for Hogs Legacy division")
		em.add_field(name="s2bowlersrush", value="Brackets and schedule for Bowlers Rush division")
		em.add_field(name="s2lavaflyers", value="Brackets and schedule for Lava Flyers division")
		em.add_field(name="s2witchesdominion", value="Brackets and schedule for Witches Dominion division")
		em.set_thumbnail(url='https://media.discordapp.net/attachments/398628125593960449/450379699261014046/HWCWL_MAIN_LOGO_C.png')
		await ctx.send(embed=em)
	else:
		if command.lower() == 'ping':
			color = discord.Color(value=0x00ff00)
			em = discord.Embed(color=color, title='ping')
			em.description = 'Gets the websocket latency for the bot.\nA latency higher than 100 ms usually means a slower response.'
			await ctx.send(embed=em)
		if command.lower() == 'clanlist':
			color = discord.Color(value=0x00ff00)
			em = discord.Embed(color=color, title='clanlist')
			em.description = 'Gets a list of clans that are added to the bot.\nYou may type `?claninfo [clan name]`, by replacing [clan name] with the name of a clan on this list.\n\nIf your clan is not yet on the list, notify dat banana boi #1982 or TiTAN|HWCWL|CNA #8672 to update it.'
			await ctx.send(embed=em)
		if command.lower() == 'claninfo':
			color = discord.Color(value=0x00ff00)
			em = discord.Embed(color=color, title='claninfo [clan name]')
			em.description = 'Gets clan info for a given clan name.\nType `?claninfo [clan name]` and replace [clan name] with a name of a clan.\nAll the clans supported by this command are listed in the command `?clanlist`.\nPlease make sure you type the name correctly.'
			await ctx.send(embed=em)
		if command.lower() == 'warinfo':
			color = discord.Color(value=0x00ff00)
			em = discord.Embed(color=color, title='warinfo [clan name]')
			em.description = "Gets the current info of a clan war.\nType `?warinfo [clan name]`, replacing [clan name] with the name of a clan.\nAll the clans supported by this command are listed in the command `?clanlist`."
			await ctx.send(embed=em)
		else:
			await ctx.send('Command not found. To view all commands, type `?help`.')


@bot.command()
async def stats(ctx):
	color = discord.Color(value=0x00ff00)
	em = discord.Embed(color=color, title='HWCWL Bot Stats')
	em.add_field(name="Servers", value=f"{len(bot.guilds)}")
	em.add_field(name="Latency", value=f"{bot.latency * 1000:.4f}")
	em.add_field(name="Users", value=f"{len(bot.users)}")
	em.add_field(name="Latency", value=f"{bot.latency * 1000:.4f}")
	em.add_field(name="Commands Run (Since Uptime)", value=cmds)
	await ctx.send(embed=em)


@bot.command()
async def info(ctx):
	await ctx.send("Heavy Weight Clan War League, we are one of the first league's who brought heavy weight divisions into the Esports scene. We brought a new meta by announcing 1 hit and 2 hit divisions!")



@bot.command()
async def invite(ctx):
	await ctx.send("https://discordapp.com/oauth2/authorize?client_id=409708279980228608&permissions=2048&scope=bot")



# @bot.command()
# async def divisioninfo(ctx):
# 	await ctx.send(textwrap.dedent("""
# 	**Hogs Legacy** :- 5/0/0
# 	**Witches Dominion** :- 4/4/2
# 	**Bowlers Rush** :- 3/10/12
# 	**Lava Flyers** :- 4/12/14
# 	**Wizards Unite** :- 6/14/15
# 		"""))


@bot.command(aliases=['divisionsinfo'])
async def divisioninfo(ctx):
	await ctx.trigger_typing()
	#em = discord.Embed(color=discord.Color(value=0x00ff00), title="HWCWL S2 Division Info")
	#em.set_image(url="https://images-ext-1.discordapp.net/external/oBPsCELAryOBWXCkzgPbRrzZhvQsay4y4Y1DSzf-TbY/https/cdn.discordapp.com/attachments/414003663623946251/450243436734316544/division_info.png")
	await ctx.send(textwrap.dedent("""
		**Hogs Legacy** :- 2/3/0/0
		**WitchesDominion** :- 2/2/3/3
		**Bowlers Rush** :- 0/3/10/12
		**Lava Flyers** :- 0/4/12/14
		**Wizards Unite** :- 0/6/14/15"""))


@bot.command()
async def rules(ctx):
	await ctx.send("**Rules**\nhttp://bit.ly/HWCWLs2Rules")


@bot.command()
async def signup(ctx):
	await ctx.send("**Sign-Up Form**\nhttp://bit.ly/s2sign-upform")


@bot.command()
async def dates(ctx):
	await ctx.send(textwrap.dedent("""
		**27th May**: Sign-ups starts
		**24th June**: Sign-ups ends
		**26th June**: Clan Selection 
		**15th July**: s2 starts
		"""))


@bot.command()
async def s2gfx(ctx):
	await ctx.send("**GFX**\nhttp://bit.ly/HWCWLs2Gfx")


@bot.command(aliases=['s2bowlersrush', 's2lavaflyers', 's2witchesdominion'])
async def s2hogslegacy(ctx):
	await ctx.send("Brackets and schedule will be out soon!")



@bot.command()
async def ping(ctx):
    """Premium ping pong giving you a websocket latency."""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='PoIIIng! Your supersonic latency is:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)


bot.run(os.environ.get("TOKEN")) 