#!/usr/bin/env python

# sAIns-digital by Danny Ismarianto Ruhiyat (info@danito.net)
# https://sains.digital

# CYIENT CyientifIQ Innovation League - Global Hackathon
# https://cyient.hackerearth.com/

import time

from datetime import datetime
from unihiker import GUI

from pinpong.board import Board
from pinpong.board import Pin

from pinpong.libs.dfrobot_ina219 import INA219
from pinpong.libs.dfrobot_dht20 import DHT20

from pinpong.extension.unihiker import *

Board().begin()

light_level = 0

temp = 0
humi = 0

bus_voltage = 0
battery_level = 0

VAC = 220
CSENSOR = 5
VREF = 5
amp = 0

now = datetime.now()
day_now  = now.strftime("%A")
date_now  = now.strftime("%d %B %Y")
hour_now  = now.strftime("%H")
minute_now  = now.strftime("%M")
second_now  = now.strftime("%S")

pin22 = Pin(Pin.P22, Pin.ANALOG)

dht = DHT20()

ina = INA219(i2c_addr=0x41)

ina.begin()
ina.linear_calibrate(1000)

gui = GUI()

img_header = gui.draw_image(x = 53, y = 10, w = 134, h = 72, image = '/home/sAIns-digital/images/sains-digital-72.png')

# horizontal line (date-time top)
gui.draw_line(x0=0, y0=90, x1=240, y1=90, width=1, color=(0, 0, 0))

val_date = gui.draw_text(x = 30, y = 93, text = day_now + ", " + date_now, color="black", font_size=10)

val_separator1 = gui.draw_text(x = 91, y = 106, text = ":", color=(0, 183, 235), font_size=20)
val_separator2 = gui.draw_text(x = 140, y = 106, text = ":", color=(0, 183, 235), font_size=20)

val_hour = gui.draw_digit(x = 51, y = 118, text = hour_now, color="black", font_size=20)
val_minute = gui.draw_digit(x = 103, y = 118, text = minute_now, color="black", font_size=20)
val_second = gui.draw_digit(x = 152, y = 118, text = second_now, color="black", font_size=20)

# horizontal line (date-time bottom)
gui.draw_line(x0=0, y0=150, x1=240, y1=150, width=1, color=(0, 0, 0))

gui.draw_line(x0=96, y0=176, x1=240, y1=176, width=1, color=(0, 0, 0))

gui.draw_line(x0=96, y0=150, x1=96, y1=320, width=1, color=(0, 0, 0))

# footer horizontal line
gui.draw_line(x0=0, y0=288, x1=240, y1=288, width=1, color=(0, 0, 0))

# footer vertical line (separator)
gui.draw_line(x0=144, y0=288, x1=144, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=192, y0=288, x1=192, y1=320, width=1, color=(0, 0, 0))

img_camera = gui.draw_image(x = 1, y = 158, w = 92, image = '/home/sAIns-digital/images/camera.png')

val_temp = gui.draw_text(x = 110, y = 153, text = str(temp) + " \N{DEGREE SIGN}C", color="black", font_size=10)
val_humi = gui.draw_text(x = 175, y = 153, text = str(humi) + " %", color="black", font_size=10)

img_amp = gui.draw_image(x = 141, y = 185, w = 56, h = 80, image = '/home/sAIns-digital/images/amp-off.png')
val_amp = gui.draw_text(x = 143, y = 266, text = str(amp) + " A", color="black", font_size=10)

img_battery_level = gui.draw_image(x = 4, y = 295, w = 40, h = 20, image = '/home/sAIns-digital/images/battery-level-0.png')
val_battery_level = gui.draw_text(x=54, y=295, text = str(battery_level) + "%", color="black", font_size=10)

img_light_level = gui.draw_image(x = 145, y = 289, w = 47, h = 32, image = '/home/sAIns-digital/images/lamp-000.png')
val_light_level = gui.draw_text(x=200, y=295, text = str(light_level), color="black", font_size=10)

while True:

      now = datetime.now()
      day_now  = now.strftime("%A")
      date_now  = now.strftime("%d %B %Y")
      hour_now  = now.strftime("%H")
      minute_now  = now.strftime("%M")
      second_now  = now.strftime("%S")

      val_date.config(text = day_now + ", " + date_now)

      val_hour.config(text = hour_now)
      val_minute.config(text = minute_now)
      val_second.config(text = second_now)

      # buzzer.pitch(200, 1)

      bus_voltage = float(ina.get_bus_voltage_mv() / 1000)
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

      light_level = light.read()

      if 0 <= light_level < 50:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-000.png')
      elif 50 <= light_level < 100:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-017.png')
      elif 100 <= light_level < 250:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-034.png')
      elif 250 <= light_level < 1000:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-050.png')
      elif 1000 <= light_level < 2000:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-067.png')
      else:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-100.png')

      val_light_level.config(text = str(light_level))

      img_camera.config(image = '/home/sAIns-digital/images/camera.png')

      temp = dht.temp_c()
      humi = dht.humidity()

      val_temp.config(text = str(temp) + " \N{DEGREE SIGN}C")
      val_humi.config(text = str(humi) + " %")

      peakVoltage = 0
      virtualVoltage = 0
      amp = 0

      for _ in range(5):
          peakVoltage += pin22.read_analog()
          time.sleep(0.5)

      peakVoltage = peakVoltage / 5

      # The root-mean-square voltage is 0.707
      # 1.41421356237 = sqrt(2)

      virtualVoltage = peakVoltage * 0.707
      virtualVoltage = (virtualVoltage / 1024 * VREF) / 2
      amp = virtualVoltage * CSENSOR

      amp = (amp / 10) + 0.005

      amp = round(amp, 3)

      if amp >= 0.017:
         val_amp.config(text = str(amp) + " A")
         img_amp.config(image = '/home/sAIns-digital/images/amp-on.png')
      else:
         val_amp.config(text = str(amp) + " A")
         img_amp.config(image = '/home/sAIns-digital/images/amp-off.png')
