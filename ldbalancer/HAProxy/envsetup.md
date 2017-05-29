## HAProxy Server Setup
OS: Ubuntu 14.04 LTS
IP Address: 192.168.0.125
Hostname: 
## Client Web Server Setup
Web Server #1: Ubuntu 14.04 LTS [IP: 192.168.0.121] - [hostname: ]
Web Server #2: Ubuntu 14.04 LTS [IP: 192.168.0.122] - [hostname: ]
## Installing Apache and Deploying Flask on Client Server
* Place Web Application code inside directory
For example,`~/git/NuageWebApplication/code`
* Create Python file `~/git/NuageWebApplication/code/app.wsgi`. The code in this file will import the main Flask application object and will be actually executed by the WSGI module of Apache.
