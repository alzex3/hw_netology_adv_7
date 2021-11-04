import email
from smtplib import SMTP
from imaplib import IMAP4_SSL
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart


class EmailApp:
    def __init__(self, login, password, smtp_serv, imap_serv):
        self.login = login
        self.password = password
        self.smtp_serv = smtp_serv
        self.imap_serv = imap_serv

    def send_mail(self, smtp_serv, recipients, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        smtp = SMTP(smtp_serv, 587)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(self.login, self.password)
        smtp.sendmail(self.login, smtp, msg.as_string())
        smtp.quit()

    def recieve_mail(self, header, mailbox='INBOX'):
        mail = IMAP4_SSL(self.imap_serv)
        mail.login(self.login, self.password)
        mail.list()
        mail.select(mailbox)
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('SEARCH', criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('FETCH', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()
        return email_message


if __name__ == '__main__':
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_IMAP = "imap.gmail.com"

    usr_login = 'login@gmail.com'
    usr_password = 'qwerty'

    mail_subject = 'Subject'
    mail_recipients = ['vasya@email.com', 'petya@email.com']
    mail_message = 'Message'
    mail_header = None

    main = EmailApp(usr_login, usr_password, GMAIL_SMTP, GMAIL_IMAP)
    main.recieve_mail(mail_header)
