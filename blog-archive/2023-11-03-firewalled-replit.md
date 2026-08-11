---
title: "Firewalled Replit"
subtitle: "Winning a Round of the Content Filter Whack-a-Mole Game"
date: 2023-11-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/firewalled-replit
---

# Firewalled Replit

*Winning a Round of the Content Filter Whack-a-Mole Game*

[![Replit: The software creation platform. IDE, AI, and Deployments - Replit](https://substackcdn.com/image/fetch/$s_!U6Wb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F895b8eed-9d7b-4ac6-9542-7edfbbf97d1f_1200x630.png "Replit: The software creation platform. IDE, AI, and Deployments - Replit")](https://substackcdn.com/image/fetch/$s_!U6Wb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F895b8eed-9d7b-4ac6-9542-7edfbbf97d1f_1200x630.png)

One of the least fun parts of managing devices for students is the Big Brother aspect of content filtering and striking the balance between technical controls and classroom management. A frequent flyer in this area is Replit. Replit is a robust cloud IDE for coding that offers free team accounts for educators. Think of a shared Google Sheet, but optimized for writing and sharing code.

However, Replit has a ton of game sites and proxies that are hosted by users with the goal of circumventing content filtering. Since I have computer science teachers in my district who use Replit, though, I can’t just block it outright even if I wanted to.

## **Enter Firewalled Replit**

Cognizant of these issues, Replit recently launched an option called Firewalled Replit that provides a more edu-friendly experience by still allowing coding and collaboration while walling off the Replit environment from the rest of the internet. Once your users are using Firewalled Replit instead of Replit, then replit.com and repl.co can be safely blocked in your filter while still allowing access to Replit.

## **How do you switch?**

This is probably the easiest tech migration I’ve ever been a part of. To make the change, simply go to [firewalledreplit.com](https://firewalledreplit.com) instead of replit.com. In my case, I updated the Replit link in our SSO to point to [firewalledreplit.com](https://firewalledreplit.com), and that was it. Existing user accounts and saved content are still accessible and usable. Both replit.com and firewalledreplit.com can exist in tandem as well, so you can stage the migration to make sure everyone is able to access Firewalled Replit before blocking the original domains.

## Allow and Deny

Once your students are pointed to Firewalled Replit and you want to start enforcing it’s use, add the following to your Deny List:

- \*.replit.com (primary domain)
- \*.repl.co (where web applications built on Replit are hosted)
- \*.repl.it (old domain, not actively used)
- \*.replitusercontent.com (old domain, not actively used)

Add the following to your Allow List if necessary:

- \*.firewalledreplit.com
- \*.firewalledreplit.co
- \*.cdn.replit.com

## Resources

[Firewalled Replit | Replit Docs](https://docs.replit.com/getting-started/firewalled-replit)
