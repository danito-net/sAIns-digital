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

gui = GUI()
gui.clear()

## footer status bar

# footer horizontal line
gui.draw_line(x0=0, y0=288, x1=240, y1=288, width=1, color=(0, 0, 0))

# footer vertical line (separator)
gui.draw_line(x0=48, y0=288, x1=48, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=96, y0=288, x1=96, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=144, y0=288, x1=144, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=192, y0=288, x1=192, y1=320, width=1, color=(0, 0, 0))

bus_voltage = 0
battery_level = 0

img_battery_level = gui.draw_image(x = 4, y = 295, w = 40, h = 20, image = '/home/sAIns-digital/images/battery-level-0.png')
val_battery_level = gui.draw_text(x=54, y=295, text = str(battery_level) + "%", color="black", font_size=10)

while True:

      bus_voltage = float(ina1.get_bus_voltage_mv() / 1000)
      battery_level = (bus_voltage - 9) / 3.6 * 100
      battery_level = int(round(battery_level, 0))

      # calculation correction for the 'out of range' battery level
      if(battery_level > 100):battery_level = 100
      if(battery_level < 0):battery_level = 0

      if 0 <= battery_level < 21:
         img_battery_level.config(image = '/home/sAIns-digital/images/battery-level-0.png')
      elif 21 <= battery_level < 41:
         img_battery_level.config(image = '/home/sAIns-digital/images/battery-level-20.png')
      elif 41 <= battery_level < 61:
         img_battery_level.config(image = '/home/sAIns-digital/images/battery-level-40.png')
      elif 61 <= battery_level < 81:
         img_battery_level.config(image = '/home/sAIns-digital/images/battery-level-60.png')
      elif 81 <= battery_level < 96:
         img_battery_level.config(image = '/home/sAIns-digital/images/battery-level-80.png')
      else:
         img_battery_level.config(image = '/home/sAIns-digital/images/battery-level-100.png')

      val_battery_level.config(text = str(battery_level) + "%")

      time.sleep(1)
