# oiam
# one in a million
# bare bones web server that will serve a random number between 1-1million 

# Mason Dructor August 2019

from bottle import route, run
from random import randint

LOWER = 1
UPPER = 1000000

@route('/')
def serve_number():
    return str(randint(LOWER, UPPER + 1))


if __name__ == "__main__":
    run (host='0.0.0.0', port=8080, debug=True)

           

