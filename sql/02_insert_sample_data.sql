-- insert sample data into listening_history_raw table
INSERT INTO listening_history_raw (track_id, track_name, artist_name, album_name, played_at, duration_ms, popularity)
VALUES
    ('track_001', 'Jolene', 'Dolly Parton', 'Jolene', '2025-12-04 20:00:00', 155000, 95),
    ('track_002', 'Shape of You', 'Ed Sheeran', 'Divide', '2025-12-01 18:30:00', 235000, 90),
    ('track_003', 'Lose Yourself', 'Eminem', '8 Mile', '2025-12-02 20:00:00', 326000, 92),
    ('track_004', 'Thinking Out Loud', 'Ed Sheeran', 'X', '2025-12-03 19:15:00', 281000, 88),
    ('track_005', 'Blinding Lights', 'The Weeknd', 'After Hours', '2025-12-05 10:00:00', 200000, 94),
    ('track_006', 'Levitating', 'Dua Lipa', 'Future Nostalgia', '2025-12-05 11:30:00', 203000, 91),
    ('track_007', 'As It Was', 'Harry Styles', 'Harry''s House', '2025-12-05 14:15:00', 173000, 93),
    ('track_008', 'Anti-Hero', 'Taylor Swift', 'Midnights', '2025-12-05 16:45:00', 227000, 95);
