import os
import logging
from dotenv import load_dotenv
from utils.db import connect
from utils.logger import setup_logging
from utils.ids import gid
from generators.users import generate_users
from generators.teams import generate_teams
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks
from generators.custom_fields import generate_custom_fields
from generators.attachments import generate_attachments

load_dotenv()

def main():
    setup_logging()
    logging.info("Starting Asana Simulation...")
    
    db_path = os.getenv("DB_PATH")
    if os.path.exists(db_path):
        os.remove(db_path)
    conn = connect(db_path)

    with open("schema.sql") as f:
        conn.executescript(f.read())

    org_id = gid()
    conn.execute(
        "INSERT INTO organizations VALUES (?, ?, CURRENT_TIMESTAMP)",
        (org_id, os.getenv("ORG_NAME"))
    )

    users = generate_users(conn, int(os.getenv("EMPLOYEE_COUNT")))
    teams = generate_teams(conn, org_id)
    users_by_team = generate_team_memberships(conn, users, teams)

    projects = generate_projects(conn, teams)
    sections_by_project = generate_sections(conn, list(projects.keys()))

    task_ids = generate_tasks(conn, projects, users_by_team, sections_by_project)
    generate_custom_fields(conn, list(projects.keys()), task_ids)
    generate_attachments(conn, task_ids)

    conn.commit()
    conn.close()
    logging.info("Asana Simulation completed successfully.")


if __name__ == "__main__":
    main()
