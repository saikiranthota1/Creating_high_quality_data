import sqlite3
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv()

def inspect_db():
    db_path = os.getenv("DB_PATH")
    if not os.path.exists(db_path):
        print(f"Database not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    
    tables = [
        "users", "teams", "projects", "sections", "tasks", 
        "comments", "tags"
    ]
    
    print(f"--- Database Inspection: {db_path} ---")
    
    for table in tables:
        try:
            count = pd.read_sql_query(f"SELECT COUNT(*) FROM {table}", conn).iloc[0, 0]
            print(f"\nTable: {table} ({count} rows)")
            
            if count > 0:
                print("Sample data:")
                df = pd.read_sql_query(f"SELECT * FROM {table} LIMIT 3", conn)
                print(df.to_string(index=False))
        except Exception as e:
            print(f"Could not read table {table}: {e}")

    conn.close()

if __name__ == "__main__":
    inspect_db()
