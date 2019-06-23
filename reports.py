from bs4 import BeautifulSoup
import requests
import time
from datetime import timezone, datetime
import smtplib

time_delay = 900

def send_email(frequency, count):
    from_my = 'projectemail1212@yahoo.com' 
    to  = 'kc9gpj12@gmail.com'
    subj= 'Recent Reception'
    date= datetime.now()
    message_text= '{} is bitchin right now. Within the past {} minutes. There have been {} signals received.'.format(frequency, time_delay/60, count)

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
        all_reports = []
        current_time = datetime.now()
        r = requests.get('https://retrieve.pskreporter.info/query?receiverCallsign=kc9gpj')
        print(r.status_code)
        soup = BeautifulSoup(r.content, features="html.parser")
        frequency = int(soup.receptionreport["frequency"])
        for link in soup.find_all('receptionreport'):
            report_times = link.get('flowstartseconds')
            report = datetime.fromtimestamp(int(report_times))
            difference = (current_time - report).seconds
            if difference < time_delay:
                all_reports.append(report_times)
        count = len(all_reports)
        print(count)
        if count >= 5:
            print('pass to email')
            send_email(frequency, count)
        else:
            print('no email to send')
            time.sleep(time_delay)
            get_data()
        
            
    except Exception as e:
        print(e)
        time.sleep(time_delay)
        get_data()

get_data()
