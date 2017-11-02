#!/usr/bin/python3
import sys
import feedparser
import notify2
import time
feed = feedparser.parse(sys.argv[1])
notify2.init("Latest News from "+str(sys.argv[1]))

for i in range(3):
    info = feed["entries"][i]["title"]
    URL = feed.entries[i]["link"]
    icon = "/home/les/Documents/LXF/232/RSS-Notif/Pi.png"
    n = notify2.Notification(info,URL,icon=icon)
    n.show()
    

