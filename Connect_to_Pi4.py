import pyautogui as auto
import subprocess as sub
import time

sub.Popen(['C:\\Users\\Public\\Putty.exe'])
time.sleep(2)
auto.write('192.168.0.51')
time.sleep(0.5)
auto.press('enter')
time.sleep(0.7)
auto.write('pi')
auto.press('enter')
auto.write('1D2NT3L4G5')
auto.press('enter')
time.sleep(0.5)
auto.write('cd /home/pi/Desktop/RaspCode/RaspCode')
auto.press('enter')
auto.write('ls')
auto.press('enter')
auto.write('python Py.py')
auto.press('enter')
