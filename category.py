'''
The Category class groups related tasks and events together. It provides organizational 
structure within the planner.
'''

class Category:
    def __init__(self, category_name, description):
        self.category_name = category_name
        self.description = description

    # GETTERS / ACCESSORS
    def get_category_name(self):
        return self.category_name

    def get_description(self):
        return self.description
        
    # SETTERS / MUTATORS
    def set_category_name(self, new_data):
        self.category_name = new_data

    def set_description(self, new_data):
        self.description = new_data
        
    def to_dict(self):
        new_dict = {
            "category_name": self.category_name,
            "description": self.description
        }
        return new_dict
    
    @staticmethod
    def from_dict(dictionary):
        new_category = Category(
            dictionary["category_name"],
            dictionary["description"]
        )
        return new_category