from utils.ids import gid
from utils.dates import random_past_date
import random

def generate_comments(conn, task_ids, user_ids):
    comments = []
    for tid in task_ids:
        for _ in range(random.randint(0, 3)):
            comments.append((
                gid(),
                tid,
                random.choice(user_ids),
                "Looks good to me.",
                random_past_date()
            ))
    conn.executemany(
        "INSERT INTO comments VALUES (?, ?, ?, ?, ?)", comments
    )
