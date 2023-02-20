# Sending Emails from csv file

# import required libraries
import csv
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    ''' A class to represent the working of send mails from csv files '''

    def __init__(self, file_name, send, subject):
        '''Intializing instance variables'''
        self.file_name = file_name
        self.send = send
        self.subject = subject

    def csv_file(self):
        '''Setting up the smtp library

        Opening the .csv file to take the names and email ids from it

        Using MIMEMultiport module to set up From, To and Subject '''

        # Using the SMTP function from smtplib and writing the smtp domain url of gmail and port number
        server = smtplib.SMTP(host='smtp.gmail.com', port=587)

        # Put the SMTP connection in TLS (Transport Layer Security) mode.
        server.starttls()
        server.login('example@gmail.com', 'password')

        with open('emailids.csv') as fname:
            # reads each lines from csv files
            read = csv.reader(fname)
            # to skip the first line from csv files
            next(read)
            for name, mailid in read:
                # MIMEMultipart and MIMEText is used to encode From, To and Subject
                msg = MIMEMultipart()
                msg['From'] = self.send
                msg['To'] = mailid
                msg['Subject'] = self.subject
                file = open(self.file_name, 'r')
                data = file.read()
                # mail with username
                a = 'candidate'
                d = data.replace(a, name)
                d2 = data.replace(d, a)
                file.close()
                file = open(self.file_name, 'w')
                message = file.write(d)
                file.close()
                file = open(self.file_name, 'r')
                message = file.read()
                msg.attach(MIMEText(message, 'plain'))
                text = msg.as_string()
                server.sendmail(self.send, mailid, text)
                file.close()
                print(f'Sent to {name}')
                file = open(self.file_name, 'w')
                message = file.write(d2)
                file.close()
        server.close()


e = Email('Email.txt', 'example@gmail.com', 'Python Project')
e.csv_file()
