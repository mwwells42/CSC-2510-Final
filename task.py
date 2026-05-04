# DONE: import the datetime library
import datetime

'''
The Task class represents an actionable to-do item. Tasks have descriptive information 
and a status (incomplete, in progress, completed).
'''

class Task:
    def __init__(self, task_name, todays_focus, description, due_date, status, weight, steps, category_name):
        self.task_name = task_name
        self.todays_focus = todays_focus
        self.description = description
        self.due_date = due_date
        self.status = status
        self.weight = weight
        self.steps = steps
        self.category_name = category_name

    # GETTERS / ACCESSORS
    def get_task_name(self):
        return self.task_name
    
    def get_todays_focus(self):
        return self.todays_focus

    def get_description(self):
        return self.description

    def get_due_date(self):
        return self.due_date

    def get_status(self):
        return self.status

    def get_weight(self):
        return self.weight

    def get_steps(self):
        return self.steps

    def get_category_name(self):
        return self.category_name

    # SETTERS / MUTATORS
    def set_task_name(self, new_data):
        self.task_name = new_data
    
    def set_todays_focus(self):
        if self.todays_focus:
            self.todays_focus = False
        else:
            self.todays_focus = True

    def set_description(self, new_data):
        self.description = new_data

    def set_due_date(self, new_data):
        self.due_date = new_data

    def set_status(self, new_data):
        self.status = new_data

    def set_weight(self, new_data):
        self.weight = new_data

    def set_steps(self, new_data):
        self.steps = new_data

    def set_category_name(self, new_data):
        self.category_name = new_data

    def to_dict(self):
        new_dict = {
            "task_name": self.task_name,
            "todays_focus": self.todays_focus,
            "description": self.description,
            "due_date": self.due_date,
            "status": self.status,
            "weight": self.weight,
            "steps": self.steps,
            "category_name": self.category_name
        }
        return new_dict

    @staticmethod
    def from_dict(dictionary):
        new_task = Task(
            dictionary["task_name"],
            dictionary["todays_focus"],
            dictionary["description"],
            dictionary["due_date"],
            dictionary["status"],
            dictionary["weight"],
            dictionary["category_name"],
            dictionary["steps"],
        )
        return new_task

    # DONE: Write a methdo called update_task that accepts all attributes as arugments. It then sets
    #       each of the Task object's attributes to the given arguments. If any of the arugments was
    #       not given a value, the should be set to None as default. The attributes should only be 
    #       updated if a value was passed.
    def update_task(self, task_name=None, todays_focus=None, description=None, due_date=None, status=None, weight=None, category_name=None, steps=None):
        if task_name != None:
            self.task_name = task_name
        if todays_focus != None:
            self.todays_focus = todays_focus
        if description != None:
            self.description = description
        if due_date != None:
            self.due_date = due_date
        if status != None:
            self.status = status
        if weight != None:
            self.weight = weight
        if category_name != None:
            self.category_name = category_name
        if steps != None:
            self.steps = steps
            
    # DONE: Write a method called is_overdue that accepts a date object as an argument representing 
    #       today's date. If the task was not given a due date or if the status is completed, return false. 
    #       Otherwise, format the due date with the following equation:
    #           due date = datetime.date.fromisoformat(Task object's due date)
    #       Use the datetime call exactly as it was given to you. After formatting, make sure the today 
    #       argument is populated. If the argument is Nonetype, set it equal to datetime.date.today()
    #       Finally, return true if the due date is less than today's date or false if not.
    def is_overdue(self, today=None):
        if not self.due_date or self.status == "completed":
            return False
        due_date = datetime.date.fromisoformat(self.due_date)
        if not today:
            today = datetime.date.today()
        if due_date < today:
            return True
        return False
        
    ###################################
    #       Step Managment            #
    ###################################

    # DONE: Write a method called add_step that is passed a step title as an argument.
    #       It then creates a new step and adds it to the Task's list of steps.
    #       Steps are each a dictionary with the keys "step" and "status". The "step" key
    #       should have the value of the title sent as an argument. The "status" key should
    #       be set to "incomplete" when created.
    def add_step(self, title):
        new_step = {
            "step": title,
            "status": "incomplete"
            }
        self.steps.append(new_step)

    # DONE: Write a method called toggle_step that accepts a step index as an argument.
    #       The specified step's status should be set according to the following key.
    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''
    def toggle_step(self, index):
        target = self.steps[index]
        if target["status"] == "incomplete":
            target["status"] = "started"
        elif target["status"] == "started":
            target["status"] = "completed"
        elif target["status"] == "completed":
            target["status"] = "incomplete"



    # DONE: Write a method called edit_step that accepts a step index and a new title as arugments.
    #       The specified step should be updated.
    def edit_step(self, index, new_title):
        self.steps[index]["step"] = new_title

    # DONE: Write a method called remove_step that accepts a step index as an argument.
    #       The specified step should be removed from the Task's list of steps.
    def remove_step(self, index):
        self.steps.pop(index)