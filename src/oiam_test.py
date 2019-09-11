# oiam
# one in a million
# client that sends a request to the oiam webserver, retrieves the data sent, and copies it to clipboard

# Mason Dructor August 2019

import requests
import time

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total:
        print()

# server address
URL = 'http://35.239.61.141:8000'

def test():
    test_count = 10
    test_size = 1000
    printProgressBar(0, test_size, prefix = 'Test Progress:', suffix = 'Complete', length = 50)
    for i in range(test_count):
        test_array = []
        for j in range(test_size):
            r = requests.get(URL)
            if r.status_code == 200:
                test_array.append(r.text)
                printProgressBar(len(test_array), test_size, prefix = 'Test Progress:', suffix = 'Complete', length = 50)
            else:
                j -= 1
        test_array = list(dict.fromkeys(test_array))
        print('Test ' + str(i + 1) + ': ', end = '')
        msg = 'PASSED! ' if (len(test_array) >= 750) else 'FAILED! '
        print(msg + str(test_size - len(test_array)) + ' duplicate(s) found.')


if __name__ == '__main__':
    test()
