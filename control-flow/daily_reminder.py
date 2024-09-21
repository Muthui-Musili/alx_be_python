# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize the reminder message
reminder = ""

# Process the task based on priority
match priority:
    case "high":
        reminder = f"'{task}' is a high priority task."
        if time_bound == "yes":
            reminder += " It requires immediate attention today!"
    case "medium":
        reminder = f"'{task}' is a medium priority task."
        if time_bound == "yes":
            reminder += " Don't forget to check on it today."
    case "low":
        reminder = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder += " You might want to do it soon."
    case _:
        reminder = "Invalid priority level. Please enter high, medium, or low."

# Provide a customized reminder
if time_bound == "no":
    reminder += " Consider completing it when you have free time."

print(reminder)
