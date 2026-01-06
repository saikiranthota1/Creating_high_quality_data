import random
from datetime import datetime, timedelta

def random_past_date(months=6):
    now = datetime.now()
    delta = timedelta(days=random.randint(1, months * 30))
    return now - delta

def completion_after(created_at):
    return created_at + timedelta(days=random.randint(1, 14))
