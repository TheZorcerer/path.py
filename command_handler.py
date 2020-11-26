import discord

class handler():
	def __init__(self,client):
		self.client = client

	def handle(self,message,guild_preferences):
		prefix = guild_preferences[str(message.guild.id)]["prefix"]
		if(message.content[len(prefix):7].lower() == "server"):
			x = message.content.split(" ")
			print(x)
		pass