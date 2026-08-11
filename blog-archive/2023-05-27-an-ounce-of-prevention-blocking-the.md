---
title: "An Ounce of Prevention: Blocking the new .zip and .mov Top-Level Domains"
date: 2023-05-27
author: Andy Lombardo
source: https://www.edtechirl.com/p/an-ounce-of-prevention-blocking-the
---

# An Ounce of Prevention: Blocking the new .zip and .mov Top-Level Domains

[![](https://substackcdn.com/image/fetch/$s_!LnFh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7383242c-1737-44c0-93b5-a58fbe723b12_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!LnFh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7383242c-1737-44c0-93b5-a58fbe723b12_1024x1024.png)

Earlier this month, Google made the .zip and .mov top-level domains (TLDs) publicly available for purchase.

**Why is this a bad idea?**

In general, files with the .zip and .mov extension are super common and are frequently downloaded. Most people won’t think twice about downloading an attachment in an email called hrdocuments.zip or onboardingvideo.mov (which is a problem in its own right). Crafty attackers know this, and it’s only a matter of time until you start seeing messages with phishing links like hrdocuments.zip or onboadingvideo.mov. Take it a step further, and since it’s only $15 to register one of these domains, it wouldn’t be hard for someone to register yourcompany-documentstoreview.zip or something similarly benign-looking but highly personalized.

[![](https://substackcdn.com/image/fetch/$s_!q6QO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb89dfbf3-c1c7-4954-856e-509a82c1f516_1688x690.png)](https://substackcdn.com/image/fetch/$s_!q6QO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb89dfbf3-c1c7-4954-856e-509a82c1f516_1688x690.png)

In addition to links in phishing emails, these malicious .zip and .mov domains are going to show up online, in forums, tweets, and anywhere else you can see linked content. Where this is going to cause even more unpredictable problems in the long run has to do with how programs detect and auto-link content. For example, say you sent a legitimate email to your users that said something like “Be sure to go to your share drive and download the financialstatement.zip” file. If your email program auto-links to website addresses, you may be sending your users an email with a link to the external [financialstatement.zip](https://financialstatement.zip/) website (go ahead and click the link for some additional context on this problem).

**What can you do?**

Aside from education and encouraging vigilance before clicking, I suggest explicitly blocking these domains in your content filter and/or email gateway. It’s possible that at some point someone will send you to a .zip or .mov with a legitimate purpose, but currently the risk outweighs the reward. Explicitly blocking these TLDs is a quick and easy way to add an additional layer of security that will cost you $0.
