from micropython import const
from machine import Pin,I2C
import time


CLEAR_DISPLAY=const(0x01)
CLEAR_DISPLAY=const(0x02)
CLEAR_DISPLAY=const(0x04)
CLEAR_DISPLAY=const(0x0C)
CLEAR_DISPLAY=const(0x20)
CLEAR_DISPLAY=const(0x10)
CLEAR_DISPLAY=const(0x50)
CLEAR_DISPLAY=const(0x60)
CLEAR_DISPLAY=const(0x70)
CLEAR_DISPLAY=const(0x80)

class ST032i:
    def __inti__(self,i2c,addr=0x3e):
        pass
    def write_cmd(self):
        pass
    def write_data(self):
        pass
    def init_display(self):
        pass
    def clear(self):
        pass
    def print_str(self):
        pass
