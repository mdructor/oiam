import requests
import time

with open('urls.txt', 'r') as f:
    URLS = [line.strip() for line in f]

def time_requests():
    for i in URLS:
        t1 = time.time()
        r = requests.get(i)
        if r.status_code == 200:
            t2 = time.time()
            print(i + ': request took ' + str(t2-t1) + ' seconds. Number: ' + r.text.strip())
        else:
            print(i + ': status_code ' + str(status_code))

if __name__ == '__main__':
    time_requests()
