import smtplib
#allow us to send text
from email.mime.text import MIMEText

def send_mail(time,vehicles, n_people, location, severity , latitude,longitude,officer ):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'd0799f4a92f84f'
    password = '66b1b88c997f2a'

    message = f"<h3>New Crash Reporting</h3><ul><li>time: {time}</li><li>vehicles: {vehicles}</li><li>people: {n_people}</li><li>location: {location}</li><li>severity: {severity}</li><li>latitude: {latitude}</li><li>longitude: {longitude}</li></ul>"

    sender_email ='email@example.com'

    receiver_email = 'guyodubjarso@gmail.com' #subsitute for managing doctors using Triggers

    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Crash report'

    msg['from'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email,  msg.as_string())

