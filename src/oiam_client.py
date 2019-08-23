# oiam
# one in a million
# client that sends a request to the oiam webserver, retrieves the data sent, and copies it to clipboard 

# Mason Dructor August 2019

import requests
import pyperclip

# server address
URL = 'http://localhost:8080'

data = requests.get(URL).text # request data from the URL
pyperclip.copy(data) # copy data to system clipboard

