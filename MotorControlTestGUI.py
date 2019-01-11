import PCA9685
from PCA9685 import pwm
import time

from tkinter import *

class MotorUI:

  def __init__(self, window):
    
    self.pwm_value = IntVar()
    self.pwm_value.set(2048)

    slider = Scale(window, from_=0, to=4096,
    resolution=1, orient=HORIZONTAL, length=500, command=self.change_pwm, variable=self.pwm_value)
    slider.set(2048)
    slider.pack()

    zero = Button(window, text="Stop", command=self.zero).pack()

  def set_pwm(self, channel, value):
    print('Setting PWM to', str(channel) + ',' , value)
    x=min(4095,value)
    x=max(0,x)
    """Sets a single PWM channel."""
    LED0_ON_L          = 0x06
    LED0_ON_H          = 0x07
    LED0_OFF_L         = 0x08
    LED0_OFF_H         = 0x09
    pwm.write(bytes([(LED0_ON_L+4*channel), 0]))
    pwm.write(bytes([(LED0_ON_H+4*channel), 0]))
    pwm.write(bytes([(LED0_OFF_L+4*channel), (x & 0xFF)]))
    pwm.write(bytes([(LED0_OFF_H+4*channel), (x >> 8)]))
    print('set pwm value')

  def change_pwm(self, nada):
    self.set_pwm(0, self.pwm_value.get())

  def zero(self):

    self.pwm_value.set(2048)
    print('zero')
    self.set_pwm(0, 2048)
    '''Reset POWM'''
    pwm.write(bytes([0xFA, 0]))     # zero all pin
    pwm.write(bytes([0xFB, 0]))     # zero all pin
    pwm.write(bytes([0xFC, 0]))     # zero all pin
    pwm.write(bytes([0xFD, 0]))     # zero all pin
    pwm.write(bytes([0x01, 0x04]))  # The 16 LEDn outputs are configured with a totem pole         structure.
    pwm.write(bytes([0x00, 0x01]))  #PCA9685 responds to LED All Call I2C-bus address
    time.sleep(0.01)  # wait for oscillator

if __name__ == '__main__':
  root = Tk()
  root.title('Motor Control Testing')
  app = MotorUI(root)
root.mainloop()

