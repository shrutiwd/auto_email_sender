# sending emails from csv file

# importing necessary libraries
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Email:
    def __init__(self, file_name,send, subject):
        '''Intializing instance variables'''
        self.file_name = file_name
        self.send = send
        self.subject = subject

    def csv_file(self):
        '''Setting up the smtp library

            Opening the .csv file to take the names and email ids from it

            Using MIMEMultiport module to set up From, To and Subject '''
        
        server = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
        server.starttls() # Secure the connection
        server.login('examplemailid51@gmail.com', 'ExampleMailId@51')
        with open('emailids.csv') as f:
            # reads each lines from csv files
            read = csv.reader(f)
            # to skip the first line from csv files
            next(read)
            for name, mailid in read:
                # MIMEMultipart and MIMEText is used to encode From, To and Subject
                msg = MIMEMultipart()
                msg['From'] = self.send
                msg['To'] = mailid
                msg['Subject'] = self.subject
                email = open(self.file_name, 'r')
                message = email.read()
                msg.attach(MIMEText(message, 'plain'))
                text = msg.as_string()
                
                # sendmail(sender, receiver, message)
                server.sendmail(self.send, mailid, text)
                print(f'Sent to {name}')
        server.close()
e = Email('Email.txt', 'examplemailid51@gmail.com', 'Python')
e.csv_file()
