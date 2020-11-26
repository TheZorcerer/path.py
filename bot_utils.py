import discord
import json

def check_guilds(client):
	f = open("guild_prefs.json")
	guild_preferences = json.load(f)
	for guild in client.guilds:
		if(str(guild.id) not in list(guild_preferences.keys())):
			print("new guild with ID",guild.id)
			guild_preferences[guild.id] = {"allowed_channels":[],"on":True,"prefix":"="}
	f.close()
	f = open("guild_prefs.json","w+")
	json.dump(guild_preferences,f)
	f.close()
	return guild_preferences