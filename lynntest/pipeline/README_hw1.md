
docker build --no-cache -t ingest_hw1:v001  -f Dockerfile_hw1 .
 docker run -it --rm --network=pipeline_default ingest_hw1:v001 ingest_green_docker.py
  docker run -it --rm --network=pipeline_default ingest_hw1:v001 ingest_lookup_docker.py






Question 1. Understanding Docker images
answer: 25.3

docker run -it --rm --entrypoint bash python:3.13
root@eef02a504d75:/# pip --version
pip 25.3 from /usr/local/lib/python3.13/site-packages/pip (python 3.13)
root@eef02a504d75:/# 

Question 2:   db:5432

Question3: 8,007


SELECT COUNT(*) AS trips_leq_1_mile
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime <  '2025-12-01'
  AND trip_distance <= 1;



Question 4:  11-14


  select max(trip_distance) as max, date(lpep_pickup_datetime) as date
  from green_taxi_data
  where trip_distance <= 100
  group by date(lpep_pickup_datetime)
  order by max(trip_distance) desc

Question 5:   East Harlem North

SELECT
    z."Zone" AS pickup_zone,
    COUNT(*) AS total_trips
FROM green_taxi_data t
JOIN lookup_data z
  ON t."PULocationID" = z."LocationID"
WHERE t.lpep_pickup_datetime >= '2025-11-18'
  AND t.lpep_pickup_datetime <  '2025-11-19'
GROUP BY z."Zone"
ORDER BY total_trips DESC
LIMIT 1;



Question 6: Yorkville West
SELECT
    z_drop."Zone" AS dropoff_zone,
    t.tip_amount AS largest_tip
FROM green_taxi_data t
JOIN lookup_data z_pick
  ON t."PULocationID" = z_pick."LocationID"
JOIN lookup_data z_drop
  ON t."DOLocationID" = z_drop."LocationID"
WHERE t.lpep_pickup_datetime >= '2025-11-01'
  AND t.lpep_pickup_datetime <  '2025-12-01'
  AND z_pick."Zone" = 'East Harlem North'
ORDER BY t.tip_amount DESC
LIMIT 1;


Question 7.  terraform init, terraform apply -auto-approve, terraform destroy


