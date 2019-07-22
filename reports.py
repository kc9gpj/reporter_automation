from bs4 import BeautifulSoup
import requests
import time
from datetime import timezone, datetime
import smtplib

time_delay = 900

def send_email(band, count, dx):
    from_my = 'projectemail1212@yahoo.com'
    to  = 'kc9gpj12@gmail.com'
    subj= 'Recent Reception'
    date= datetime.now()
    message_text= 'On {} meters, Within the past {} minutes. There have been {} signals received. DX: {}'.format(band, int(time_delay/60), count, dx)

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
        dx = []
        current_time = datetime.now()
        r = requests.get('https://retrieve.pskreporter.info/query?receiverCallsign=kc9gpj')
        soup = BeautifulSoup(r.content, features="html.parser")
        frequency = int(soup.receptionreport["frequency"])
        if 144000000 <= frequency <= 144300000:
            band = 2
        if 50313000 <= frequency <= 50316000:
            band = 6
        elif 18100000 <= frequency <= 18100300:
            band = 17
        elif 14074000 <= frequency <= 14077000:
            band = 20
        elif 10136000 <= frequency <= 10139000:
            band = 30
        elif 7074000 <= frequency <= 7077000:
            band = 40
        else:
            band = 0
        for link in soup.find_all('receptionreport'):
            print(link)
            report_times = link.get('flowstartseconds')
            dxcc = link.get('senderdxcc')
            print(dxcc)
            report = datetime.fromtimestamp(int(report_times))
            difference = (current_time - report).seconds
            if difference < time_delay:
                all_reports.append(report_times)
            if dxcc != 'United States':
                dx.append(dxcc)
        count = len(all_reports)
        print(count)
        if count >= 1 and band == 2:
            print('pass to email')
            send_email(band, count, dx)
        elif count >= 5 and band == 6:
            print('pass to email')
            send_email(band, count, dx)
        elif dx and band == 17:
            print('pass to email')
            send_email(band, count, dx)
        elif dx and band == 17:
            print('pass to email')
            send_email(band, count, dx)
        elif dx and band == 20:
            print('pass to email')
            send_email(band, count, dx)
        elif dx and band == 30:
            print('pass to email')
            send_email(band, count, dx)
        elif dx and band == 40:
            print('pass to email')
            send_email(band, count, dx)
        else:
            print('no email to send')
            time.sleep(time_delay)
            get_data()

    except Exception as e:
        print(e)
        time.sleep(time_delay)
        get_data()

get_data()
