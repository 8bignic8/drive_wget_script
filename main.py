import os
link = input('Please insert link from drive.google.com: ') #reads the input of the user and saves it in link
link_id = link.split('/')[5] #splits link at 5th backsalsh and saves it in link_id
#print(link_id)
dateinamen = input('please insert filename with file extension: ')#reads the input of the user and saves it in dateinamen
#print(dateinamen)
ausgabe = ("wget --load-cookies /tmp/cookies.txt \"https://docs.google.com/uc?export=download&confirm=$(wget --quiet --save-cookies /tmp/cookies.txt --keep-session-cookies --no-check-certificate 'https://docs.google.com/uc?export=download&id=")+link_id+(r"' -O- | sed -rn 's/.*confirm=([0-9A-Za-z_]+).*/\1\n/p')&id=")+link_id+("\" -O ")+dateinamen+(r" && rm -rf /tmp/cookies.txt")
# puts togehter the string wir the generated variables above
os.system(ausgabe) #puts out the generates string so that the system can perform it
