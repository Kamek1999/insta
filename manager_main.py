from dateandtime import hours_f, minutes_f
from writetocsv import WriteToCSV
from printchart import PrintChart
import os
from time import sleep
from log_sender import logsend
dirname = "\Archives"
pngname = "\Charts"
while True:
    try: #Create dir for files
        actualpath = os.getcwd()
        os.mkdir(actualpath + dirname)
        print("Created")
    except:
        pass

    try: #Create dir for .png
        actualpath = os.getcwd()
        os.mkdir(actualpath + pngname)
    except:
        pass

    twriteh = int(hours_f())
    twritem = int(minutes_f())

    WriteToCSV(twriteh, twritem)
    PrintChart()
    logsend(twriteh, twritem)
    """logarchive(twriteh, twritem)"""
    sleep(45)
