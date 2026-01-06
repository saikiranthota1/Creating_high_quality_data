from faker import Faker
from utils.ids import gid
from utils.dates import random_past_date

fake = Faker()

def generate_users(conn, n):
    users = []
    for _ in range(n):
        uid = gid()
        users.append((
            uid,
            fake.name(),
            fake.email(),
            fake.job(),
            random_past_date()
        ))
    conn.executemany(
        "INSERT INTO users VALUES (?, ?, ?, ?, ?)", users
    )
    return [u[0] for u in users]
