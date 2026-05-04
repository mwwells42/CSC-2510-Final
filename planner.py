# DONE: import the task, category, and event classes
from event import Event
from category import Category
from task import Task 
# DONE: import the datetime library
import datetime

'''
The Planner class is the central coordinating component of the system. It owns and manages 
all categories, tasks, and events. Most application behavior ultimately routes through this class.
'''

# DONE: create a Planner class
class Planner:
    # DONE: write a constructor with the attributes name, categories, tasks, and events.
    #       Each of these attributes will be passed in as arguments. They should be set
    #       to each of the attributes accordingly.
    #       If categories, tasks, or events were passed as Nonetypes, set them equal to 
    #       an empty list.
    def __init__(self, name="", categories=[], tasks=[], events=[]):
        self.name = name
        self.categories = categories
        self.tasks = tasks
        self.events = events

    # DONE: write the getters and setters for each of the attributes. They must have the format
    #       "get_attributeName" or "set_attributeName"
    
    # GETTERS / ACCESSORS
    def get_name(self):
        return self.name

    def get_categories(self):
        return self.categories

    def get_tasks(self):
        return self.tasks

    def get_events(self):
        return self.events

    # SETTERS / MUTATORS
    def set_name(self, new_data):
        self.name = new_data

    def set_categories(self, new_data):
        self.categories = new_data

    def set_tasks(self, new_data):
        self.tasks = new_data

    def set_events(self, new_data):
        self.events = new_data
        
    def to_dict(self):
        new_dict = {
            "name": self.name,
            "categories": [],
            "tasks": [],
            "events": []
        }

        # for categories, tasks, and events in the planner object, turn them in to dictionaries and 
        # append them

        for category_obj in self.categories:
            new_dict["categories"].append(category_obj.to_dict())

        for task_obj in self.tasks:
            new_dict["tasks"].append(task_obj.to_dict())

        for event_obj in self.events:
            new_dict["events"].append(event_obj.to_dict())

        return new_dict

    @staticmethod
    def from_dict(dictionary):
        tasks = []
        categories = []
        events = []

        # for categories, tasks, and events in the planner dictionary, turn them in to objects and
        # append them

        for category_dict in dictionary["categories"]:
            categories.append(Category.from_dict(category_dict))

        for task_dict in dictionary["tasks"]:
            tasks.append(Task.from_dict(task_dict))

        for event_dict in dictionary["events"]:
            events.append(Event.from_dict(event_dict))

        return Planner(dictionary["name"], categories, tasks, events)
    

    #########################################
    #            Task Methods               #
    #########################################
    def create_task(self, task_name, todays_focus, description, due_date, status, weight, category_name):
        new_task = Task(
            task_name,
            todays_focus,
            description,
            due_date,
            status,
            weight,
            [],
            category_name
        )
        self.tasks.append(new_task)

    '''
     Current Status          New Status
    ------------------------------------
     incomplete       ->      started
     started          ->      completed
     completed        ->      incomplete
    '''
    def set_task_status(self, index):
        task = self.tasks[index]
        if task.status == "incomplete":
            task.status = "started"
        elif task.status == "started":
            task.status = "completed"
        else:
            task.status = "incomplete"

    def set_task_todays_focus(self, index):
        task = self.tasks[index]
        task.set_todays_focus()

    # DONE: Write a method called delete_task that will take an index as an argument. It will then delete
    #       the task at that index for the Planner object
    def delete_task(self, index):
        self.tasks.pop(index)

    # DONE: Write a method called add_task_step that will take in a task index and a step title as arguments.
    #       It will then call the add_step method on the Task object at the specified index in the Planner's 
    #       task list.
    def add_task_step(self, index, title):
        self.tasks[index].add_step(title)

    # DONE: Write a method called toggle_task_step that takes in a task index and a step index as arguments.
    #       It will then call the toggle_step method on the Task object at the specified index in the Planner's
    #       task list.
    def toggle_task_step(self, task_index, step_index):
        self.tasks[task_index].toggle_step(step_index)

    # DONE: Write a method called edit_task_step that takes a task index, a step index, and a new step title 
    #       as arguments. It will then call the edit_step method on the specified Task object.
    def edit_task_step(self, task_index, step_index, step_title):
        self.tasks[task_index].edit_step(step_index, step_title)

    # DONE: Write a method called remove_task_step that will take a task index and a step index as arguments.
    #       It will then call the remove_step on the specified Task object.
    def remove_task_step(self, task_index, step_index):
        self.tasks[task_index].remove_step(step_index)

    # DONE: Write a method called edit_task that will take a task index, task name, focus bool, description, 
    #       due date, status, and weight as arguments. Call the update_task method on the specified Task.
    def edit_task(self, index, name, focus, description, due_date, status, weight):
        self.tasks[index].update_task(name, focus, description, due_date, status, weight)

    # DONE: Write a method called get_task_by_index that accepts a task index as an arugment.
    #       It should return the specified task from the Planner's task list.
    def get_task_by_index(self, index):
        return self.tasks[index]

    # DONE: Write a method called get_overdue tasks that accepts a date object as the argument representing today.
    #       You will need a list to store the overdue tasks. For each task in the Planner's task list, determine if 
    #       the task is overdue using the is_overdue method. If it is, add it to the list of overdue tasks and return 
    #       the list when done.
    def get_overdue_tasks(self, today):
        overdue_tasks = []
        for task in self.tasks:
            if task.is_overdue(today):
                overdue_tasks.append(task)
        return overdue_tasks

    # DONE: Write a method called get_due_soon that accepts a date object as the argument representing today. This method
    #       will search for any tasks due within a week. To do so, find the date 7 days from now with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the tasks in the
    #       Planner.  If the task's due date is greater than or equal to today's and less than or equal to the end of the week,
    #       add it to the list of tasks due soon and return when done. Tasks that were not given a due date or are already
    #       completed should not be added to the list.
    def get_due_soon(self, today):
        due_soon = []
        if today is None:
            today = datetime.date.today()
        end_date = today + datetime.timedelta(days=7)
        for task in self.tasks:
            if task.due_date and task.status != "completed":
                due_date = datetime.date.strptime(task.due_date, "%Y-%m-%d")
                if due_date >= today and due_date <= end_date:
                    due_soon.append(task)
        return due_soon

    # DONE: Write a method called get_tasks_in_todays_focus. For each task in the Planner's task list, add it to a list
    #       collecting tasks where the todays_focus is set to True. Return the list of tasks in today's focus.
    def get_tasks_in_todays_focus(self):
        focus_tasks = []
        for task in self.tasks:
            if task.todays_focus:
                focus_tasks.append(task)
        return focus_tasks

    # DONE: write a method called get_task_status_counts. It should create a dictionary with each status as a key. The
    #       count for each status should start at a 0. For each task in the Planner, increment the count for the correct
    #       status in the dictionary. Return the dictionary when done.
    def get_task_status_counts(self):
        task_statuses = {
            "incomplete": 0,
            "started": 0,
            "completed": 0
        }
        for task in self.tasks:
            if task.status == "incomplete":
                task_statuses["incomplete"] += 1
            elif task.status == "started":
                task_statuses["started"] += 1
            elif task.status == "completed":
                task_statuses["completed"] += 1
        return task_statuses

    # DONE: Write a method called get_incomplete_by_category. It should create a dictionary with each category as a key.
    #       There should also be a variable to count the number of not complete tasks. The count for each category should 
    #       start at 0. For each task in the Planner, increment the count for the category that task is in only if the status
    #       is not "completed". Return a dictionary that has 2 key-value pairs: one pair has the key "total" with the value 
    #       of the number of tasks that are not complete and another pair with the key "byCategory" that has the value of the
    #       dictionary.
    def get_incomplete_by_category(self):
        task_statuses = {
            "incomplete": 0,
            "started": 0,
            "completed": 0
        }
        not_completed_tasks = 0
        for task in self.tasks:
            if task.status == "incomplete":
                task_statuses["incomplete"] += 1
                not_completed_tasks += 1
            elif task.status == "started":
                task_statuses["started"] += 1
                not_completed_tasks += 1
            elif task.status == "completed":
                task_statuses["completed"] += 1
        return {
            "total": not_completed_tasks,
            "byCategory": task_statuses
        }

    #########################################
    #          Category Methods             #
    #########################################

    # DONE: Write a method called get_category_by_index that is passed a category index as an argument. Return
    #       the requested Category object from the Planner's list of categories
    def get_category_by_index(self, index):
        return self.categories[index]

    # DONE: Write a method called add_category that accepts a name and description as arugments.
    #       Create a new Category object and add it to the Planner's list of categories.
    def add_category(self, name, description):
        new_category = Category(name, description)
        self.categories.append(new_category)

    # DONE: Write a method called edit_category that accepts a category index, name and description
    #       as arguments. It will then call the setters for the specified Category object.
    def edit_category(self, index, name, description):
        self.categories[index].set_category_name(name)
        self.categories[index].set_description(description)

    # DONE: Write a method called remove_category_by_index that accepts a category index as an argument.
    #       It then remvoes the specified Category object from the Planner's list of categories.
    def remove_category_by_index(self, index):
        self.categories.pop(index)

    #########################################
    #            Event Methods              #
    #########################################

    # DONE: Write a method called get_event_by_index that accepts an index as an argument. It then
    #       returns the specified Event object from the Planner's list of events.
    def get_event_by_index(self, index):
        return self.events[index]

    # DONE: Write a method called add_event that accepts an event name, description, date, start time,
    #       end time, and category name as arguments. It then creates a new Event object and adds it 
    #       to the Planner's list of events.
    def add_event(self, event_name, description, date, start_time, end_time, category_name):
        new_event = Event(event_name, description, date, start_time, end_time, category_name)
        self.events.append(new_event)

    # DONE: Write a method called remove_event_by_index that accepts an index as an argument. It then
    #       removes the specified index from the Planner's list of events.
    def remove_event_by_index(self, index):
        self.events.pop(index)

    # DONE: Write a method called set_event_category that accepts an event index and a category name. 
    #       Set the corresponding Event object's category to the specified category name.
    def set_event_category(self, event_index, category_name):
        self.events[event_index].set_category_name(category_name)

    # DONE: Write a method called get_upcoming_events that accepts a date object as the arument representing
    #       today's date. It should calculate the date exactly 7 days from today with the equation:
    #       end date = today's date + datetime.timedelta(days=7)
    #       Use the datetime call exactly as it was provided to you. You will then need to iterate through the
    #       Planner's list of events. Collect all events in a list where there is a date and the date is greater
    #       than or equal to today and less than or equal to 7 days from now. Return the list of events happening
    #       within the next week.
    def get_upcoming_events(self, today):
        upcoming = []
        end_date = today + datetime.timedelta(days=7)
        for event in self.events:
            if event.date:
                if event.date >= today and event.date <= end_date:
                    upcoming.append(event)
        return upcoming

    # DONE: write a method called get_todays_events that accepts a date object as an argument representing
    #       today's date. Iterate throught the Planner's list of events to find event's who's date matches
    #       today's date. Collect those events in a list and return them.
    def get_todays_events(self, today):
        todays_events = []
        for event in self.events:
            if event.date == today:
                todays_events.append(event)
        return todays_events
