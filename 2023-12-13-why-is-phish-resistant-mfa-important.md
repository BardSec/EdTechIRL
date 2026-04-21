---
title: "Why is Phish-Resistant MFA Important? or, How I Learned to Bypass MFA"
subtitle: "Not all MFA is created equal"
date: 2023-12-13
author: Andy Lombardo
source: https://www.edtechirl.com/p/why-is-phish-resistant-mfa-important
---

# Why is Phish-Resistant MFA Important? or, How I Learned to Bypass MFA

*Not all MFA is created equal*

[![](https://substackcdn.com/image/fetch/$s_!a6oA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd34315e-8d5f-4740-9200-4899f660df5a_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!a6oA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd34315e-8d5f-4740-9200-4899f660df5a_1024x1024.png)

One criticism of Multi-Factor Authentication (MFA) is that since it can be bypassed by attackers then it shouldn’t be trusted. While it’s true that there are MFA bypass attacks, MFA still provides an obstacle that gives an extra layer of protection between your users and the bad guys. However, just because some forms of MFA are vulnerable to attack doesn’t mean that all MFA is vulnerable.

## What does “Phish-Resistant MFA” mean?

Since the majority of account compromises come as a result of phishing attacks or other social engineering, Phish-Resistant MFA refers to types of MFA that are resistant to such attempts. That way, if you are bombarded by MFA requests on your authenticator app and you accidentally or prematurely complete the authentication, you’re OK. Similarly, if a phisher sends you a link in an email that steals your M365 session cookie, Phish-resistant MFA will keep you secure.

## Types of Phish-Resistant MFA

- Azure Certificate Based Authentication
- Windows Hello for Business
- FIDO2 Security Key

## How Easy is it to Phish MFA?

I’m glad you asked.

1. Set up a virtual Linux server using a service like Linode, Digital Ocean, Azure, AWS, etc.
2. Purchase a domain name that you can use for your phishing endeavors. Mine is pleasepleasedont.click ($3 a year from AWS). If you want to be particularly devious, choose a domain like 302a.zip. That way you can make super-phishy sub-domains like chrome\_update.11.4.302a.zip all day long.
3. Install and run EvilGinx on the Linux server. The steps for that are beyond the scope of this article, but can be found in abundance on YouTube and the interwebs in general. It took less than an hour for me to have an instance of EvilGinx up and running from the first time I heard of it to successfully phishing myself.
4. Send a malicious link and wait for someone to click.

## MFA Bypass Demo

The video below shows the steps involved in conducting an Adversary-in-the-Middle attack to capture a M365 tenant’s global admin session cookie that includes their MFA authentication using the Microsoft Authenticator app, and then replaying the session without having to complete MFA or crack a password hash.

[If you don’t see an embedded video above, you may need to allow content from this sender in your email client. The video can also be viewed on YouTube [here](https://youtu.be/LZQaIvVVc6A)]

While the video focuses on a phishlet for M365, custom phishlets can be crafted for additional sites, or downloaded from a variety of sources. This [github](https://github.com/An0nUD4Y/Evilginx2-Phishlets) has examples of the variety of phishlets that are openly available in categories like eCommerce (Amazon, eBay), Banking (Chase, CapitalOne), P2P Payments (PayPal, Venmo) and Social Media (Facebook, TikTok).

## How Do You Protect Yourself?

Phish-resistant MFA is, well, resistant to this type of AitM attack. In many cases, especially with Windows Hello for Business, phish-resistant MFA can actually lead to an improved end-user experience. If there is stakeholder pushback, though, control what you can control. If you can only implement this among IT admins or IT staff, start there. Conditional Access can be configured in M365 to require Phish-Resistant MFA for a variety of roles or apps. If you can expand the circle to key staff members, principals, finance staff, anyone with elevated privileges, etc., then every expanded circle is a win that hardens your environment a little bit more.

## Resources

- Overview of Microsoft Entra authentication strength - Microsoft Entra ID | Microsoft Learn <https://learn.microsoft.com/en-us/entra/identity/authentication/concept-authentication-strengths>
- Require phishing-resistant multifactor authentication for Microsoft Entra administrator roles - Microsoft Entra ID | Microsoft Learn <https://learn.microsoft.com/en-us/entra/identity/conditional-access/how-to-policy-phish-resistant-admin-mfa>
- Introduction to EvilGinx <https://help.evilginx.com/docs/intro>
- Implementing Phishing-Resistant MFA (cisa.gov) <https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf>
- Creating Additional Phishlet Templates in EvilGinx <https://help.evilginx.com/docs/guides/phishlets>
