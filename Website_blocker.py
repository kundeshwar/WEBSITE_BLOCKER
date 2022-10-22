import datetime
import time

end_time = datetime.datetime(2022,10,15)#i block this website for one day
site_block = ["www.wscubetech.com","www.facebook.com"]
host_path = "C:/Windows/System32/drivers/etc/hosts"
redirect = "127.0.0.1"

while True:
    if datetime.datetime.now() < end_time:
        print("start Blocking")
        with open(host_path,"r+") as f:
            a = f.read()
            for website in site_block:
                if website not in a:
                    f.write(redirect + " "+ website+"\n")
                else:
                    pass
    else:
        with open(host_path,"r+") as f:
            a = f.readline()
            f.seek(0)
            for lines in a:
                if not any(website in lines for website in site_block):
                    f.write(lines)

            f.truncate()
        time.sleep(5)
