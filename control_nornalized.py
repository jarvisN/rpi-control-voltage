import board
import busio
import time
import adafruit_mcp4725


i2c = busio.I2C(board.SCL, board.SDA)

dac = adafruit_mcp4725.MCP4725(i2c)

dac.normalized_value = 1.0  # Use the normalized_value property to set the
# output with a floating point value in the range
# 0 to 1.0 where 0 is minimum/ground and 1.0 is
# maximum/Vout.

print("maxiumum power output: ", dac.normalized_value ,"volts") # print the value of the DAC.
time.sleep(5) # wait 5 seconds.
dac.normalized_value = 0 # set the value of the DAC to 0.
print("minimum power output: ", dac.normalized_valuee ,"volts") # print the value of the DAC.
print("done")