import random

def generate_team_memberships(conn, users, teams):
    rows = []
    for user in users:
        assigned = random.sample(teams, k=random.randint(1, 2))
        for team in assigned:
            rows.append((user, team))

    conn.executemany(
        "INSERT INTO team_memberships VALUES (?, ?)", rows
    )
    
    users_by_team = {tid: [] for tid in teams}
    for uid, tid in rows:
        users_by_team[tid].append(uid)
        
    return users_by_team
