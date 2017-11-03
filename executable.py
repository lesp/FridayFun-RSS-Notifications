#!/usr/bin/python3
import sys
import feedparser
import notify2
import time
feed = feedparser.parse(sys.argv[1])
delay = int(sys.argv[2])
notify2.init("Latest News from "+str(sys.argv[1]))

while True:
    for i in range(3):
        info = feed["entries"][i]["title"]
        URL = feed.entries[i]["link"]
        icon = "/home/les/Documents/blog/RSS-Notif/Pi.png"
        n = notify2.Notification(info,URL,icon=icon)
        n.show()
    time.sleep(delay)

