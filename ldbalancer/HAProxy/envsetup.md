## HAProxy Server Setup

OS: Ubuntu 14.04 LTS
IP Address: 192.168.0.125
Hostname: 

## Client Web Server Setup

Web Server #1: Ubuntu 14.04 LTS [IP: 192.168.0.121] - [hostname: ]
Web Server #2: Ubuntu 14.04 LTS [IP: 192.168.0.122] - [hostname: ]
## Installing Apache and Deploying Flask on Client Servers
* Place Web Application code inside directory
For example,`/var/www/NuageWebApplication`
Directory structure is:-
|----NuageWebApplication
|---------code
|------------templates
|------------app.py
* Download and Install Apache webserver
`apt-get install apache2`
* Install and enable mod_wsgi for Apache
`apt-get install libapache2-mod-wsgi`
`service apache2 restart`
* Configure and Enable Virtual Host
`nano /etc/apache2/sites-available/NuageWebApp.conf`
Add the following lines:-
```
<VirtualHost *:80>
		ServerName IPAddress
		ServerAdmin admin@IPAddress
		WSGIScriptAlias / /var/www/NuageWebApplication/code/app.wsgi
		<Directory /var/www/NuageWebApplication/code/>
			Order allow,deny
			Allow from all
		</Directory>
		ErrorLog ${APACHE_LOG_DIR}/error.log
		LogLevel warn
		CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
Save and close the file.
Enable Virtual Host using the command
`a2ensite NuageWebApp`
* Create Python file `app.wsgi` in our directory. The code in this file will import the main Flask application object and will be actually executed by the WSGI module of Apache. We are extending the Python classes path to include our own webapplication's folder.
Refer to [code/app.wsgi](code/app.wsgi)
* Restart Apache
`service apache2 restart`

## Installing HAProxy Server

* Download and install HAProxy
`apt-get install haproxy`
* Configure HAProxy Logs. Open the main HAProxy config file
`vim /etc/haproxy/haproxy.cfg`
Replace the following lines,
```
log /dev/log        local0
log /dev/log        local1 notice
``` 
With,
`log         127.0.0.1 local2`
* Enable UDP syslog reception in ?/etc/rsyslog.conf? configuration file. Uncommnet ModLoad and UDPServerRun, Here our Server will listen to Port 514 to collect the logs into syslog.
```
# Provides UDP syslog reception
$ModLoad imudp
$UDPServerRun 514
```
* Create a separate file ?haproxy.conf? under ?/etc/rsyslog.d/? directory to configure separate log files.
`local2.*	/var/log/haproxy.log`
* Restart the rsyslog service to update the new changes.
`service rsyslog restart`

## Configuring HAProxy Global Settings

* Refer to [ldbalancer/HAProxy/config](ldbalancer/HAProxy/config)
* Restart the HAProxy and make it persistant at system startup.
`service haproxy restart`
* Set “ENABLED” option to “1” in ‘/etc/default/haproxy‘ file.
`ENABLED=1`

## Configuring SSL

* Enable SSL and restart Apache
```
a2enmod ssl
service apache2 restart
```
* Navigate to SSL library and create certificates
```
cd /etc/ssl/
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout /etc/ssl/mykey.key -out /etc/ssl/mykey.crt
cat mykey.crt mykey.key > mykey.pem
```
* Make changes to [ldbalancer/HAProxy/config](ldbalancer/HAProxy/config). Check lines after the comment SSL under Frontend/Backend.
* Restart HAProxy.
`service haproxy restart`
* Fix warning by making changes to [ldbalancer/HAProxy/config](ldbalancer/HAProxy/config). Check lines after the comment Warning Fix under Global.

## Enable Ports Rules on IP Tables
* Make changes to [firewall/iptables/config](firewall/iptables/config) to allow required ports.