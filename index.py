import rainbowhat as rh
import time
import colorsys

@rh.touch.B.press()
def touch_b(channel):
    rh.display.clear()
    rh.display.print_str('Brian Rocks')
    rh.display.show()
    print('Button B pressed')

while True:
    t = rh.weather.temperature()
    p = rh.weather.pressure()
    rh.display.clear()
    rh.display.print_float(t)
    rh.display.show()
    print(t, p)
    time.sleep(1.0)