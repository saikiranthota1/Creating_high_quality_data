
from utils.ids import gid
from utils.dates import random_past_date
import random

def generate_projects(conn, team_ids):
    projects = []
    for tid in team_ids:
        for i in range(5):
            projects.append((
                gid(),
                f"Q{i+1} Initiative",
                tid,
                "Sprint",
                random_past_date()
            ))
    conn.executemany(
        "INSERT INTO projects VALUES (?, ?, ?, ?, ?)", [p[:5] for p in projects]
    )
    
    return {
        p[0]: {
            "team_id": p[2],
            "function": "Engineering", 
            "completion_rate": random.uniform(0.3, 0.9)
        }
        for p in projects
    }
    
