from ywaves import ywave
import unicornhat
from time import sleep

while True:
    unicornhat.rotation(0)
    ywave()
    sleep(1)
    unicornhat.rotation(90)
    ywave()
    sleep(1)
    unicornhat.rotation(180)
    ywave()
    sleep(1)
    unicornhat.rotation(270)
    ywave()
    sleep(1)