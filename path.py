import json
import discord
import command_handler
import bot_utils

client = discord.Client()
handler = command_handler.handler(client)


@client.event
async def on_ready():
	print("logged in as"+str(client))
	guild_preferences = bot_utils.check_guilds(client)
	client.guild_preferences = guild_preferences

@client.event
async def on_message(message):
    handler.handle(message,client.guild_preferences)

with open("token.txt") as token:
	client.run(token.read())