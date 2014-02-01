#!/bin/bash
echo "start_time,total_distance,avg_speed,total_elapsed_time" > ./garmin_data.csv
FILES=/home/mike/Desktop/GarminDataAgent/FitActivities/*
for f in $FILES
do
  #echo "Processing File = $f"
  sudo python sample_program.py $f
done
