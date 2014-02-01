#!/bin/bash

#Extract Activities from device and move to main data folder
sudo python ./Software/Garmin-Forerunner-610-Extractor/garmin.py
cp /home/mike/.config/garmin-extractor/3863488130/activities/* ./FitActivities/

#Parse Activity files and write summary to csv
#sudo bash ./Software/python-fitparse-master/scripts/ActivityFileParser.sh
FILES=~/GarminDataAgent/FitActivities/*
cd Software/python-fitparse-master/scripts/
echo "start_time,total_distance,avg_speed,total_elapsed_time" > ./garmin_data.csv
for f in $FILES
do
  #echo "Processing File = $f"
  sudo python sample_program.py $f
done
#move back to main dir yeah I know...its a quick fix...
cd ..
cd ..
cd ..
mv ./Software/python-fitparse-master/scripts/garmin_data.csv ./

#remove the log file lolz.............
rm *.log

#run R script to produce viz!
R CMD BATCH ./Software/r_viz/garminDataViz.R
