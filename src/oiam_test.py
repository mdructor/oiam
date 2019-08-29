# oiam
# one in a million
# client that sends a request to the oiam webserver, retrieves the data sent, and copies it to clipboard 

# Mason Dructor August 2019

import requests

# server address
URL = 'http://10.128.0.2:8080'

def test():
    test_count = 10
    test_size = 1000 
    for i in range(test_count):
        test_array = []
        for j in range(test_size):
            test_array.append(int(requests.get(URL).text))
        test_array = list(dict.fromkeys(test_array))
        print('Test ' + str(i + 1) + ': ', end='' )
        msg = 'PASSED! ' if (len(test_array) >= 750) else 'FAILED! '
        print(msg + str(test_size - len(test_array)) + ' duplicate(s) found.')
        

if __name__ == '__main__':
    test()
