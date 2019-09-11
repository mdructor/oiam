# oiam
## one in a million

`oiam` is a simple server/client application. 

On every request, it generates a random number between 1 and 1,000,000 (inclusive) and serves it.

It is currently implemented as 4 different services, a python and java
implementation running on a virtual machine on Gcloud, as well as a python and java version running on the AppEngine on Gloud.

The python versions are using `flask` on AppEngine and `bottle` on the vm.

The Java version is using `tomcat` on AppEngine and Sun's `HttpServer` on the vm.

All of the programs behave relatively the same, and can be accessed via
the following URLS:

* https://one-in-a-million252417.appspot.com

* https://one-in-a-million-251918.appspot.com

* http://35.239.61.141:8080

* http://35.239.61.141:8000

### Process

For running the virtual machine, we opened a Tmux session and detached from it so that our web servers would be running all of the time. Below you can see the Tmux session running the java web server (left) and python web server (right) simultaneously:
![tmux](screenshots/tmux.png)


Afterwards, we had to configure our VM's firewall settings so that our web servers were listening on ports 8000 and 8080. 
![firewall](screenshots/firewall.png)

You can see both running in a web browser below:
#### Python VM
![python vm](screenshots/python-vm.png)
#### Java VM
![java vm](screenshots/java-vm.png)
