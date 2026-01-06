import random

VERBS = ["Implement", "Design", "Review", "Test", "Refactor", "Update", "Create"]
NOUNS = ["API", "Schema", "Frontend", "Backend", "Button", "Form", "Database"]

def task_name(function):
    return f"{random.choice(VERBS)} {random.choice(NOUNS)} for {function}"
