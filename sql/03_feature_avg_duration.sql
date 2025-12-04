DROP TABLE IF EXISTS analytics_artist_features;

CREATE TABLE analytics_artist_features (
  artist_name TEXT PRIMARY KEY,
  avg_duration_ms FLOAT,
  track_count INTEGER,
  last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO analytics_artist_features (artist_name, avg_duration_ms, track_count)
SELECT
  artist_name,
  AVG(duration_ms)      AS avg_duration_ms,
  COUNT(*)              AS track_count
FROM listening_history_raw
GROUP BY artist_name
ORDER BY avg_duration_ms DESC;