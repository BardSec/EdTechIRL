---
title: "Instant DNS and Email Authentication Lookup for Any Site"
subtitle: "My second Chrome extension, RecordKeeper, lets you check DNS without opening a new tab"
date: 2026-02-09
author: Andy Lombardo
source: https://www.edtechirl.com/p/instant-dns-and-email-authentication
---

# Instant DNS and Email Authentication Lookup for Any Site

*My second Chrome extension, RecordKeeper, lets you check DNS without opening a new tab*

[![](https://substackcdn.com/image/fetch/$s_!QxXp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88dfef2a-6f45-4765-a73c-fb20385198f1_968x536.png)](https://substackcdn.com/image/fetch/$s_!QxXp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88dfef2a-6f45-4765-a73c-fb20385198f1_968x536.png)

I regularly find myself needing to check DNS records for whatever site I’m currently looking at. Sometimes it’s to sanity-check email authentication, sometimes it’s to confirm a nameserver change propagated, and sometimes it’s just basic curiosity. There are plenty of DNS lookup tools out there, but most of them require copying a domain, opening a new tab, pasting it into a form, and then digging through a wall of results. It’s not hard, but it *is* just enough friction to be annoying when you’re doing it often.

My solution? I built a small Chrome extension called **[RecordKeeper](https://chromewebstore.google.com/detail/recordkeeper/cdfnmlfpanmjnongcmjoeciifmhkcmek)** that lives right alongside my other tools. You click the icon and instantly see the DNS records for the current site—no tab switching, no copy/paste, no guessing which lookup tool you used last. I made email authentication records (SPF, DMARC, and DKIM) show up first, since that’s what I check most often, followed by the usual suspects: A and AAAA records, MX, TXT, NS, CNAME, and SOA. Everything is clearly labeled and includes TTL values.

Like TempPad, RecordKeeper is very much a one-job extension. It doesn’t try to manage domains or store history or track anything you do. It just queries DNS—securely, via Google’s DNS-over-HTTPS—and shows you the results. If you need to keep a snapshot, there’s an export button that saves all the records to a simple text file. Dark mode is included too, because staring at DNS records at night is already enough punishment.

RecordKeeper started as another scratch-my-own-itch project, but it’s quickly become one of those tools I instinctively reach for without thinking about it. It’s fast, lightweight, privacy-respecting, and disappears the moment you don’t need it anymore. If you ever find yourself repeatedly looking up DNS records “just to check one thing,” it might earn a spot in your browser too.

Chrome Web Store Link: <https://chromewebstore.google.com/detail/recordkeeper/cdfnmlfpanmjnongcmjoeciifmhkcmek>
