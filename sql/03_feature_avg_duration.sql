SELECT
  artist_name,
  AVG(duration_ms)      AS avg_duration_ms,
  COUNT(*)              AS track_count
FROM listening_history_raw
GROUP BY artist_name
ORDER BY avg_duration_ms DESC;