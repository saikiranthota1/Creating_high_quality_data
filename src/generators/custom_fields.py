from utils.ids import gid
import random

def generate_custom_fields(conn, project_ids, task_ids):
    fields = []
    values = []

    for pid in project_ids:
        priority_id = gid()
        effort_id = gid()

        fields.extend([
            (priority_id, "Priority", "enum", pid),
            (effort_id, "Effort", "number", pid)
        ])

        for tid in random.sample(task_ids, k=int(len(task_ids) * 0.4)):
            values.append((tid, priority_id, random.choice(["Low", "Medium", "High"])))
            values.append((tid, effort_id, str(random.randint(1, 8))))

    conn.executemany(
        "INSERT INTO custom_field_definitions VALUES (?, ?, ?, ?)", fields
    )
    conn.executemany(
        "INSERT INTO custom_field_values VALUES (?, ?, ?)", values
    )
