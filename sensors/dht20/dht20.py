#!/usr/bin/env python

# sAIns-digital by Danny Ismarianto Ruhiyat (info@danito.net)
# https://sains.digital

# CYIENT CyientifIQ Innovation League - Global Hackathon
# https://cyient.hackerearth.com/

import time
from pinpong.board import Board
from pinpong.libs.dfrobot_dht20 import DHT20

Board().begin()
p_dht20 = DHT20()

temperature = 0
humidity = 0

while True:

      temperature = p_dht20.temp_c()
      humidity = p_dht20.humidity()

      print(" ")
      print("Temperature =", "{:.2f}\N{DEGREE SIGN}C".format(temperature))
      print("Humidity =", "{:.2f}%".format(humidity))

      time.sleep(1)
