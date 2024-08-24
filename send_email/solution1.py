import smtplib

SENDER_EMAIL = '<SECRET>'
SENDER_PASSWORD = '<SECRET>'


def send_email(receiver_email, subject, body):
    message = f'Subject: {subject}\n\n{body}'
    with smtplib.SMTP('<EMAIL_CLIENT>', '<port_num: int>') as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)