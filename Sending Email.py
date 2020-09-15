import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import traceback

def send_gmail(login, receiver, subject, content, sys = 'outlook'):
    try:
        if sys == 'outlook':
            smtp = 'smtp.live.com'
        elif sys == 'gmail':
            smtp = 'smtp.gmail.com'
        message = MIMEMultipart()
        message['From'] = login['email']
        message['To'] = receiver
        message['Subject'] = subject
        message.attach(MIMEText(content, 'plain'))
        session = smtplib.SMTP(smtp, 587)
        session.starttls()
        session.login(login['email'], login['pw'])
        text = message.as_string()
        session.sendmail(login['email'], receiver, text)
        session.quit()

        print('Mail Sent')
    except:
        print('Something is wrong')
        print(traceback.format_exc())
if __name__ == "__main__":
    # First open this link and enable: Allow less secure apps: ON
    # https://www.google.com/settings/security/lesssecureapps

    mylogin = {'email': 'myemail@gmail.com', 'pw': 'mypassword'}
    send_gmail(login = mylogin, receiver = 'gwanghaogood@gmail.com', subject='testing', content='testing')