#!/usr/bin/env python

import argparse
import smtplib
from email.mime.text import MIMEText
import time
import socket



timestamp = time.strftime("%Y%m%d-%H%M%S")

parser = argparse.ArgumentParser()

parser.description = ('Send a test email to a given SMTP server')

parser.add_argument('-a', '--address', default='localhost',
    help='address to send to, default is localhost')
    
parser.add_argument('-p', '--port', type=int, default=25,
    help='port to send to, default is 25')

parser.add_argument('-f', '--sender', default='sender@example.com',
    help='email sender, default is sender@example.com')

parser.add_argument('-t', '--recipient', default='recipient@example.com',
    help='email recipient, default is recipient@example.com')
    
parser.add_argument('-s', '--subject', default='Test Email ' + timestamp,
    help='email subject, default is Test Email ' + timestamp)



def send_email(host, port, sender, recipient, subject):
    msg = MIMEText('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient
    
    try:
        smtp = smtplib.SMTP(host, port)
        print "Connected to %s on port %s" % (host, port)
    except socket.error:
        print "Error: Cannot connect to %s on port %s" % (host, port)
        exit(1)
        
    print 'Sending test email...'
    smtp.sendmail(sender, [recipient], msg.as_string())
    smtp.quit()



if __name__ == "__main__":
    args = parser.parse_args()
    send_email(args.address, args.port, args.sender, args.recipient, args.subject)
