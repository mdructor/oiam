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

AppEnginePython URL

AppEngine JAVA URL

VM Python URL

VM Java URl

