import datetime
import time
end_time=datetime.datetime(2024,2,27)
site_block=["www.facebook.com","www.instagram.com"]
host_path="C:/Windows/System32/drivers/etc/hosts"
redirect="127.0.0.1"
 
while True:
     if datetime.datetime.now() <end_time:
         print("start blocking")
         with open(host_path,"r+") as host_file:
            content = host_file.read()
            for website in site_block:
              if website not in content:
                 host_file.write(redirect + " " + website + "\n")
            
else:
        with open(host_path,"r+") as host_file:
            content = host_file.readlines()
            host.file.seek(0)
            for lines in content:
                if not any(website in line for website in site_block):
    
    
                    host_file.write(lines)
            host.file.truncate()
        time.sleep(5)
                        

                             
