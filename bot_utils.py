import discord
import json

def check_guilds(client):
	f = open("guild_prefs.json")
	guild_preferences = json.load(f)
	for guild in client.guilds:
		if(str(guild.id) not in list(guild_preferences.keys())):
			print("new guild with ID",guild.id)
			guild_preferences[guild.id] = {"allowed_channels":[],"on":True,"prefix":"="}
	client.guild_preferences = guild_preferences
	f.close()
	f = open("guild_prefs.json","w+")
	json.dump(guild_preferences,f)
	f.close()
	return guild_preferences

def save_preferences(client):
	with open("guild_prefs.json","w") as f:
		json.dump(client.guild_preferences,f)
		f.close()
	print("saved it!")

def build_gun_embed(name,mag,maxammo,reld,firerate,ads):
	embed = discord.Embed(title=name, description="Stats on the "+name+" courtesy path.exe and PatchyTheDog.", color=0x00ff00)
	embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/781241634822029312/781799759576170516/gath.png")
	embed.add_field(name = "Magazine Capacity",value = mag,inline=False)
	embed.add_field(name = "Reserve Ammo",value = maxammo,inline=False)
	embed.add_field(name = "Reload Time",value = reld,inline=False)
	embed.add_field(name = "Firerate",value = firerate,inline=False)
	embed.add_field(name = "ADS Time",value = ads,inline=False)
	embed.set_footer(text = "Made by TaZeR/zahran#5909")
	return embed

def weapon_help(weapons,page):
	try:
		if(int(page)*10 > len(weapons)):
			return "Not a valid page"
		else:
			page = int(page)
	except ValueError:
		return "Not a valid page"
	embed = discord.Embed(title="All Weapons",description="The list of all weapons and the associated id's. You can use the id to search for them by =gun <id>",color=0x00ff00)
	for n in range((page-1)*10,min((page)*10+1,len(weapons)+1)):
		embed.add_field(name = str(n+1)+". "+ weapons[n][0], value = "ID: "+weapons[n][1],inline=False)
	embed.set_footer(text = "Use =gun help <page> for the next set of weapons")
	return embed