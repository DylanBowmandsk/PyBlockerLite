import time
from datetime import datetime as dt

hosts_path=r"C:\Windows\System32\drivers\etc\hosts"
redirect="127.0.0.1"
blockList = []
with open("blocklist.txt","r") as file:
    content = file.readlines()
    for word in content:
        blockList.append(word)
        

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,8) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,16):
        with open(hosts_path,"r+") as file:
            content=file.read() 
            for website in blockList:
                if website in content:
                    pass
                else:
                    file.write(redirect+" "+website)
    else:
        with open(hosts_path, "r+") as file:
            content=file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in blockList):
                    file.write(line)
            file.truncate()
    time.sleep(5)
