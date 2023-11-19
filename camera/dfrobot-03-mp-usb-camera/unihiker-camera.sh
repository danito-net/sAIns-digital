#!/usr/bin/env bash

# sAIns-digital by Danny Ismarianto Ruhiyat (info@danito.net)
# https://sains.digital

# CYIENT CyientifIQ Innovation League - Global Hackathon
# https://cyient.hackerearth.com/

# set a delay for 5 seconds
delay=5

# save to external storage (SDCard/MicroSD)
# the default SDCard location in UNIHIKER is /media/mmcblk0p1
sdcard="/media/mmcblk0p1"

# change current operation location to external storage
cd $sdcard

# looping process
while :; do

      year=$(date '+%Y')
      month=$(date '+%m')
      date=$(date '+%d')

      hour=$(date '+%H')
      minute=$(date '+%M')
      second=$(date '+%S')

      # if not exist, create a chronological directory (/media/mmcblk0p1/2023/11/20231119/07)
      if [ ! -d $year ]; then mkdir -p $year; fi
      if [ ! -d $year/$month ]; then mkdir -p $year/$month; fi
      if [ ! -d $year/$month/$year$month$date/$hour ]; then mkdir -p $year/$month/$year$month$date/$hour; fi

      cd $sdcard/$year/$month/$year$month$date/$hour

      # take a photo using fswebcam tools: PNG without compression, 1280 x 960 pixels, 270 degrees rotated
      # with chronological naming rule (example: /media/mmcblk0p1/2023/11/20231119/07/20231119-070432.png)
      /usr/bin/fswebcam --no-banner --resolution 1280x960 --png 0 --rotate 270 $year$month$date-$hour$minute$second.png

      # just wait for a delay
      sleep $delay

done
