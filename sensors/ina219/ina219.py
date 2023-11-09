#!/usr/bin/env python

# sAIns-digital by Danny Ismarianto Ruhiyat (info@danito.net)
# https://sains.digital

# CYIENT CyientifIQ Innovation League - Global Hackathon
# https://cyient.hackerearth.com/

import time
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

while True:

      bus_voltage = float(ina1.get_bus_voltage_mv() / 1000)
      shunt_voltage = float(ina1.get_shunt_voltage_mv() / 1000)
      current = float(ina1.get_current_ma() / 1000)
      power = float(ina1.get_power_mw() / 1000)
      load_voltage = bus_voltage + shunt_voltage

      battery_level = (bus_voltage - 9) / 3.6 * 100
      if(battery_level > 100):battery_level = 100
      if(battery_level < 0):battery_level = 0

      print(" ")
      print("Bus Voltage =", "{:.2f}V".format(bus_voltage))
      print("Shunt Voltage =", "{:.2f}V".format(shunt_voltage))
      print("Current =", "{:.2f}A".format(current))
      print("Power =", "{:.2f}W".format(power))
      print("Load Voltage =", "{:.2f}V".format(load_voltage))
      print("Battery Level =", "{:.2f}%".format(battery_level))

      time.sleep(1)
