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


As a daemon
-----------
This demonstrates adding a systemd unit to run the script as a daemon. These instructions are for Debian 8, but should (?) work on any distribution using systemd. 

To configure your daemon (paths, address and port, user), look at `fakesmtp.service` after you've copied it to `/etc/systemd/system/`. For example, if you wanted it to listen to the outside world you would change the `ExecStart=` line to `ExecStart=/usr/bin/python /usr/local/bin/fakesmtp -a 0.0.0.0 -p 2525 /var/lib/fakesmtp/mail`

Do this as root, or prefix each command with `sudo`:

1. Clone the repo: `git clone https://github.com/tylerlm/fakesmtp.git /opt/fakesmtp`
2. Symlink the script into /usr/local/bin: `ln -s /opt/fakesmtp/fakesmtp.py /usr/local/bin/fakesmtp`
3. Create a system user: `useradd -rU fakesmtp` 
4. Create a directory for the mails: `mkdir -p /var/lib/fakesmtp/mail`
5. `chown -R fakesmtp:fakesmtp /var/lib/fakesmtp`
6. Copy the systemd unit file: `cp /opt/fakesmtp/fakesmtp.service /etc/systemd/system/`
7. Take a look at `/etc/systemd/system/fakesmtp.service` and make sure paths/addresses/ports/user are correct.
8. `systemctl enable fakesmtp.service`
      
Run `service fakesmtp start` to bring up the fakesmtp daemon, it defaults to localhost:2525 saving mails to `/var/lib/fakesmtp/mail`. `service fakesmtp stop` stops it, `service fakesmtp status` will tell you its status.

If you edit the *.service file, make sure you do `systemctl daemon-reload; service fakesmtp restart`.


Test emails
-----------
Use `send_test_email.py` to send a quick lorem-ipsum-filled test email. 

    send_test_email.py [-a ADDRESS] [-p PORT] [-f SENDER] [-t RECIPIENT] [-s SUBJECT]

    Send a test email to a given SMTP server

    optional arguments:
      -a ADDRESS, --address ADDRESS
                            address to send to, default is localhost
      -p PORT, --port PORT  port to send to, default is 25
      -f SENDER, --sender SENDER
                            email sender, default is sender@example.com
      -t RECIPIENT, --recipient RECIPIENT
                            email recipient, default is recipient@example.com
      -s SUBJECT, --subject SUBJECT
                            email subject, default is Test Email 20170101-000000


Credits
-------

Original script by [Stuart Colville](http://muffinresearch.co.uk/archives/2010/10/15/fake-smtp-server-with-python/).
Forked from [Jevin](http://www.technoreply.com/finally-a-dummy-smtp-for-linux/). 
Argument parsing adapted from a fork by [David Volquartz Lebech](https://github.com/dlebech/Dummy-SMTP).