# gmail-pi-ping
Program, allows pi to detect unread emails and turns led on accordingly

Installation:

  1. Download Files And Place In Document Folder (/home/pi/Documents)
  2. Update Email Details
  3. Go to https://myaccount.google.com/lesssecureapps?utm_source=google-account&utm_medium=web&hl=en_GB and enable less secure apps.
  4. Update Cronotab (Below)
  5. Install Hardware (Images Below)
  6. Let It Run!
  
Hardware Image

  https://cdn.shopify.com/s/files/1/0176/3274/files/LEDs-BB400-1LED_bb_grande.png?6398700510979146820
  
Cronotab
  1. run command $ sudo cronotab -e
  2. add line (* * * * * python /home/pi/Documents/gmail_python/check_messages.py)
  3. save and exit
  
  
Any errors message me
