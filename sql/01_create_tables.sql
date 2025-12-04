CREATE TABLE IF NOT EXISTS listening_history_raw(
 track_id text PRIMARY KEY,
 track_name text,
 artist_name text,
 album_name text,
 played_at text,
 duration_ms integer,
 popularity integer )