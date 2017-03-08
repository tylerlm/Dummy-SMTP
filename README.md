fakesmtp
========

A simple SMTP server that saves mails to a directory instead of sending them

Usage
-----

    fakesmtp.py [-a ADDRESS] [-p PORT] maildir
    
    Start a simple SMTP server that saves mails to a directory instead of sending them
    
    positional arguments:
      maildir               directory to save mails to
    
    optional arguments:
      -a ADDRESS, --address ADDRESS
                            address to listen on, default is localhost
      -p PORT, --port PORT  port to listen on, default is 25


Credits
-------

Original script by [Stuart Colville](http://muffinresearch.co.uk/archives/2010/10/15/fake-smtp-server-with-python/).
Forked from [Jevin](http://www.technoreply.com/finally-a-dummy-smtp-for-linux/). 
Argument parsing adapted from a fork by [David Volquartz Lebech](https://github.com/dlebech/Dummy-SMTP).