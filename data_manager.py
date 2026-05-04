from planner import Planner
import json

'''
The Data_Manager class handles persistence. It is responsible for loading planner 
data from storage and saving planner data back to storage.
'''

class Data_Manager:
    def __init__(self, file_path):
        self.file_path = file_path
    def open_planner(self):
        with open(self.file_path, 'r') as file:
            raw = file.read()
            planner_dict = json.loads(raw)
            planner_obj = Planner.from_dict(planner_dict)
            return planner_obj

    def save_planner(self, planner):
        with open(self.file_path, 'w') as file:
            planner = planner.to_dict()
            json.dump(planner, file)
