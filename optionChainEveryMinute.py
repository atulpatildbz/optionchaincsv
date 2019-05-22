# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:47:55 2019

@author: Atul
"""

import csv
from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime

def mainMethod():
    site = "https://www.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10006&symbol=NIFTY&symbol=NIFTY&instrument=-&date=-&segmentLink=17&symbolCount=2&segmentLink=17"
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    
    request=Request(site,None,hdr)
    html = urlopen(request)
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table", {"id":"octable"})
    rows = table.findAll("tr")
    print("working on: " + str(datetime.now()))
    
    with open(str(datetime.now())+".csv", "wt+", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            csv_row = []
            for cell in row.findAll(["td", "th"]):
                csv_row.append(cell.get_text())
            writer.writerow(csv_row)

REFRESH_INTERVAL = 60
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(mainMethod, 'interval', seconds = REFRESH_INTERVAL)
