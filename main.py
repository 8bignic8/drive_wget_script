import os
link = input('Please insert link from drive.google.com: ')
link_id = link.split('/')[5]
#print(link_id)
dateinamen = input('please insert filename with file extension: ')
#print(dateinamen)
ausgabe = ("wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=")+link_id+(r"' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=")+link_id+("\" -O ")+dateinamen+(r" && rm -rf /tmp/cookies.txt")

os.system(ausgabe)
