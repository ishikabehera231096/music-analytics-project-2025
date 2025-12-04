import sqlite3

# Connect to your DB
conn = sqlite3.connect("db/raw.sqlite")
cur = conn.cursor()

# Insert one sample row
cur.execute("""
INSERT INTO listening_history_raw
(track_id, track_name, artist_name, album_name, played_at, duration_ms, popularity)
VALUES
('track_001', 'Jolene', 'Dolly Parton', 'Jolene', '2025-12-04 20:00:00', 155000, 95)
""")

# Commit the change
conn.commit()

# Query the table to check
cur.execute("SELECT * FROM listening_history_raw")
rows = cur.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()
