import email, smtplib, ssl
import csv
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



def send_email_attachment(attachments=list()):
    """
    This Function to send email attachment to required team or person
    :param attachments: List of the files
    :return: None
    """
    toaddr = [os.environ["USER"] + "@xyz.com"]
    logging.info('Sending mail to Team')
    msg = MIMEMultipart()
    msg['From'] = "abc@xyz.com"
    msg['To'] = ",".join(toaddr)
    msg['Subject'] = "Test is Completed !!!"
    ''' Create the email body message '''
    email_body = "Hi Team,\n\nPlease find the attached report (files)\n\n" \
                 "Please do not reply to this mail, it is an auto generated...\n\nThanks,\nTeam"
    msg.attach(MIMEText(email_body, 'plain'))

    ''' Create the attachments for each file '''
    for csv_filename in attachments:
        ''' Attach the file '''
        with open(csv_filename, "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= {}".format(os.path.basename(csv_filename)))
        msg.attach(part)
    text = msg.as_string()

    ''' Send the mail '''
    try:
        logging.info("Send the message via local SMTP server")
        mailer = smtplib.SMTP('localhost')
        mailer.send_message(msg)
        mailer.sendmail(msg['From'], toaddr, text)
        mailer.quit()
        logging.info("Please refer /var/spool/mail/$USER file for more details")
    except smtplib.SMTPConnectError as smtp_con:
        logging.error("Issue observed during establishment of a connection with the server - %s" % str(smtp_con))
        logging.info("Please refer /var/spool/mail/$USER file for more details")

# To call the function
send_email_attachment([log_filename, output_csv_filename])
