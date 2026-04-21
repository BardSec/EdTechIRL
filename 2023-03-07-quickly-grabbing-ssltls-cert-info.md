---
title: "Quickly Grabbing SSL/TLS Cert Info"
date: 2023-03-07
author: Andy Lombardo
source: https://www.edtechirl.com/p/quickly-grabbing-ssltls-cert-info
---

# Quickly Grabbing SSL/TLS Cert Info

[![](https://substackcdn.com/image/fetch/$s_!-oCL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61973a95-5325-4c91-af45-e8cf12772b75_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!-oCL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F61973a95-5325-4c91-af45-e8cf12772b75_1024x1024.png)

I’m far from an encryption expert, so when troubleshooting or researching certificate issues, it’s nice to have a quick go to for certificate information and history.

Using [crt.sh](https://crt.sh), it’s easy to pull up cert info by entering some identity details about the cert (domain name, org name, etc.) or a certificate fingerprint. It’s also an easy way to enumerate any subdomains that have held a certificate.

The simplest and most common way I use this is for a pretty simple reason - by putting in my top level domain, I can check the certificate expiration dates for all of my certs in chronological order on one screen.

For example, if I wanted to make sure this site’s cert wasn’t on the verge of expiration, I would go to crt.sh and enter edtechirl.com and get the following output:

[![](https://substackcdn.com/image/fetch/$s_!Ly-Z!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fdd285c-9227-48fd-ae5e-f6447a1bcf84_1044x101.png)](https://substackcdn.com/image/fetch/$s_!Ly-Z!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2fdd285c-9227-48fd-ae5e-f6447a1bcf84_1044x101.png)

I don’t have any subdomains so it’s a short list, but I can see at a glance that my cert is good till 29 Feb 2024.

Clicking on the top crt.sh ID yields the info below, where you can also check the revocation status of the cert or download a copy of the certificate.

[![](https://substackcdn.com/image/fetch/$s_!Wmuh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5f85432-ccd6-4cad-a053-48e8c52f28a8_1211x830.png)](https://substackcdn.com/image/fetch/$s_!Wmuh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5f85432-ccd6-4cad-a053-48e8c52f28a8_1211x830.png)

I’ve used this before when troubleshooting issues where I’ve incorrectly renewed a cert and changed a field like the Common Name, or if the CA has changed some information since the previous renewal and I need to track down where I have a mismatch. Having a history of the certs available here, I can go back and compare the current cert to previous certs.

On the exploratory side, there is a ton more information at hand if you have a more sprawling environment to manage or if you’re trying to track down OSINT. By looking at the relationships between Common Names, Identities, and Alternative Names in the certs, it also gives you an idea of other entities related to the certificate. In the case of the theme park Dollywood, for example, searching crt.sh shows that it is connected to a variety of other sites through their parent company: hfecorp.com, herschenduniversity.com, adventureaquarium.com, kentuckykingdom.com, newportaquarium.com, and even the harlemglobetrotters.com.

[![](https://substackcdn.com/image/fetch/$s_!LoJo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa89a761a-e266-48c7-a530-b7e4a08cfcb7_1847x809.png)](https://substackcdn.com/image/fetch/$s_!LoJo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa89a761a-e266-48c7-a530-b7e4a08cfcb7_1847x809.png)

Another way this can be fun is exploring for subdomains that maybe aren’t intended for public consumption to see what kind of tools are used or experimented with in an environment. A good place to explore this is to pick a large university. Chances are, there will be dozens of subdomains. Visit the ones with interesting or unusual names. You’ll most likely find some non-production test environments and a random assortment of admin portals, which can tell you more about the overall environment. You may find hints about infrastructure if intuitive domain names were chosen. For example, if there is an SSO, MDM, NAC, or other tool in use in the environment that has a gateway with a TLS/SSL cert, you may be able to glean that information based on the cert common names, which may also reveal the host names of those devices. With that in mind, reviewing what information you’re leaking about your own environment via certificates and sub-domains could be a worthwhile use of time.
