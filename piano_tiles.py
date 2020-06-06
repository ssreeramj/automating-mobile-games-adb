import time
import numpy as np
from mss import mss
from ppadb.client import Client

# Default is "127.0.0.1" and 5037
client = Client(host="127.0.0.1", port=5037)
device = client.devices()[0]

lap_row = [195, 346, 498]
lap_col = [1065, 1152, 1234, 1325]

mob_row = [247, 719, 1146]
mob_col = [127, 400, 680, 950]

blacks = [1]
sct = mss()

while True:
    time.sleep(.13)

    blacks = []
    for row in lap_row:
        for ind, col in enumerate(lap_col):
            pixel = np.array(sct.grab(
                { "left": col, "top": row, "width": 1, "height": 1 }
            ))

            if sum(pixel[0][0]) < 5:
                blacks.append(ind)
                break

    if blacks:
        device.shell(f"input tap {mob_col[blacks[2]]} {mob_row[2]}")
        device.shell(f"input tap {mob_col[blacks[1]]} {mob_row[2]}")
        device.shell(f"input tap {mob_col[blacks[0]]} {mob_row[2]}")
    else:
        break