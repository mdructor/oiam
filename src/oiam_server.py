# oiam
# one in a million
# bare bones web server that will serve a random number between 1-1million 

# Mason Dructor August 2019

from bottle import route, run
from random import randint

LOWER = 1
UPPER = 1_000_000

@route('/')
def serve_number():
    return str(randint(LOWER, UPPER + 1))

run (host='0.0.0.0', port=5000, debug=True)
