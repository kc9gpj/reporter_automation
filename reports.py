from bs4 import BeautifulSoup
import requests

def get_data():
    print('called')
    try:
        r = requests.get('https://retrieve.pskreporter.info/query?receiverCallsign=kc9gpj')
        soup = BeautifulSoup(r.content)
        for a in soup.find_all('receptionreports'):
            # flowstartseconds
            print(a)
                    
    except Exception as e:
        print(e)

get_data()

# def send_expiring_domain_email(task):
#     domain_list = []
#     cert_list = []
#     with logger.task_logger(task=task):
#         two_weeks_from_now = datetime.today() + timedelta(days=14)
#         thirty_days_from_now = datetime.today() + timedelta(days=30)
#         domain = WebsiteDomain.objects.filter()
#         for d in domain.all():
#             if d.domain_expire_date is not None:
#                 if d.domain_expire_date.date() < thirty_days_from_now.date():
#                     domain_list.append("https://bowser.legalfit.io/websites/{}/info".format(d.website.key))
#                     domain_list.append(d.domain)
#                     domain_list.append(d.domain_expire_date.strftime("%B %d, %Y"))

#         for d in domain.all():
#             if d.ssl_expire_date is not None:
#                 if d.ssl_expire_date.date() < two_weeks_from_now.date():
#                     cert_list.append("https://bowser.legalfit.io/websites/{}/info".format(d.website.key))
#                     cert_list.append(d.domain)
#                     cert_list.append(d.ssl_expire_date.strftime("%B %d, %Y"))

#     try:
#         send_mail(
#             'Doman/SSL Expirations',
#             'Here is the message.',
#             'no-reply@big6media.com',
#             [settings.EXPIRE_NOTIFICATION_EMAILS],
#             html_message='<div style="font-size: 20px;">Domains Expiring Within 30 Days: </div>'
#             + '<div>'
#             + str("<br> ".join(domain_list)) + '<div style="font-size: 20px;">Certificates Expiring Within 14 Days: </div>'
#             + str("<br> ".join(cert_list)),
#         )