# sAIns-digital

(This repository is to complete the requirements for [CYIENT CyientifIQ Innovation League - Global Hackathon 2023](https://cyient.hackerearth.com/))

![desk-sAIns](https://github.com/danito-net/sAIns-digital/blob/main/desk-sAIns/images/desk-sAIns-cyient.png)

## MiniServer sAIns-digital

The MiniServer sAIns-digital will carrying out the main processes and storage

![MiniServer sAIns-digital front side](https://github.com/danito-net/sAIns-digital/blob/main/MiniServer-sAIns-digital/images/MiniServer-sAIns-digital-front.png)

![MiniServer sAIns-digital back side](https://github.com/danito-net/sAIns-digital/blob/main/MiniServer-sAIns-digital/images/MiniServer-sAIns-digital-back.png)

## desk-sAIns

The desk-sAIns devices place on a desk in the laboratory to sense the environtment, condition and taking measurements using sensors, take a photo or video when it necessary and connected to laboratory's instruments.

![desk-sAIns' Hardware](https://github.com/danito-net/sAIns-digital/blob/main/desk-sAIns/images/desk-sains-hardware.png)

desk-sAIns using UNIHIKER, a Linux based Single Board Computer.

![DFRobot UNIHIKER](https://github.com/danito-net/sAIns-digital/blob/main/unihiker/images/dfrobot-unihiker.png)


### UNIHIKER's Technical Specification

* CPU: Quad-Core ARM Cortex-A35, up to 1.2GHz
* RAM: 512MB
* Flash: 16GB
* Wi-Fi: 2.4G
* BT: Bluetooth 4.0
* Screen: 2.8inch, 240×320, Touch Screen
* MCU: GD32VF103
* Sensor: Button, Microphone, Light Sensor, Accelerometer Sensor, Gyroscope Sensor
* Actuator: Led, Buzzer
* Port: USB Type-C, USB-A, Gravity 3pin&4pin port, Edge connector
* Power: 5V 2A for USB Type-C
* Size: 51.6mmx83mmx13mm
* OS: Linux Debian

For more detail information, please click the official page: [DFRobot UNIHIKER](https://www.dfrobot.com/product-2691.html)

Using DFRobot 0.3 Mega Pixwls USB camera for taking a photo or video:

![DFRobot 0.3 Mega Pixels USB Camera](https://github.com/danito-net/sAIns-digital/blob/main/camera/dfrobot-03-mp-usb-camera/images/dfrobot-03mp-usb-camera.png)


### DFRobot 3 Mega Pixels USB Camera Technical Specification

* Sensor type: CMOS
* IR Filter: 650 ± 10nm
* Resolution: 640 x 480 pixels (0.3 Mega Pixels)
* Field of View: 70 degrees
* AGC/AEC/AWB: Auto
* Operating voltage: 5V (USB-A)

For more detail information, please click the official page: [DFRobot 0.3MP USB Camera](https://www.dfrobot.com/product-2089.html)


For power supply, using Waveshare UPS Module 3S:

![Waveshare UPS Module 3S](https://github.com/danito-net/sAIns-digital/blob/main/ups/waveshare-ups-module-3s/images/waveshare-ups-module-3s.png)


Using DFRobot Gravity DHT20 for temperature and humidity sensor:

![DFRobot Gravity DHT20](https://github.com/danito-net/sAIns-digital/blob/main/sensors/images/gravity-dht20-sensor.jpg)

The sAIns-sense devices will taking measurements using sensors

![ESP32 + External + Antenna + Battery](https://github.com/danito-net/sAIns-digital/blob/main/esp32/images/esp32-antenna-battery.png)


In this project, I use a microcontroller based on the ESP32 chip which has an external antenna and battery sockets: [LilyGO / TTGO T7 Mini32 V 1.3](https://www.lilygo.cc/products/t7-v1-3-mini-32-esp32) (Hereafter it will be referred as TTGO-T7)


The photo below shows the details of TTGO-T7:

![TTGO T7 Mini32 V1.3 Detail](https://github.com/danito-net/sAIns-digital/blob/main/esp32/images/TTGO-T7-Mini32-V13.png)

![TTGO T7 Mini32 V1.3 Pinout](https://github.com/danito-net/sAIns-digital/blob/main/esp32/images/ttgo-t7-mini32-v13-pinout.png)

Image source: [LilyGO T7 Mini32 V1.3 pinout](https://www.lilygo.cc/cdn/shop/products/H3d70f69649bb4870af424b7ce6f6e0eaG.jpg)


Using [Airgain N2420 2.4GHz](https://www.arcantenna.com/products/n2420-pk1-g100u-airgain-dual-band-2-4-2-49-ghz-pcb-plug-and-play-antenna-with-100-mm-cable-and-u-fl-connector) external anttena for the TTGO-T7:

![External Antenna 2.4 GHz](https://github.com/danito-net/sAIns-digital/blob/main/esp32/images/external-antenna.png)
