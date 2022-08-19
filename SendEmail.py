import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


class SendEmail():
    COMMASPACE = ', '

    def __init__(self, email):
        sender = 'nusran7@gmail.com'
        gmail_password = 'Iloveyoumymom'
        recipients = [email]

        # Create the enclosing (outer) message
        outer = MIMEMultipart()
        outer['Subject'] = 'Estimation have been made.'
        outer['To'] = self.COMMASPACE.join(recipients)
        outer['From'] = sender
        outer.preamble = 'Please find your estimation attached.\n'

        # List of attachments
        attachments = ['File_Locations//out_location//sample.xls']

        # Add the attachments to the message
        for file in attachments:
            try:
                with open(file, 'rb') as fp:
                    msg = MIMEBase('application', "octet-stream")
                    msg.set_payload(fp.read())
                encoders.encode_base64(msg)
                msg.add_header('Content-Disposition', 'attachment', filename=os.path.basename(file))
                outer.attach(msg)
            except:
                # print("Unable to open one of the attachments. Error: ", sys.exc_info()[0])
                raise

        composed = outer.as_string()

        # Send the email
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as s:
                s.ehlo()
                s.starttls()
                s.ehlo()
                s.login(sender, gmail_password)
                s.sendmail(sender, recipients, composed)
                s.close()
            print("Email sent!")
        except:
            # print("Unable to send the email. Error: ", sys.exc_info()[0])
            raise

