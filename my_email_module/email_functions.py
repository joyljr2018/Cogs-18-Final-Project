import smtplib
import imaplib
import time
from email.mime.text import MIMEText
import string

    
def email_send(user,password,message,from_address,to_address):
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.starttls()
    smtp.ehlo()
    time.sleep(2)
    EMAIL_TEXT = message
    FROM_ADDRESS = str(from_address)
    TO_ADDRESS = str(to_address)
    
    
    try:
        smtp.login(user,password)
        print("SENDING EMAIL")
        try:
            msg = MIMEText(EMAIL_TEXT)
            msg['From'] =  FROM_ADDRESS
            msg['To'] = TO_ADDRESS
            msg['Subject'] = message
            smtp.send_message(msg)
            print('EMAIL SENT!')
            time.sleep(1)
            return True
            
        except smtplib.SMTPRecipientsRefused:
            print("SMTPRecipientsRefused")
            return False
   
    except smtplib.SMTPAuthenticationError:
        print("SMTPAuthenticationError")
       
        return False
    
    
    
    
    
    
    
    
def email_receive(user,password):
    import email 
    imap_ssl_host = 'imap.gmail.com'  # imap.mail.yahoo.com
    imap_ssl_port = 993
    user = str(user)
    password = str(password)
    server = imaplib.IMAP4_SSL(imap_ssl_host, imap_ssl_port)
    server.login(user, password)
    server.select('INBOX')
    server.list()
    result,data = server.uid('search',None,"ALL")
    inbox_item_list = data[0].split()
    most_recent = inbox_item_list[-1]
    result2,email_data = server.uid('fetch',most_recent,'(RFC822)')
    raw_email = email_data[0][1].decode("utf-8")
    msg = email.message_from_string(raw_email)
    From = msg['From']
    Subject = msg['Subject']
    content = msg.get_payload()
    email_receive = [Subject,From,content]
    
    return email_receive



