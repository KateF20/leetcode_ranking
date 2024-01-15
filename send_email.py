import smtplib
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])


def send_email(ranking):
    sender = 'kaitherinayrd@gmail.com'
    receivers = ['kaitherinayrd@gmail.com']
    password = 'tgntpmbqirssykzl'

    subject = 'LeetCode Change'
    body = f'Your LeetCode ranking changed! You\'re now are at {ranking}th place!'

    logging.info(f'ready to send an email to {receivers} with this text: {body}')

    message = MIMEMultipart()
    message['From'] = sender
    message['To'] = ', '.join(receivers)
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            text = message.as_string()
            server.sendmail(sender, receivers, text)
            logging.info('Email sent successfully')

    except Exception as e:
        logging.info(f"Error: {e}")
