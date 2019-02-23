import time
from datetime import datetime as dt

host_temp =r"D:\hosts"
# the prefix r escape special characters
host_path =r"C:\Windows\System32\drivers\etc\hosts" #location of host file
redirect = "127.0.0.1" # redirect ip address when trying to access blocked site
website_list = ["www.facebook.com", "facebook.com"] #to append on host file

while True:
# run the script conntinuously
    if dt(dt.now().year, dt.now().month,dt.now().day,16) < dt.now() < dt(dt.now().year, dt.now().month,dt.now().day,22):
        print("Working Hours...")
        with open (host_temp,'r+',) as file:
            content = file.read()
            for website in website_list:
                if website in content:
                    pass #go to another line
                else:
                    file.write(redirect + " " + website + "\n")
    else :
        with open (host_temp,'r+') as file:
            content = file.readlines()
            file.seek(0) #go to the start of the file and insert new content excluding the blocked hostname
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate() #delete rest of the content after rewriting evverything except the blocked hostname
        print("Fun Hours . . . ")
    # to save processor resources delay the processes
    time.sleep(5)
