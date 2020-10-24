import json
import sys
import os
import unittest

database_dir = '/MyDatabaseDirectory'

def save_json(obj, file, indent=4, sort_keys=True):
    with open(file, 'w') as f:
        json.dump(obj, f, sort_keys=sort_keys, indent=indent)

class Request:
	'''
	User Request to add certain plants to database
	'''
	def __init__(self, new_plant, description=None, Username='NoName', Emailadress=None):
		self.name = Username
		self.mail = Emailadress
		self.plant_name = new_plant
		self.comment = description
		
		assert isinstance(self.plant_name, str), 'the plant name should be string'

	def save(self): 
		json_dict = dict()
		json_dict['Username'] = self.name
		json_dict['User_email'] = self.mail
		json_dict['plant_to_add'] = self.plant_name
		json_dict['User_comment'] = self.comment
		save_json(json_dict,database_dir)

	def repeat_plant_name(self):
		return self.plant_name

if __name__ == "__main__":
	plant_name = sys.argv[1]
	user_req = Request(new_plant=plant_name)