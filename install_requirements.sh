#!/bin/bash

# Installieren benötigter Pakete
sudo apt update
sudo apt install -y build-essential python-dev python-openssl git

# Herunterladen der Adafruit DHT-Bibliothek
git clone https://github.com/adafruit/Adafruit_Python_DHT.git
cd Adafruit_Python_DHT
sudo python setup.py install

# End of Script
