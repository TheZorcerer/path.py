import discord

class handler():
	def __init__(self,client):
		self.client = client

	def handle(self,message):
		prefix = self.client.guild_preferences[str(message.guild.id)]["prefix"]
		if(message.content[:len(prefix)] == prefix):
			return self.handler(message,prefix)


	def handler(self,message,prefix):
		data = message.content.split(" ")
		module = data[0][len(prefix):7].lower()
		if(module == "server"):
			return self.server(message)
		pass

	def server(self,message):
		data = message.content.split(" ")
		if(str(message.author.id) == "358869991459782666"):
			if(data[1] == "prefix"):
				self.client.guild_preferences[str(message.guild.id)]["prefix"] = data[2]
				return "I have changed the prefix to " + data[2]
		else:
			return "You aint tazer"