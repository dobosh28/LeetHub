# Write your MySQL query statement below
SELECT 
    machine_id,
    ROUND(AVG(duration), 3) AS processing_time
FROM (
    SELECT
        machine_id,
        process_id,
        MAX(CASE WHEN activity_type = 'end' THEN timestamp ELSE 0 END) 
        - MAX(CASE WHEN activity_type = 'start' THEN timestamp ELSE 0 END) AS duration
    FROM Activity
    GROUP BY machine_id, process_id
) AS process_durations
GROUP BY machine_id;
