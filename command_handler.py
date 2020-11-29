import discord
import data
import bot_utils

class handler():
	def __init__(self,client):
		self.client = client
		self.gun_data = data.Data()

	def handle(self,message):
		prefix = self.client.guild_preferences[str(message.guild.id)]["prefix"]
		if(message.content[:len(prefix)] == prefix):
			return self.handler(message,prefix)


	def handler(self,message,prefix):
		data = message.content.split(" ")
		module = data[0][len(prefix):7].lower()
		if(module == "server"):
			return self.server(message)
		elif(module == "gun"):
			return self.gun(message)
		return None

	def server(self,message):
		data = message.content.split(" ")
		if(str(message.author.id) == "358869991459782666"):
			if(data[1] == "prefix"):
				self.client.guild_preferences[str(message.guild.id)]["prefix"] = data[2]
				return "I have changed the prefix to " + data[2]
			elif(data[1] == "allow"):
				self.client.guild_preferences[str(message.guild.id)]["allowed_channels"].append(str(message.channel.id))
				return "added channel with id" + str(message.channel.id)
		else:
			return "You aint tazer"

	def gun(self,message):
		if(str(message.channel.id) in self.client.guild_preferences[str(message.guild.id)]["allowed_channels"]):
			data = message.content.split(" ")
			if(data[1].lower() == "help"):
				try:
					if(data[2]):
						return bot_utils.weapon_help(self.gun_data.weapons,data[2])
				except IndexError:
					pass
				return bot_utils.weapon_help(self.gun_data.weapons,"1")
			weapon_data = self.gun_data.search(data[1])
			name,weapon_data = weapon_data[0],weapon_data[1]
			if(weapon_data == None):
				return None
			else:
				try:
					firerate = str(weapon_data['fr']) + " rpm"
				except KeyError:
					firerate = "Not Available"
				try:
					reld = str(weapon_data["reload"]) + "s"
				except KeyError:
					reld = "Not Available"
				try:
					ads = str(weapon_data["ads"]) + " ms"
				except KeyError:
					ads = "Not Available"
				mag = weapon_data["mag"]
				max_ammo = weapon_data["maxAmmo"]
				embed = bot_utils.build_gun_embed(name,mag,max_ammo,reld,firerate,ads)
				return embed
		else:
			return "Bot is not allowed in this channel"

	def gulag(self,message):
		pass
