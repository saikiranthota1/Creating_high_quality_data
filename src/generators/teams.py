from utils.ids import gid

FUNCTIONS = ["Engineering", "Marketing", "Operations"]

def generate_teams(conn, org_id):
    teams = []
    for fn in FUNCTIONS:
        for i in range(10):
            tid = gid()
            teams.append((tid, f"{fn} Team {i+1}", org_id, fn))
    conn.executemany(
        "INSERT INTO teams VALUES (?, ?, ?, ?)", teams
    )
    return [t[0] for t in teams]
