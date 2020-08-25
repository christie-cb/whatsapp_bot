# WhatsApp Bot

You can use this to automatically send messages on WhatsApp.
Put this script on your crontab and put some messages into messages.txt
to schedule messages.

I'm a lousy texter so I made this to schedule messages to my mum
and to my bf. You can also use it to send reminders to yourself;
simply add yourself as a contact and enter the contact as the recipient.

<h2> How to use </h2>

Put the contact name into the 'recipient' field. Write a message in
messages.txt and it will get sent. If you want to randomly send one 
of several messages, add each different message to a different line in
messages.txt and it'll randomly choose one for you.

WhatsApp can't already be open in another window in your browser, otherwise
this will not work.

Make sure your phone is connected to the internet. 

When you first run start_session, you'll need to scan the QR code to
access whatsapp web. The script will save the session into a folder
called 'session'. 

Also, you will need to enter the path to chromedriver in start_session.
