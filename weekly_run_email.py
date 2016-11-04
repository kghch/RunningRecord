# Use crontab to run this.

import model
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def get_weekly_record(username):
    records = model.Record().find(username)
    total_distance = 0
    for record in records:
        total_distance += record.length

    prints = "Last week, your running distance is: "
    prints += str(total_distance)
    prints += 'm.\nKeep running!'

    return prints

def emailTo(mailbox, content):
    sender = '15210240044@fudan.edu.cn'

    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(sender)
    message['To'] = Header(mailbox)

    subject = 'Weekly Running Record'
    message['subject'] = Header(subject, 'utf-8')

    m_host = 'mail.fudan.edu.cn:25'
    m_user = sender
    #Todo:
    #Rmember to remove this !
    m_password = ''
    server = smtplib.SMTP(m_host)
    server.ehlo()
    server.starttls()
    server.login(sender, m_password)
    server.sendmail(sender, [mailbox], message.as_string())
    server.close()

if __name__ == '__main__':
    users = model.User().all_users()
    for user in users:
        username = user.username
        mailbox = user.mail
        content = get_weekly_record(username)
        emailTo(mailbox, content)

