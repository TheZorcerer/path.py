import json

class Data(object):
	def __init__(self):
		with open("data/gunsmith-weapons.json") as f1:
			with open("data/gunsmith-attachments.json") as f2:
				self.weapons_data = json.load(f1)
				self.attachments_data = json.load(f2)
				f1.close()
				f2.close()
		self.weapons = list()
		for weapon in self.weapons_data:
			self.weapons.append((weapon['name'],weapon['id']))
		self.path_data = dict()
		for n in range(len(self.weapons_data)):
			self.path_data[self.weapons[n][1]] = self.weapons_data[n]['path']
	def search(self,name):
		for weapon in self.weapons:
			if(weapon[0].lower() == name.lower() or weapon[1].lower() == name.lower()):
				return weapon[0],self.path_data[weapon[1]]
		return None

