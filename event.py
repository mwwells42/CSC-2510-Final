'''
The Event class represents a scheduled occurrence such as a meeting, appointment, 
or gathering. Unlike tasks, events are typically tied to a specific date or time 
and do not have progress states.
'''

class Event:
    def __init__(self, event_name, description, date, start_time, end_time, category_name):
        self.event_name = event_name
        self.description = description
        self.date = date
        self.start_time = start_time
        self.end_time = end_time
        self.category_name = category_name

    # GETTERS / ACCESSORS
    def get_event_name(self):
        return self.event_name
    
    def get_description(self):
        return self.description
    
    def get_date(self):
        return self.date
    
    def get_start_time(self):
        return self.start_time
    
    def get_end_time(self):
        return self.end_time
    
    def get_category_name(self):
        return self.category_name
    
    # SETTERS / MUTATORS
    def set_event_name(self, new_data):
        self.event_name = new_data

    def set_description(self, new_data):
        self.description = new_data

    def set_date(self, new_data):
        self.date = new_data

    def set_start_time(self, new_data):
        self.start_time = new_data

    def set_end_time(self, new_data):
        self.end_time = new_data

    def set_category_name(self, new_data):
        self.category_name = new_data

    def to_dict(self):
        new_dict = {
            "event_name": self.event_name,
            "description": self.description,
            "date": self.date,
            "start_time": self.start_time,
            "end_time": self.end_time,
            "category_name": self.category_name
        }
        return new_dict
    
    @staticmethod
    def from_dict(dictionary):
        new_event = Event(
            dictionary["event_name"],
            dictionary["description"],
            dictionary["date"],
            dictionary["start_time"],
            dictionary["end_time"],
            dictionary["category_name"]
        )
        return new_event