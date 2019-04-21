import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import datetime
import logging
import shutil
import os
logging.basicConfig(filename='logs.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')
content = 'ecample email stuff here'
my_email = "pythoninsta1@gmail.com"
to_email = "kamek1999@gmail.com"
password = "dvdromkamek1"
mail = smtplib.SMTP('smtp.gmail.com', 587)
name = "logs" + datetime.datetime.now().strftime("%B %d %H %M")
suffix = ".log"
dirname = "\Logs"
destname = "Logs\\"
def logsend(twriteh, twritem):
    try:
        if twriteh == 6 or 10 or 18 or 22:
            if twritem == 3:
                msg = MIMEMultipart()
                msg['From'] = my_email
                msg['To'] = to_email
                msg['Subject'] = name
                body = "chart - " + name
                msg.attach(MIMEText(body, 'plain'))
                filename = "logs" + suffix
                attachment = open(filename, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename= " + filename)
                msg.attach(part)
                text = msg.as_string()
                mail.ehlo()
                mail.starttls()
                mail.login(my_email, password)
                mail.sendmail(my_email, to_email, text)
                mail.close()
                logging.info("Logs sent")
                print("Logs sent")
    except Exception as e:
        print("Logs didn't send")
        logging.error(r"Couldn't send logs ERROR " + str(e))
"""def logarchive(twriteh, twritem):
    if twriteh == 15 and twritem == 46:
        try: #Create dir for logs
            actualpath = os.getcwd()
            os.mkdir(actualpath + dirname)
            logging.info("Created logs folder")
        except Exception as e:
            logging.error("Couldn't create folder for logs " + str(e))
        try:
            shutil.copyfile("logs" + suffix, dirname + "logs" + suffix)
            os.rename("logs" + suffix, destname + "logs" + datetime.datetime.now().strftime("%B%d") + suffix)
            os.remove("logs" + suffix)
            logging.info("Logs copied to directory")
            print("Logs copied")
        except Exception as e:
            logging.error("Couldn't copy file " + str(e))
"""