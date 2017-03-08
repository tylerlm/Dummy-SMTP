#!/usr/bin/env python

import os
import smtpd
import asyncore
import time
import argparse
import socket



class FakeSMTPServer(smtpd.SMTPServer):
    """A simple SMTP server that saves mails to a directory instead of sending them"""
    
    def __init__(self, address, port, maildir):
        smtpd.SMTPServer.__init__(self, (address, port), None)
        self.maildir = maildir

    def process_message(self, peer, mailfrom, rcpttos, data):
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        file = '%s/%s.eml' % (self.maildir, timestamp)
        print "New mail sent by %s:%s from %s to %s saved to %s" % (peer[0], peer[1], mailfrom, rcpttos, file)
        handle = open(file, "w")
        handle.write(data)
        handle.close
        
        
        
parser = argparse.ArgumentParser()

parser.description = ('Start a simple SMTP server that saves mails to a directory instead of sending them')

parser.add_argument('maildir',
    help='directory to save mails to')
                      
parser.add_argument('-a', '--address', default='localhost',
    help='address to listen on, default is localhost')
                    
parser.add_argument('-p', '--port', type=int, default=25,
    help='port to listen on, default is 25')
                    
                    

if __name__ == "__main__":
    args = parser.parse_args()
    
    if not os.path.isdir(args.maildir):
        print 'Error: The maildir "' + args.maildir + '" does not exist'
    else:
        try:
            smtp_server = FakeSMTPServer(args.address, args.port, args.maildir)
            print 'fakesmtp listening on %s:%s' % (args.address, args.port)
        except socket.error:
            print "Error: Cannot listen on port %s" % args.port
            
        try:
            asyncore.loop()
        except KeyboardInterrupt:
            smtp_server.close()
            print 'fakesmtp stopped'
