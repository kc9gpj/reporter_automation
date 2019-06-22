from bs4 import BeautifulSoup
import requests
import time
from datetime import timezone, datetime
import smtplib

time_delay = 1800

def send_email():
    from_my = 'projectemail1212@yahoo.com' 
    to  = 'kc9gpj12@gmail.com'
    subj= 'Recent Reception'
    date= datetime.now()
    message_text= 'You have received a signal within the last 30 mintues.'

    msg = "From: %s\nTo: %s\nSubject: %s\nDate: %s\n\n%s" % ( from_my, to, subj, date, message_text )

    username = str('projectemail1212@yahoo.com')  
    password = str('1111asdf')  

    try :
        print('connecting')
        server = smtplib.SMTP("smtp.mail.yahoo.com", 587, timeout=10)
        server.starttls()
        server.ehlo
        print('login')
        server.login(username,password)
        print('send email')
        server.sendmail(from_my, to, msg)
        server.quit()    
        print('ok the email has sent')
        time.sleep(time_delay)
        get_data()
    except Exception as e:
        print('can\'t send the Email')
        print(e)
        time.sleep(time_delay)
        get_data()


def get_data():
    print('called')
    try:
        current_time = datetime.now()
        print(current_time)
        r = requests.get('https://retrieve.pskreporter.info/query?receiverCallsign=kc9gpj')
        print(r.status_code)
        soup = BeautifulSoup(r.content, features="html.parser")
        report_time = int(soup.receptionreport["flowstartseconds"])
        report = datetime.fromtimestamp(report_time)
        print(report_time)
        difference = (current_time - report).seconds
        if difference < time_delay:
            print('less than 15 minutes')
            send_email()
        else:
            print('no reports')
            time.sleep(time_delay)
            get_data()
            
    except Exception as e:
        print(e)
        time.sleep(time_delay)
        get_data()

get_data()