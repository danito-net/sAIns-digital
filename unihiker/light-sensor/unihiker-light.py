#!/usr/bin/env python

# sAIns-digital by Danny Ismarianto Ruhiyat (info@danito.net)
# https://sains.digital

# CYIENT CyientifIQ Innovation League - Global Hackathon
# https://cyient.hackerearth.com/

import time
from datetime import datetime
from unihiker import GUI
from pinpong.board import Board
from pinpong.extension.unihiker import *

Board().begin()

gui = GUI()
gui.clear()

## footer status bar

# footer horizontal line (separator)
gui.draw_line(x0=0, y0=288, x1=240, y1=288, width=1, color=(0, 0, 0))

# footer vertical line (separator)
gui.draw_line(x0=48, y0=288, x1=48, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=96, y0=288, x1=96, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=144, y0=288, x1=144, y1=320, width=1, color=(0, 0, 0))
gui.draw_line(x0=192, y0=288, x1=192, y1=320, width=1, color=(0, 0, 0))

light_level = 0

img_light_level = gui.draw_image(x = 145, y = 289, w = 47, h = 32, image = '/home/sAIns-digital/images/lamp-25.png')
val_light_level = gui.draw_text(x=200, y=295, text = str(light_level), color="black", font_size=10)

while True:

      light_level = light.read()

      if 0 <= light_level < 1024:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-25.png')
      elif 1024 <= light_level < 2048:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-50.png')
      elif 2048 <= light_level < 3072:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-75.png')
      else:
         img_light_level.config(image = '/home/sAIns-digital/images/lamp-100.png')

      val_light_level.config(text = str(light_level))

      time.sleep(1)
