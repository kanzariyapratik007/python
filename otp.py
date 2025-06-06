
import smtplib
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = 'smtp.gmail.com'  
smtp_port = 587  
username = 'kanzariyapratik124@gmail.com' 
password = 'owqlehbqijgdyumo'  


pratik = input("Enter  email: ")
otp=random.randint(1000,9999)

p_email = username
pp_email = pratik
subject = 'LOVE YOU BHAI'
body = f'KA BHAI MOJ MA NE BHULI TO NATHI GYO : {otp}'


msg = MIMEMultipart()
msg['From'] = p_email
msg['To'] = pp_email
msg['Subject'] = subject


msg.attach(MIMEText(body, 'plain'))


try:
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()  
        server.login(username, password) 
        server.send_message(msg)  
    print('Email sent successfully!')
except Exception as e:
    print(f'Failed to send email: {e}')
