import requests
import time

with open('urls.txt', 'r') as f:
    LINES = [line.strip() for line in f]


def time_requests():
    for i in LINES:
       
        split = (i).split('@')
        URLS = split[1]
        t1 = time.time()
        try:
            r = requests.get(URLS)
        except requests.exceptions.ConnectionError:
            r.status_code = "Connection refused"    
        if r.status_code == 200:
            t2 = time.time()
            file.write(i + ' ' + str(t2-t1) + ' ' + r.text.strip() + '\n')
        else:
            file.write(i + ' ' + str(t2-t1)+ ' ' + "error\n") 
            print(URLS + ': status_code ' + str(r.status_code))
        

if __name__ == '__main__':
    file = open("TimingResults.txt", 'w')
    time_requests()
    file.close()
