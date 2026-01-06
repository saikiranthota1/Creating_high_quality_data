import random
from utils.ids import gid
from utils.dates import random_past_date, completion_after
from utils.task_text import task_name

SECTION_NAMES = ["Backlog", "In Progress", "Review", "Done"]

def generate_tasks(conn, projects, users_by_team, sections_by_project):
    tasks = []
    subtasks = []

    for project_id, meta in projects.items():
        team_users = users_by_team[meta["team_id"]]
        sections = sections_by_project[project_id]

        for _ in range(random.randint(80, 150)):
            created = random_past_date()
            completed = random.random() < meta["completion_rate"]

            assignee = None
            # Heuristic: 15% of tasks are unassigned (per Asana benchmarks)
            # Assignees are chosen from the project's owning team
            if team_users and random.random() > 0.15:
                assignee = random.choice(team_users)

            task_id = gid()
            tasks.append((
                task_id,
                task_name(meta["function"]),
                "Auto-generated realistic task description.",
                project_id,
                random.choice(sections),
                assignee,
                None,
                random.choice([None, None, None, created.date()]), # Heuristic: ~25% have due dates
                created,
                completed,
                completion_after(created) if completed else None
            ))

            # Subtasks (~25%)
            if random.random() < 0.25:
                for _ in range(random.randint(1, 3)):
                    subtasks.append((
                        gid(),
                        "Subtask - implementation detail",
                        None,
                        project_id,
                        random.choice(sections),
                        assignee,
                        task_id,
                        None,
                        created,
                        completed,
                        None
                    ))

    conn.executemany(
        "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
        tasks + subtasks
    )

    return [t[0] for t in tasks]
