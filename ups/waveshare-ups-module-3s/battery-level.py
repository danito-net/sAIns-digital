#!/usr/bin/env python

# sAIns-digital by Danny Ismarianto Ruhiyat (info@danito.net)
# https://sains.digital

# CYIENT CyientifIQ Innovation League - Global Hackathon
# https://cyient.hackerearth.com/

import time
from datetime import datetime
from unihiker import GUI
from pinpong.board import Board
from pinpong.libs.dfrobot_ina219 import INA219

Board().begin()

ina1 = INA219(i2c_addr=0x41)
ina1.begin()
ina1.linear_calibrate(1000)

bus_voltage = 0
shunt_voltage = 0
current = 0
power = 0
load_voltage = 0

gui = GUI()
gui.clear()

battery_level = 0
prev_battery_level = 0

gui.draw_line(x0=0, y0=288, x1=240, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=48, y0=288, x1=48, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=96, y0=288, x1=96, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=144, y0=288, x1=144, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=192, y0=288, x1=192, y1=320, width=1, color=(0, 0, 0))

stat = " "

img_battery_level = gui.draw_image(x = 4, y = 295, w = 40, h = 20, image='/home/sAIns-digital/images/battery-level-0.png')
val_battery_level = gui.draw_text(x=54, y=295, text = str(battery_level) + "%", color="black", font_size=10)

while True:

      bus_voltage = float(ina1.get_bus_voltage_mv() / 1000)
      battery_level = (bus_voltage - 9) / 3.6 * 100
      battery_level = int(round(battery_level, 0))

      # calculation correction for the 'out of range' battery level
      if(battery_level > 100):battery_level = 100
      if(battery_level < 0):battery_level = 0

      if (prev_battery_level != battery_level):

         if (battery_level  <= 100) & (battery_level  > 80):
            img_battery_level.config(image='/home/sAIns-digital/images/battery-level-100.png')
         elif (battery_level  <= 80) & (battery_level  > 60):
            img_battery_level.config(image='/home/sAIns-digital/images/battery-level-80.png')
         elif (battery_level  <= 60) & (battery_level  > 40):
            img_battery_level.config(image='/home/sAIns-digital/images/battery-level-60.png')
         elif (battery_level  <= 40) & (battery_level  > 20):
            img_battery_level.config(image='/home/sAIns-digital/images/battery-level-40.png')
         elif (battery_level  <= 20) & (battery_level  > 0):
            img_battery_level.config(image='/home/sAIns-digital/images/battery-level-20.png')
         else:
            img_battery_level.config(image='/home/sAIns-digital/images/battery-level-0.png')

         val_battery_level.config(text = str(battery_level) + "%")

      prev_battery_level = battery_level

      time.sleep(1)
