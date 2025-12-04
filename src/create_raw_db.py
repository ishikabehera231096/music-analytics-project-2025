import sqlite3
import os

# Ensure db folder exists at the root of the project
db_path = "db/raw.sqlite"
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect to SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Create the table
cur.execute("""
CREATE TABLE IF NOT EXISTS listening_history_raw (
    track_id TEXT PRIMARY KEY,
    track_name TEXT,
    artist_name TEXT,
    album_name TEXT,
    played_at TEXT,
    duration_ms INTEGER,
    popularity INTEGER
)
""")

conn.commit()
conn.close()

print(f"Database created at {db_path} and table listening_history_raw is ready!")
