# oiam
## one in a million

`oiam` is an extremely simple server/client application. 

The server generates and serves a random number from 1-1,000,000 (inclusive) on each request.

The client sends a request to the server, retrieves the data, and copies the number to the system clipboard.

Both the client and server are in `python` and about 5-10 lines of code each.

The server and client rely on the following `python` dependencies (all easily installable via `pip`):

`bottle`

`requests`

`pyperclip`

After installing the dependencies, you can run `oiam` by

1) Running the server

    `python oiam_server.py`

2) Running the client

    `python oiam_client.py`

3) Paste your random number to see what you got! Everytime
you run the client, a request for a new number will be sent and copied to 
the clipboard.



<sup><sub>All code and documentation produced by Mason Dructor<sup><sub>


