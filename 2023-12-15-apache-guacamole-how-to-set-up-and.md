---
title: "Apache Guacamole with Cloudflare: How to Set up and Secure Remote Access to All the Things"
date: 2023-12-15
author: Andy Lombardo
source: https://www.edtechirl.com/p/apache-guacamole-how-to-set-up-and
---

# Apache Guacamole with Cloudflare: How to Set up and Secure Remote Access to All the Things

[![](https://substackcdn.com/image/fetch/$s_!k0F4!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77ba8d2f-c159-45fb-bae6-307b6fc20065_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!k0F4!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77ba8d2f-c159-45fb-bae6-307b6fc20065_1024x1024.png)

*Disclaimer: Providing external access to your environment is never something to be taken lightly. Please consider the sensitivity of your environment and the security controls you have in place before creating external access to internal resources, regardless of the method you use to provide access.*

My paranoia may come out a little in this post, but when you’re dealing with exposing yourself to the internet (ha), it pays to have defense in depth and to not trust anybody. However, we frequently find ourselves off-site and in need of quick, reliable, secure access to on-prem infrastructure. We’ve tried lots of different methods, ranging from TeamViewer to VPN access to RAPs to poking holes in the firewall so we can RDP from home IPs. None of these are perfect solutions. As a solution for remote access while on-prem, I’ve been using an RDP gateway called Apache Guacamole for about two years and I love it. So, then the mission became how do I make this accessible off-prem, securely? The rest of this article will describe what Guacamole is and how to set it up for remote access in a way that is secure and stable.

## What does Guacamole do?

Once configured (more on that later), Guacamole gives you a dashboard of connections over RDP, VNC, SSH, Telnet (yuck), or Kubernetes sessions with the network information and credentials already included. So once you’re in Guacamole, all you have to do it click on a connection to make a remote connection to the device inside of your browser. After you click on a connection, it will open up a session in the browser like in the image below.

[![](https://substackcdn.com/image/fetch/$s_!R5FL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc748396c-6a74-4c6e-b1f8-ff32d86de6e3_2191x1251.png)](https://substackcdn.com/image/fetch/$s_!R5FL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc748396c-6a74-4c6e-b1f8-ff32d86de6e3_2191x1251.png)

From an administrative standpoint, you can also create connection groups. For example, you can make a group for Domain Controllers that houses all of your DCs; a group for Cameras for connections to your security cameras or NVR servers; an IoT group for connections to vape sensors, lighting controllers, etc. The options are endless based on your infrastructure.

The power of these groups comes in providing role-based access. If you have a staff member who needs to access all of your IoT group, but nothing else, you can assign them access to only be able to see and make connections to the IoT group when they sign in to Guacamole. Similarly, if you have a contractor or other 3rd party that needs access to a group or a specific machine, you can tailor their remote access to just that one device or group by editing their user account and checking the appropriate boxes:

[![](https://substackcdn.com/image/fetch/$s_!e2XJ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61540771-86e4-481e-872c-edf6edeca1f4_340x231.png)](https://substackcdn.com/image/fetch/$s_!e2XJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61540771-86e4-481e-872c-edf6edeca1f4_340x231.png)

As one use case for this, we have several vendors who offer support on specific systems (cameras, phones, IoT). Whereas we may have previously provided them a jumpbox accessed by TeamViewer, we can now funnel them through Guacamole. Or, in some cases, we’ve been able to cut out the jumpbox and provide access to just the webapp they need through the Cloudflare process described later in this article.

## Use Cases

- Providing on-prem access to servers, desktops, and networked devices for IT staff
- Providing remote access to servers, desktops, and networked devices for IT staff
- Providing remote, role-based access to servers and desktops for other internal or external entities who require access.

## Setting the Stage: Spinning up Ubuntu Server

Start by setting up a Linux server in your environment. For the sake of this walk through, we’ll be using the Ubuntu Server 22.04 LTS release with no desktop environment. The are multiple ways to skin the avocado though… there are tons of tutorials online for setting up Guacamole using Docker. I have personally not had luck setting up Guacamole through Docker and still being able to manage user accounts and enable MFA the way I wanted to. It’s almost certainly a user-problem, but I’ve just more consistently had luck running this directly from a server.

## Installing Guacamole Server

Start by updating your repos and upgrading Linux. If prompted to restart services, you can stick with the default.

```
sudo apt update && sudo apt upgrade -y
```

Next, install the appropriate dependencies. If prompted to restart services, you can stick with the default.

```
sudo apt install build-essential libcairo2-dev libjpeg-turbo8-dev \
    libpng-dev libtool-bin libossp-uuid-dev libvncserver-dev \
    freerdp2-dev libssh2-1-dev libtelnet-dev libwebsockets-dev \
    libpulse-dev libvorbis-dev libwebp-dev libssl-dev \
    libpango1.0-dev libswscale-dev libavcodec-dev libavutil-dev \
    libavformat-dev -y
```

Download the source for Guacamole from Apache.org:

```
wget https://archive.apache.org/dist/guacamole/1.5.3/source/guacamole-server-1.5.3.tar.gz
```

Extract the source code:

```
tar -xvf guacamole-server-1.5.3.tar.gz
```

Navigate to this directory:

```
cd guacamole-server-1.5.3
```

Build the Guacamole server. First:

```
sudo ./configure --with-init-dir=/etc/init.d --enable-allow-freerdp-snapshots
```

Then:

```
sudo make
```

And:

```
sudo make install
```

Next, update the library cache:

```
sudo ldconfig
```

Reload the daemon:

```
sudo systemctl daemon-reload
```

Start guacd:

```
sudo systemctl start guacd
```

And Enable:

```
sudo systemctl enable guacd
```

Make a directory for Guacamole extensions (you’ll use this when it’s time to setup MFA):

```
sudo mkdir -p /etc/guacamole/extensions
```

You’ll also need this directory:

```
sudo mkdir -p /etc/guacamole/lib
```

## Installing Guacamole Web App

Install Apache Tomcat

```
sudo apt install tomcat9 tomcat9-admin tomcat9-common tomcat9-user -y
```

Download the Guac client:

```
wget https://archive.apache.org/dist/guacamole/1.5.3/binary/guacamole-1.5.3.war
```

Move guacamole-1.5.3.war to the Tomcat web directory:

```
sudo mv guacamole-1.5.3.war /var/lib/tomcat9/webapps/guacamole.war
```

Restart Tomcat and Guacd:

```
sudo systemctl restart tomcat9 guacd
```

## Configure Database Authentication

Install MariaDB:

```
sudo apt install mariadb-server -y
```

Complete the initial SQL secure installation wizard:

```
sudo mysql_secure_installation
```

Download the MySQL Java Connector:

```
wget https://dev.mysql.com/get/Downloads/Connector-J/mysql-connector-java-8.0.26.tar.gz
```

Extract the Java connector

```
tar -xf mysql-connector-java-8.0.26.tar.gz
```

and move to /etc/guacamole/lib:

```
sudo cp mysql-connector-java-8.0.26/mysql-connector-java-8.0.26.jar /etc/guacamole/lib/
```

Download the JDBC Auth plugin from Apache:

```
wget https://archive.apache.org/dist/guacamole/1.5.3/binary/guacamole-auth-jdbc-1.5.3.tar.gz
```

Extract it:

```
tar -xf guacamole-auth-jdbc-1.5.3.tar.gz
```

Move it to /etc/guacamole/extensions:

```
sudo mv guacamole-auth-jdbc-1.5.3/mysql/guacamole-auth-jdbc-mysql-1.5.3.jar /etc/guacamole/extensions/
```

Login to MariaDB as root:

```
mysql -u root -p
```

After MariaDB loads, you should be at a MariaDB SQL prompt like below:

[![](https://substackcdn.com/image/fetch/$s_!Mm3b!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fbce447-2aeb-4766-a439-678eea33e7a5_215x37.png)](https://substackcdn.com/image/fetch/$s_!Mm3b!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3fbce447-2aeb-4766-a439-678eea33e7a5_215x37.png)

Once at that prompt, run the following command to change the root password (replace ‘password’ with the ‘desired password’), create the Guacamole database, create a db user for Guacamole, set the password for the Guacamole db user, and assign privileges.

```
ALTER USER 'root'@'localhost' IDENTIFIED BY 'password'; CREATE DATABASE guacamole_db; CREATE USER 'guacamole_user'@'localhost' IDENTIFIED BY 'password'; GRANT SELECT,INSERT,UPDATE,DELETE ON guacamole_db.* TO 'guacamole_user'@'localhost'; FLUSH PRIVILEGES;
```

Exit SQL:

```
quit
```

Now that you’re back at the Linux prompt, change directories:

```
cd guacamole-auth-jdbc-1.5.3/mysql/schema
```

Import SQL schema files to the MariaDB:

```
cat *.sql | mysql -u root -p guacamole_db
```

Create the Guacamole Properties file:

```
sudo nano /etc/guacamole/guacamole.properties
```

Paste in the following configuration. Be sure to update the database password with the password you set in the steps above.

```
# MySQL properties 

mysql-hostname: 127.0.0.1 

mysql-port: 3306 

mysql-database: guacamole_db 

mysql-username: guacamole_user 

mysql-password: password
```

Ctrl-X to quit nano, Y then Enter to save the properties file.

Next, restart services:

```
sudo systemctl restart tomcat9 guacd mysql
```

## Checkpoint!

Now, if everything has gone to plan so far, if you go to the IP of your server at port 8080 (e.g., 192.168.1.125:8080, localhost:8080), you’ll see a landing page for Tomcat like below:

[![](https://substackcdn.com/image/fetch/$s_!urkd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe64cb103-7e97-483e-844a-0b329862743a_920x501.png)](https://substackcdn.com/image/fetch/$s_!urkd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe64cb103-7e97-483e-844a-0b329862743a_920x501.png)

On the one hand, this is awesome because, well, you just made a webserver and here it is!

On the other hand, when you go to port 8080, you want to see Guacamole, and this isn’t guacamole. For those more skilled in webserver administration, there are almost definitely better ways to do this (and I’d love it if you let me know how in the comments), but basically Tomcat and Guacamole are fighting over who gets this port, and Tomcat wins. To fix this, I take the Tomcat ROOT web directory and copy it to ROOT\_backup, and make a symbolic link between Guacamole and the ROOT directory to trick Tomcat into displaying the Guacamole webapp instead of Tomcat using the steps below:

Backup the Root directory:

```
sudo mv /var/lib/tomcat9/webapps/ROOT /var/lib/tomcat9/webapps/ROOT_backup
```

Create a link from Guacamole to the ROOT directory:

```
sudo ln -s /var/lib/tomcat9/webapps/guacamole /var/lib/tomcat9/webapps/ROOT
```

Restart Services:

```
sudo systemctl restart tomcat9 guacd mysql
```

NOW you should see a bona fide Guacamole sign in page:

[![](https://substackcdn.com/image/fetch/$s_!F4fm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e2262d0-2ead-4b63-955c-9dd6957d03b0_807x608.png)](https://substackcdn.com/image/fetch/$s_!F4fm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e2262d0-2ead-4b63-955c-9dd6957d03b0_807x608.png)

For testing purposes, you can now log in to Guacamole with the un/pw combo guacadmin/guacadmin. If you’re playing around and just want this in your homelab , this can be as far as you need to go. However, this is a great time to set up some added security with MFA and Cloudflare, as well as a chance to set up your Guac for remote access. You may also note that at this point, this is an insecure HTTP site accessed by IP. We’ll fix both of these problems in the coming steps.

# Securing and Exposing Guacamole

## Default Admin Account

To make MFA easier in the next step, now is a good time to disable the default guacadmin account. Start by signing in to Guacamole using the default credentials (guacadmin/guacadmin), and then go to the account info in the upper-right hand corner of the screen and select Settings → Users → +New User

[![](https://substackcdn.com/image/fetch/$s_!KU62!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8338ff49-56c2-4f61-bbb5-a4cded257fd7_1268x477.png)](https://substackcdn.com/image/fetch/$s_!KU62!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8338ff49-56c2-4f61-bbb5-a4cded257fd7_1268x477.png)

From here, you can create a solid, secure username and password. You can also add additional time- and date-based access restrictions. These should remain unconfigured on your admin account, but when you start to delegate access to other users, especially external users, this is a valuable tool to prevent privilege creep over time. This page is also where you can assign users access to only specific connections or connection groups.

[![](https://substackcdn.com/image/fetch/$s_!mIwt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30aea4b5-e0cc-4f35-aae7-57e41dde7900_409x422.png)](https://substackcdn.com/image/fetch/$s_!mIwt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30aea4b5-e0cc-4f35-aae7-57e41dde7900_409x422.png)

On the administrator account, you should also be sure that you provision the new account with permission to administer Guacamole:

[![](https://substackcdn.com/image/fetch/$s_!S0xr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe37d914b-1ec7-4dee-b80a-e59863071a0a_319x248.png)](https://substackcdn.com/image/fetch/$s_!S0xr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe37d914b-1ec7-4dee-b80a-e59863071a0a_319x248.png)

Once you have created —and tested— your new admin account, it’s best practice to go back to Settings —> Users —> click on guacadmin and either disable or preferably delete the account. At a minimum, the password should be reset.

[![](https://substackcdn.com/image/fetch/$s_!OgQl!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5dc2eb8-7869-403d-b093-87f51d1fc8f1_1170x1455.png)](https://substackcdn.com/image/fetch/$s_!OgQl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa5dc2eb8-7869-403d-b093-87f51d1fc8f1_1170x1455.png)

## Configuring MFA

Luckily, Guacamole has a pre-made extension that can be used to enable time-based one-time passcode MFA. To set it up:

Download the Guacamole TOTP extension:

```
wget https://archive.apache.org/dist/guacamole/1.5.3/binary/guacamole-auth-totp-1.5.3.tar.gz
```

Extract it:

```
tar -xf guacamole-auth-totp-1.5.3.tar.gz
```

Move the extracted jar file to the /etc/guacamole/extensions directory:

```
sudo mv guacamole-auth-totp-1.5.3/guacamole-auth-totp-1.5.3.jar /etc/guacamole/extensions/
```

The Guacamole documentation specifically states that a full restart isn’t required, but I’ve had mixed luck on the half dozen or so Guac installs I’ve done. I’ve tried restarting only specific services, but I’ve found I usually spend more time troubleshooting than a shutdown would have required, so now I just restart the server:

```
sudo shutdown -r
```

After it comes back up, Guacamole should be accessible at port 8080 again. The next time you log-in, it should require MFA registration like below:

[![](https://substackcdn.com/image/fetch/$s_!WTmG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90c1d25a-2ba7-4185-9294-e887a8563c14_620x657.png)](https://substackcdn.com/image/fetch/$s_!WTmG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90c1d25a-2ba7-4185-9294-e887a8563c14_620x657.png)

Once you complete MFA registration, your new admin account should be active and protected by time-based OTP MFA.

## Remote Access and Reverse Proxy

So, you’ve evaluated your threat model, and now you’re ready to access Guacamole remotely.

### Create a Cloudflare Account

The first step will be to sign up for a free Cloudflare account. As a bit of editorial, Cloudflare is probably the coolest tool I’ve started using this year. What we’re going to use Cloudflare for in this tutorial is just about the top .001% of the surface of what’s possible.

### Purchase a Domain Name

You can use an existing domain that you already have access to, but for the sake of streamlining this doc, we’re going to do everything in Cloudflare because it saves time with configuration. The .uk domain is the cheapest offering they have at $4.17/year. To purchase a domain with Cloudflare, sign in and navigate to Domain Registration —> Register Domains and walk through the steps. If you want to use an existing domain name, there is a +Add Site button on the top banner of the Cloudflare dashboard where you can go to start the process of adding your existing domain. In the name of security by obscurity, if your domain doesn’t have to be look pretty, make it obscure and unrelated to your environment. If you work for ABC School System in Texas, no one would expect you to have a domain name like green.pickledokra.uk. If this is just a tool for you and your team, there’s no need for it to be a subdomain of your actual domain, because that just makes it too easy for those attackers who are enumerating your environment to identify a target. A domain like guacamole.my-school.org may as well be remoteaccesstoallthethings.my-school.org.

### Install Cloudflare Tunnels on your Guacamole Server

This is where the magic starts. In Cloudflare, navigate to Zero Trust —> Access —> Tunnels and click on Create a Tunnel:

[![](https://substackcdn.com/image/fetch/$s_!HJ9k!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa8db3a-0eff-4cd5-bc7d-ae0d8add5ed4_761x310.png)](https://substackcdn.com/image/fetch/$s_!HJ9k!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0aa8db3a-0eff-4cd5-bc7d-ae0d8add5ed4_761x310.png)

Walk through the wizard to name the tunnel. If you’ve followed this guide, you’ll select Debian —> 64-bit and you’ll copy the bit of code under “If you don’t have cloudflared installed on your machine.”

[![](https://substackcdn.com/image/fetch/$s_!O1Sn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc74c1bbe-30fd-4f3f-8d73-f4af5a2b9996_1082x883.png)](https://substackcdn.com/image/fetch/$s_!O1Sn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc74c1bbe-30fd-4f3f-8d73-f4af5a2b9996_1082x883.png)

Take this bit of code and run it on the server where Guacamole lives. The code snippet is customized and contains a token to access your environment. Please safeguard this token. After the commands complete, finish the tunnel wizard.

### Assign a Subdomain and Domain to Your Site

The last step of the wizard is to make up a subdomain and select the domain you attached to Cloudflare. If you purchased from Cloudflare, all this takes is clicking on the drop down and picking the domain. Finally, enter the IP and port where Cloudflare will access Guacamole (if the Cloudflare Tunnel is on the same server where your Guac webapp is hosted you can use http://localhost:8080 or http://127.0.0.1:8080).

[![](https://substackcdn.com/image/fetch/$s_!kFPE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb70c8cc9-d211-48fb-9d10-bec28194bab2_1103x387.png)](https://substackcdn.com/image/fetch/$s_!kFPE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb70c8cc9-d211-48fb-9d10-bec28194bab2_1103x387.png)

*NOTE: Be sure that you’ve selected HTTP under type. If you select HTTPS, you’ll get a Bad Gateway error from Cloudflare. That doesn’t mean you’re unencrypted though. Cloudflare serves as a reverse proxy, so your traffic will be served as HTTPS.*

Your tunnel should now display as HEALTHY:

[![](https://substackcdn.com/image/fetch/$s_!HcN6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37b71a7f-9546-47b7-9017-ac112c040f1e_736x221.png)](https://substackcdn.com/image/fetch/$s_!HcN6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F37b71a7f-9546-47b7-9017-ac112c040f1e_736x221.png)

At this point, your Guacamole instance should be accessible on the public internet (😬)

## Configure Cloudflare Access

Now that Guacamole is publicly accessible, we need to place some additional restrictions on who can access it. Even though we’ve set Guacamole up to require MFA, we really want to add layers to the security and prevent bad guys from even getting that far. From the main Cloudflare page, go to Zero Trust —> Access —> Applications. From here, you’ll click +Add an Application and select Self-Hosted.

[![](https://substackcdn.com/image/fetch/$s_!jW1W!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2ce0f8a-fd22-4c16-9c31-c0abe04e98bd_1155x564.png)](https://substackcdn.com/image/fetch/$s_!jW1W!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc2ce0f8a-fd22-4c16-9c31-c0abe04e98bd_1155x564.png)

Next, you’ll provide a name for the application, and enter the same subdomain and domain you previously entered for your tunnel.

[![](https://substackcdn.com/image/fetch/$s_!D6qt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2547c1a9-4b3e-4dac-a112-36c40570a5e6_1138x502.png)](https://substackcdn.com/image/fetch/$s_!D6qt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2547c1a9-4b3e-4dac-a112-36c40570a5e6_1138x502.png)

There are also some additional configurations you can make here on the Add an Application screen to customize error messages, add a logo, or add an identity provider. To get started, you can accept all the defaults and click Next. I’ve not done this yet, but my next addition to my Guacamole setup will be to add Azure as an Identity Provider in Cloudflare to enforce Entra ID group membership as a factor in gaining access. [Update: I set up Azure as an ID provider for Cloudflare today, and I definitely recommend this route. I’ll update with details in a separate post after I have a chance to test it more]

After configuring the application, it’s time to add a policy. As an example of the types of policy requirements you can add, you can require users to enter a one-time passcode sent to an email address in your organization, require sign in from the US, and require sign in only from specific IP addresses or ranges. For Guacamole in my environment, only 3 people require access, so the administrative burden of managing these 3 IP addresses plus the IP address range for our organization is light. This layer of defense on the application provides 3 specific hurdles someone has to overcome before being able to even get to the point of signing in with MFA. While this may seem like overkill, the broad exposure Guacamole can provide to your environment makes defense in depth necessary.

[![](https://substackcdn.com/image/fetch/$s_!Xqvd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1547230c-109c-4b30-bd7d-4e3f09d5f664_973x731.png)](https://substackcdn.com/image/fetch/$s_!Xqvd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1547230c-109c-4b30-bd7d-4e3f09d5f664_973x731.png)

After saving the application, if you meet the location and IP requirements you established in the app policy above, then visiting the subdomain and domain you specified will take you to a Cloudflare login page like below, where you’ll need to enter your email address and wait for the OTP code to be sent.

[![](https://substackcdn.com/image/fetch/$s_!p_Se!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d46df8f-0a01-4bf6-93f8-14e7e8706399_638x866.png)](https://substackcdn.com/image/fetch/$s_!p_Se!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d46df8f-0a01-4bf6-93f8-14e7e8706399_638x866.png)

After authenticating with the code, you’ll be directed to the Guacamole sign in page. Notice that the domain is being served over HTTPS with a valid certificate, thanks to the Cloudflare tunnel.

[![](https://substackcdn.com/image/fetch/$s_!E3YP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb01ccd29-a4a0-4b6d-a184-2e36972ce285_718x560.png)](https://substackcdn.com/image/fetch/$s_!E3YP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb01ccd29-a4a0-4b6d-a184-2e36972ce285_718x560.png)

If you don’t meet the conditional location/IP restrictions, you’ll see a page similar to this:

[![](https://substackcdn.com/image/fetch/$s_!nQA5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F696cca42-a3c7-4690-b6e5-5a57cfebb83b_403x564.png)](https://substackcdn.com/image/fetch/$s_!nQA5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F696cca42-a3c7-4690-b6e5-5a57cfebb83b_403x564.png)

In addition to the application policies we configured, there are also Cloudflare settings that can be configured under Websites —> [Your Site] —> Security —> WAF (web application firewall). You can explore the Traffic Sequence diagram on the right-hand side of WAF page for options. Many of these configuration options here are free, but some do require a paid subscription. Virtually each link here is a rabbit hole you can explore for ways to make access to your Guacamole more tailored to your needs.

[![](https://substackcdn.com/image/fetch/$s_!n9nP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcce654c1-0d11-4621-ab28-13a9a0c96456_1390x968.png)](https://substackcdn.com/image/fetch/$s_!n9nP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcce654c1-0d11-4621-ab28-13a9a0c96456_1390x968.png)

If you decide not to use Cloudflare for a layer of defense before logging in to Guacamole, you may want to consider installing Fail2Ban on the Guacamole server and integrating it with Cloudflare to provide some customizable options for stopping brute force attacks. A good walk-through of this process can be found in this [YouTube video from #Geek2Gether](https://www.youtube.com/watch?v=qblSFoXVEos), along with other great Guacamole setup tutorials.

## Configure Servers

As we wrap up setting up and securing the supporting infrastructure for Guacamole, it’s time to work on preparing to use it. Since Guacamole works by making a remote connection to your servers or computers using common protocols like RDP, VNC, and SSH, you have to enable the appropriate protocols on the servers. Since RDP and SSH are often-attacked protocols, it’s a good idea to make it a little harder for attackers to find. RDP usually operates on port 3389, so when attackers look for it, that’s where they start. To make it harder, you can manually change the RDP port (or VNC, SSH) to a non-standard port number. If the RDP port is changed to, say, 13450, an attacker is going to be very unlikely to find it while probing your network. To change this listening port on a Windows server, run the following PowerShell script to change the port number and create firewall rules to allow RDP on that port:

```
#Change port number 

$portvalue = 13450

Set-ItemProperty -Path 'HKLM:\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp' -name "PortNumber" -Value $portvalue 

New-NetFirewallRule -DisplayName 'RDPPORTLatest-TCP-In' -Profile 'Public' -Direction Inbound -Action Allow -Protocol TCP -LocalPort $portvalue 

New-NetFirewallRule -DisplayName 'RDPPORTLatest-UDP-In' -Profile 'Public' -Direction Inbound -Action Allow -Protocol UDP -LocalPort $portvalue
```

## Add Servers to Guacamole

Now that Guacamole is set up, secured, and remotely accessible, it’s time to make it useful by adding your connections.

### RDP

To add an RDP connection, you need the following information at a minimum:

- Hostname or IP address
- Port Number
- Username
- Password
- Domain (if applicable)

Once you’ve gathered the above information, navigate to Settings —> Connections —> New Connection.

In the “Edit Connection” section, enter the display name you want to use for the connection on your Guacamole dashboard and select the protocol. Under location, Root is the default location. If you have a Connection Group you want to use, this is where you would assign it (note: the Connection Group has to be created before you can assign a connection to it. Create a Connection Group under Settings —> Connections —> New Group).

[![](https://substackcdn.com/image/fetch/$s_!FcnG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F603a5a3b-9ccb-4d27-987f-1e4d3c7a0827_283x154.png)](https://substackcdn.com/image/fetch/$s_!FcnG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F603a5a3b-9ccb-4d27-987f-1e4d3c7a0827_283x154.png)

Next, scroll down to the Parameters section. Here you’ll enter the Hostname (or IP) of the device you want to connect to, followed by the port number. Enter the username and password used to access the resource and enter the domain it’s a member of if applicable. Select NLA (Network Level Authentication) under security mode. I usually check the “ignore server certificate error” box. If you normally get an insecure error when trying to access this resource on prep, but ignore it and connect anyway, checking this box will have the same result.

[![](https://substackcdn.com/image/fetch/$s_!NAcq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa27aa67b-457a-4c20-9a23-6076729d9fa4_475x386.png)](https://substackcdn.com/image/fetch/$s_!NAcq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa27aa67b-457a-4c20-9a23-6076729d9fa4_475x386.png)

Next, save the connection and go back to the Home link in your account info to go back to the main dashboard. You should now see the connection you created in your “All Connections” list.

[![](https://substackcdn.com/image/fetch/$s_!ywTt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08d3a173-7b36-45ca-921b-966b7a817145_425x564.png)](https://substackcdn.com/image/fetch/$s_!ywTt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F08d3a173-7b36-45ca-921b-966b7a817145_425x564.png)

When you test your connection, if it times out or fails, the most common culprit is needing to all RDP through the host-based firewall on that device. In Windows, this is accessed through the Windows Defender Firewall app and clicking on “Allow an app or feature through Windows Defender Firewall” and scroll down to RDP to ensure it’s enabled. You will need admin access on the device to make this change.

### SSH

The process for an SSH connection is similar to the above steps but substituting SSH and the appropriate port (22 unless you’ve changed it to a non-standard port). One notable difference is that you also have the ability to use an SSH keypair to authenticate if your server is configured for keypair access.

[![](https://substackcdn.com/image/fetch/$s_!KJmI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd71fc7c1-3417-47e5-b87e-abceae33fc07_482x459.png)](https://substackcdn.com/image/fetch/$s_!KJmI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd71fc7c1-3417-47e5-b87e-abceae33fc07_482x459.png)

## Other Neat Features to Consider in Guacamole

- Guacamole can be configured for screen recording of your sessions
- You can create a view-only link to a session so you can easily share your screen, similar to doing an RDP shadow session, but shareable on the internet.
- Copying and pasting text between host and remote
- Session logging to see who has open sessions, as well as session history for your users… and the ability to kill sessions
- Time- and date-based account access
- Set limits for number of connections
- SFTP file transfer between your computer and the remote computer
- Mouse emulation for touch devices (i.e., using Guacamole from an iPad to a remote PC)

## Resources:

Apache Guacamole™ <https://guacamole.apache.org/>

Installing Guacamole on Linode <https://www.linode.com/docs/guides/installing-apache-guacamole-on-ubuntu-and-debian/>

Cloudflare Zero Trust · Cloudflare Zero Trust docs <https://developers.cloudflare.com/cloudflare-one/>

Geek2Gether’s YouTube Channel has some good YouTube videos, esp. for setting up session sharing and session recording <https://www.youtube.com/@geek2gether469>
