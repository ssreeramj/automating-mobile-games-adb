import time
import numpy as np
from mss import mss
from ppadb.client import Client

# Default is "127.0.0.1" and 5037
client = Client(host="127.0.0.1", port=5037)
device = client.devices()[0]

# device.shell("input tap 680 1150")

c11 = { 'left' : 1062, 'top' : 175, 'width' : 1, 'height' : 1 }
c12 = { 'left' : 1149, 'top' : 175, 'width' : 1, 'height' : 1 }
c13 = { 'left' : 1237, 'top' : 175, 'width' : 1, 'height' : 1 }
c14 = { 'left' : 1321, 'top' : 175, 'width' : 1, 'height' : 1 }

c21 = { 'left' : 1062, 'top' : 322, 'width' : 1, 'height' : 1 }
c22 = { 'left' : 1149, 'top' : 322, 'width' : 1, 'height' : 1 }
c23 = { 'left' : 1237, 'top' : 322, 'width' : 1, 'height' : 1 }
c24 = { 'left' : 1321, 'top' : 322, 'width' : 1, 'height' : 1 }

c31 = { 'left' : 1062, 'top' : 466, 'width' : 1, 'height' : 1 }
c32 = { 'left' : 1149, 'top' : 466, 'width' : 1, 'height' : 1 }
c33 = { 'left' : 1237, 'top' : 466, 'width' : 1, 'height' : 1 }
c34 = { 'left' : 1321, 'top' : 466, 'width' : 1, 'height' : 1 }

sct = mss()

def get_black(a, b, c, d):
    if sum(a[0][0]) < 5:
        return 1
    elif sum(b[0][0]) < 5:
        return 2
    elif sum(c[0][0]) < 5:
        return 3
    else:
        return 4 

while True:
    time.sleep(.2)

    c11_pixel = np.array(sct.grab(c11))
    c12_pixel = np.array(sct.grab(c12))
    c13_pixel = np.array(sct.grab(c13))
    c14_pixel = np.array(sct.grab(c14))

    c21_pixel = np.array(sct.grab(c21))
    c22_pixel = np.array(sct.grab(c22))
    c23_pixel = np.array(sct.grab(c23))
    c24_pixel = np.array(sct.grab(c24))

    c31_pixel = np.array(sct.grab(c31))
    c32_pixel = np.array(sct.grab(c32))
    c33_pixel = np.array(sct.grab(c33))
    c34_pixel = np.array(sct.grab(c34))
    

    # print(c1_pixel)
    # print(c2_pixel)
    # print(c3_pixel)
    # print(c4_pixel)

    first_row = get_black(c11_pixel, c12_pixel, c13_pixel, c14_pixel)
    second_row = get_black(c21_pixel, c22_pixel, c23_pixel, c24_pixel)
    third_row = get_black()

    if sum(c1_pixel[0][0]) < 5:
        device.shell("input tap 130 1170")
        # print(1)
    elif sum(c2_pixel[0][0]) < 5:
        device.shell("input tap 406 1170")
        # print(2)
    elif sum(c3_pixel[0][0]) < 5:
        device.shell("input tap 680 1170")
        # print(3)
    elif sum(c4_pixel[0][0]) < 5:
        device.shell("input tap 966 1170")
        # print(4)
    else:
        continue