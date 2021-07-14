from result_notifier import Scrape
import smtplib
import ssl
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

receivers = ["dhruvjadhav225@gmail.com", "cskharche2005@gmail.com", "aravidind@gmail.com"]

# Email sender function
def FireEmail(sender, receiver, link, time):
    global server
    try:
        # Creating body of email
        message = MIMEMultipart()
        message["From"] = sender
        message["To"] = receiver
        message["Subject"] = f"Hey! Your 10th Board Results Are OUT!"

        body = f"""\
        <html>
            <body>
            <p>Hi There!
                <br/>
                <hr/>
            </p>
            <p>
                The CBSE 10th Board Results are out!
                <br/>
                <br/>
                Go to <a href="{link}">{link}</a> to check the results.
                <br/>
                <br/>
                Last checked at {time}
            </p>
            <p>
                <strong>Regards,<br/>The_Devs</strong>
            </p>
            </body>
        </html>
        """

        message.attach(MIMEText(body, "html"))

        text = message.as_string()

        # Initializing smtp server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        context = ssl.create_default_context()
        server.ehlo()
        server.starttls(context=context)
        server.ehlo()

        server.login(user='wow.acdc2005@gmail.com', password=os.getenv('WOW_KEY'))
        server.sendmail(sender, receiver, text)
        print(f"Email Sent to: {receiver}")
    except Exception as e:
        print(e)
    finally:
        server.close()

# -----------------------------------------------------------------------------------------
if Scrape()[0] == 'True':
    for k in receivers:
        FireEmail(sender="wow.acdc2005@gmail.com", receiver=k, link=Scrape()[1], time=Scrape()[2])
else:
    print("Gotta wait for some more time")
