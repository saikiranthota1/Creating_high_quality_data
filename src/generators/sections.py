from utils.ids import gid

DEFAULT_SECTIONS = ["Backlog", "In Progress", "Review", "Done"]

def generate_sections(conn, project_ids):
    sections = []
    for pid in project_ids:
        for name in DEFAULT_SECTIONS:
            sections.append((gid(), name, pid))
    conn.executemany(
        "INSERT INTO sections VALUES (?, ?, ?)", sections
    )
    
    sections_by_project = {}
    for sid, _, pid in sections:
        if pid not in sections_by_project:
            sections_by_project[pid] = []
        sections_by_project[pid].append(sid)
        
    return sections_by_project
