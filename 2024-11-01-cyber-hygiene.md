---
title: "Cyber Hygiene > $$$"
subtitle: "Stop Throwing Money at Cybersecurity Tools Until You’ve Mastered the Basics"
date: 2024-11-01
author: Andy Lombardo
source: https://www.edtechirl.com/p/cyber-hygiene
---

# Cyber Hygiene > $$$

*Stop Throwing Money at Cybersecurity Tools Until You’ve Mastered the Basics*

[![A brightly colored illustration of a network technician walking carefully on a tightrope high above, symbolizing the challenges and risks of maintaining cybersecurity. The technician is holding a laptop, wearing a safety harness, and carrying network cables. The background is a vibrant cityscape with abstract technology icons like locks, shields, and network nodes floating around, indicating a secure network environment. The scene is dynamic, with expressive details in the technician’s cautious steps and focused expression. Use vivid colors to create a lively, energetic feel.](https://substackcdn.com/image/fetch/$s_!F_Iq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa104e287-a5eb-474a-92d6-b0c2ed78b569_1024x1255.webp "A brightly colored illustration of a network technician walking carefully on a tightrope high above, symbolizing the challenges and risks of maintaining cybersecurity. The technician is holding a laptop, wearing a safety harness, and carrying network cables. The background is a vibrant cityscape with abstract technology icons like locks, shields, and network nodes floating around, indicating a secure network environment. The scene is dynamic, with expressive details in the technician’s cautious steps and focused expression. Use vivid colors to create a lively, energetic feel.")](https://substackcdn.com/image/fetch/$s_!F_Iq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa104e287-a5eb-474a-92d6-b0c2ed78b569_1024x1255.webp)

It’s no secret that cybersecurity vendors have a solution/buzzword/acronym for just about everything. Whether it’s EDR, XDR, SIEM, SOAR, NGFW, or, <gasp> AI, there’s no shortage of expensive tools designed to keep the bad guys out. But here’s the thing: if your organization isn’t already practicing basic cyber hygiene, then all these advanced tools are like polishing the brass on the Titanic.

## The Foundation

Before diving into high-priced tools, let's talk about the essentials—the basics that often get ignored in the excitement over the next-gen solutions. Here are some must-do, low-cost steps that lay the foundation for any effective cybersecurity posture:

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.

### **Principle of Least Privilege**

One of the most effective and overlooked security measures is simply giving users and systems the minimum access necessary to do their jobs. The Principle of Least Privilege means restricting access rights so that each user, device, and system only has the permissions absolutely necessary for their tasks. This drastically reduces the risk of insider threats and minimizes the potential damage from a compromised account. For instance, if a user only needs read access to a file, they shouldn’t have write or delete permissions. Implementing least privilege is generally free but does require thoughtful configuration and monitoring. Once it’s in place, however, you’ll notice fewer security incidents and a safer, more controlled environment overall.

### **Just-in-Time (JIT) Access**

Building on the concept of Least Privilege, Just-in-Time (JIT) access limits access privileges to only when they’re needed. Instead of giving permanent permissions to users or systems, JIT access provides temporary access based on specific tasks or time frames. For example, instead of granting a user full admin rights indefinitely, they’d only receive those permissions when a job requires it—and only for a set time. This significantly reduces the risk of unauthorized access or abuse, as sensitive permissions automatically expire when they’re no longer necessary. JIT access can often be achieved using built-in settings or free tools, like Privileged Access Managment in Google or Privileged Access Management/Privileged Identity Management in M365, making it an essential, low-cost approach to enhancing security without investing in high-cost solutions.

### Strong Password Policies and MFA

Long gone are the days when “P@$$w0rd” was a secure password. Implement strong password policies across your organization and enable multi-factor authentication (MFA) wherever possible. MFA is often free with most services, and it drastically reduces unauthorized access. To take this up a notch, consider deploying Phish-Resistant MFA to IT staff and/or critical staff or staff with high-level access. MFA Bypass attacks are real \*and easy\* to pull off, [as documented in this previous article,](https://www.edtechirl.com/p/why-is-phish-resistant-mfa-important?utm_source=publication-search) but can easily be prevented by implementing passkeys or a hardware token like the [Yubikey](https://www.edtechirl.com/p/setting-up-fido2-yubikey-auth-for).

### Patching and Updating Regularly

Sounds too easy, right? But regular patching closes many vulnerabilities attackers love to exploit. Set up a routine schedule to update systems and software. You can leverage tools you may already have for device management to automate update policies using a Mobile Device Management platform if you already have one (Intune, Filewave, Jamf, etc.). If you’re in Intune, there are already Update Ring features to be configured, plus Windows Autopatch. If you’re managing on-prem servers in Azure Arc, you can set up automatic patching for $5/server/month. If you are in an Active Directory environment and don’t want to fight WSUS, then PDQ Inventory and Deploy is a very inexpensive and crazy good platform for managing on-prem devices, including pushing updates. There are a ton of freemium services that provide patching, but most of these tools are only free for 25, 50, or 100 devices. If you don’t have any existing tools and don’t have a budget for patching, prioritize your resources and at least add automated patching to critical systems. When you can’t hit perfection, shoot for progress.

### Backups and Disaster Recovery Planning

A good backup solution isn’t just a defense against accidental deletions; it’s your best friend in a ransomware attack. Make sure your backups are off-network or at least encrypted. I was scared off from getting this working well for a while because Veeam is the main name in the space, but it has a reputation for being expensive. As another option, I’ve had exceptional luck with Hornet Security VM Backup. From a pricing perspective, you can pay for the product as a service, or you can purchase a perpetual license based on the number of hosts you have. For example, if you have 2 virtualization hosts that are running 50 virtual machines, you would have an upfront one-time cost of about $1500, then an annual support and software assurance fee of about $600 (note this pricing is possibly out of date, but they also offer a 15% education discount). Pair this with the ability to use Hornet to send immutable backups to a cloud storage service like Wasabi, and your resilience will just keep going up. I was worried about pricing for cloud storage of backups, but in my environment, it only costs between $2-5/month per VM depending on backup frequency and retention schedules.

### Employee Training on Phishing and Social Engineering

Most breaches start with a human mistake. Make cybersecurity training part of the culture, not just an annual checkbox. Training doesn’t have to be expensive either! There are low-cost or free resources available, and even regular internal emails with tips can help keep your team informed. This has been an area primarily geared towards large enterprise environments, but over the past year a K12-centric vendor called [Cybernut](https://www.cybernut.ai) has popped up in this space. [I’ve gushed about them before](https://www.edtechirl.com/p/cybernut-phishing-simulation-and), but they’ve built a phishing simulation and security awareness training platform that is designed from the ground up to be gamified and non-punitive, turning simulations and training into positive learning opportunities. You can also add the referral code **edtechirl** for some extra-white glove attention during onboarding.

## When It’s Time to Start Investing

Once you’ve nailed the basics and have these foundational pieces running smoothly, then it might make sense to look into more advanced solutions. At that point, each dollar you spend will build on a solid foundation, maximizing value and effectiveness.

So, what should you start considering?

### Endpoint Detection and Response (EDR)

Once your systems are patched, secure, and your team is trained, EDR can provide an extra layer by monitoring devices for suspicious activity. It’s powerful but pricey—so only get into this when you’ve tackled the essentials.

### Network Detection and Response (NDR)

For larger organizations, an NDR solution can be valuable. NDR watches the network for unusual patterns, which is useful in detecting threats that may bypass simpler protections. It’s a great addition after you have solid perimeter and network hygiene. This is an area where you can drop some serious cash, but there are also some affordable gems here, like [AC-Hunter from Active Countermeasures](https://www.activecountermeasures.com/ac-hunter/) (part of the Black Hills Infosec family). Best of all, there is a free community edition of AC-Hunter, so you can try before you buy, but then upgrade to paid if you hit the ceiling on what the CE is capable of.

### Security Information and Event Management (SIEM)

SIEM solutions aggregate and analyze data across your network, providing a comprehensive view of your security posture. But they require investment—not just in the tool, but also in staffing and expertise. For many, this is the last piece of the puzzle. If you want to see what a SIEM does, though, [Blumira offers a free SIEM solution for a handful of cloud environments](https://www.edtechirl.com/p/free-siem-for-microsoft-365), including Microsoft 365. I loved their free M365 product so much, I became a customer for their full SIEM product. They do not offer academic pricing per se, because edu isn’t really their sector. Your mileage may vary, but in my experience they were very willing to work with me on pricing beyond their normal pricing structure. If you go all in with SIEM, though, be prepared to invest in manpower to investigate alerts. Alert fatigue is real, and can derail SIEM implementations for small teams.

## You Don’t Need the “Next Big Thing” to Be Secure

Vendors are great at marketing, and sometimes we’re left feeling like we need every tool on the shelf. But the truth is, if you’re not already doing cyber hygiene right, adding expensive tools won’t close the gaps; it’ll just hide them. Start with the basics and get those locked down. And when you’re ready to add the next tool, make sure it’s something that really adds value.

Building good cybersecurity habits doesn’t have to be expensive, but it does need attention and commitment. Don’t be swayed by every shiny solution—your budget and your security will thank you.

## **Join the Conversation!**

What are your thoughts on balancing basic cyber hygiene with more advanced tools? Have you found simple, low-cost measures that made a big impact in your organization? Or are there “must-have” tools you think every team should consider? Share your experiences, challenges, and tips in the comments!

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.
