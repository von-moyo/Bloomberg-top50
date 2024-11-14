from collections import defaultdict
import heapq

class TodoList:
    def __init__(self):
        # Initialize user tasks and a global task counter
        self.user_tasks = defaultdict(list)  # Stores tasks for each user in a min-heap by due date
        self.user_tagged_tasks = defaultdict(lambda: defaultdict(list))  # Maps user to tags to tasks
        self.completed_tasks = set()  # Stores completed task IDs
        self.task_id_counter = 1  # Counter for assigning task IDs
        self.task_info = {}  # Dictionary to store task details by task ID

    def addTask(self, userId, taskDescription, dueDate, tags):
        task_id = self.task_id_counter
        self.task_id_counter += 1

        # Store task information
        task = {
            "id": task_id,
            "description": taskDescription,
            "due_date": dueDate,
            "tags": tags,
            "completed": False
        }
        self.task_info[task_id] = task

        # Add task to user's tasks heap (sorted by due date)
        heapq.heappush(self.user_tasks[userId], (dueDate, task_id))

        # Map the task under each tag for the specific user
        for tag in tags:
            heapq.heappush(self.user_tagged_tasks[userId][tag], (dueDate, task_id))

        return task_id

    def getAllTasks(self, userId):
        tasks = []
        
        # Retrieve tasks for user sorted by due date, and filter out completed ones
        for due_date, task_id in self.user_tasks[userId]:
            if task_id not in self.completed_tasks:
                tasks.append(self.task_info[task_id]["description"])
        
        return tasks

    def getTasksForTag(self, userId, tag):
        tasks = []

        # Retrieve tasks under the given tag for the user, sorted by due date
        if tag in self.user_tagged_tasks[userId]:
            for due_date, task_id in self.user_tagged_tasks[userId][tag]:
                if task_id not in self.completed_tasks:
                    tasks.append(self.task_info[task_id]["description"])

        return tasks

    def completeTask(self, userId, taskId):
        # Mark task as complete only if it exists for the user and is not already completed
        if taskId in self.task_info and not self.task_info[taskId]["completed"]:
            self.task_info[taskId]["completed"] = True
            self.completed_tasks.add(taskId)


# Time Complexities:
# - Add a Task: O(logT)
# - Get all Tasks: O(T)
# - get tasks for a tag: O(Ttag)
# - complete a Task: O(1)

# Space Complexity: O(U x T + U x Ttag) where U is the number of users, T is the number of tasks per user, and T tag is the number of tagged tasks per user.