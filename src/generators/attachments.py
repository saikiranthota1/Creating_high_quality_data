from utils.ids import gid
from utils.dates import random_past_date
import random

FILES = ["spec.pdf", "design.png", "notes.docx"]

def generate_attachments(conn, task_ids):
    rows = []
    for tid in random.sample(task_ids, k=int(len(task_ids) * 0.2)):
        rows.append((
            gid(),
            tid,
            random.choice(FILES),
            random_past_date()
        ))

    conn.executemany(
        "INSERT INTO attachments VALUES (?, ?, ?, ?)", rows
    )
