# oiam
# one in a million
# client that sends a request to the oiam webserver, retrieves the data sent, and copies it to clipboard 

# Mason Dructor August 2019

import requests

# server address
URL = 'http://10.128.0.2:8080'

data = requests.get(URL).text # request data from the URL
print(data) # copy data to system clipboard

