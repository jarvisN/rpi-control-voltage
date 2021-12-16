import board
import busio
import time
import adafruit_mcp4725

i2c = busio.I2C(board.SCL, board.SDA)
dac = adafruit_mcp4725.MCP4725(i2c)

dac.value = 65535  # values is 0 (minimum/ground) to 65535 (maximum/Vout).


print("maxiumum power output: ", dac.value ,"volts") # print the value of the DAC.
time.sleep(5) # wait 5 seconds.
dac.value = 0 # set the value of the DAC to 0.
print("minimum power output: ", dac.value ,"volts") # print the value of the DAC.
print("done")