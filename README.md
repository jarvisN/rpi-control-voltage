# rpi-control-voltage
# raspberry pi use i2c port SDA / SCL
# compound with ic 4725 DAC 

First Step
# install library 
sudo pip3 install adafruit-circuitpython-mcp4725

Second Step
# you should configure your raspberry pi enable i2c port
    Raspi-Config - Interfacing - I2C via command line 
    1.From the command line or Terminal window start by running the following command :
    sudo raspi-config
    2.This will launch the raspi-config utility. Select “Interfacing Options” :
    3.Highlight the “I2C” option and activate “<Select>”.
    4.Highlight and activate “<Ok>” 
    5.Prompted to reboot highlight and activate “<Yes>”

Third Step
# find a address i2c
    sudo apt-get update
    sudo apt-get install -y python-smbus i2c-tools
    sudo halt
    lsmod | grep i2c_
    i2cdetect -y 1 or i2cdetect -y 0
