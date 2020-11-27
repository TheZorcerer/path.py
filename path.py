import json
import discord
import command_handler
import bot_utils
import signal
import sys

client = discord.Client()
handler = command_handler.handler(client)

def on_exit(signal, frame):
	bot_utils.save_preferences(client)
	print("closing!")
	sys.exit(0)


@client.event
async def on_ready():
	print("logged in as"+str(client))
	await client.change_presence(activity=discord.Game(name='=gun help'))
	guild_preferences = bot_utils.check_guilds(client)
	client.guild_preferences = guild_preferences

@client.event
async def on_message(message):
	reply = handler.handle(message)
	if(reply != None):
		if(type(reply) == type("never gonna give you up")):
			await message.channel.send(reply)
		else:
			await message.channel.send(embed=reply)

with open("token.txt") as token:
	signal.signal(signal.SIGINT, on_exit)
	client.run(token.read())