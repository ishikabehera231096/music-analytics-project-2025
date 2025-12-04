import sqlite3

# Connect to the DB
conn = sqlite3.connect("db/raw.sqlite")
cur = conn.cursor()

# Prepare multiple sample rows
songs = [
    ('track_002', 'Shape of You', 'Ed Sheeran', 'Divide', '2025-12-01 18:30:00', 235000, 90),
    ('track_003', 'Lose Yourself', 'Eminem', '8 Mile', '2025-12-02 20:00:00', 326000, 92),
    ('track_004', 'Thinking Out Loud', 'Ed Sheeran', 'X', '2025-12-03 19:15:00', 281000, 88)
]

# Insert multiple rows
cur.executemany("""
INSERT INTO listening_history_raw
(track_id, track_name, artist_name, album_name, played_at, duration_ms, popularity)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", songs)

# Commit the changes
conn.commit()

# --- Basic analytics queries ---

# Total number of songs
cur.execute("SELECT COUNT(*) FROM listening_history_raw")
total_songs = cur.fetchone()[0]
print("Total songs:", total_songs)

# Top artist by number of plays
cur.execute("""
SELECT artist_name, COUNT(*) as plays
FROM listening_history_raw
GROUP BY artist_name
ORDER BY plays DESC
LIMIT 1
""")
top_artist = cur.fetchone()
print("Top artist:", top_artist)

# Total listening time in minutes
cur.execute("SELECT SUM(duration_ms) FROM listening_history_raw")
total_minutes = cur.fetchone()[0] / 60000  # convert ms to minutes
print("Total listening minutes:", total_minutes)

# Close the connection
conn.close()
