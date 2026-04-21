---
title: "Creating a HoneyDoc with Email Notification (in less than 5 minutes)"
date: 2022-04-02
author: Andy Lombardo
source: https://www.edtechirl.com/p/creating-a-honeydoc-with-email-notification
---

# Creating a HoneyDoc with Email Notification (in less than 5 minutes)

Opinions on cyber deception are divided, but when you can implement something this fast that might give you advance notice that you have a problem, why wouldn't you do it? The use of deception through HoneyDocs is a way to get an early alert for when your defenses fail - or, in a K12 environment, when you have kiddos trying to traverse directories to see what they can find.

- Go to [canarytokens.org](https://www.canarytokens.org)
- Select your token – in this example, we’re going to create a Word document called Passwords.doc that will have a list of fake usernames and passwords… something that would be enticing for either an intruder or an insider who’s poking around a little more than they should.
- Enter the email address where you want to be notified and a reminder for which token has been triggered. If you’re doing a single token this isn’t such a big deal, but these are so easy you’ll probably end up deploying several different types of tokens in nooks and crannies across your network. Be specific enough that you can find it again. Take it from me - when I first tested this, I made one without any info about where I was putting it, and it’s now saved somewhere on the internet that gets a hit a couple times a month, and I have NO IDEA where it is.
- Click “Create my Canarytoken”

  [![](https://substackcdn.com/image/fetch/$s_!TnQP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff39cf225-cf00-4a88-8c0f-49fba9a8cb0f_624x374.png)](https://substackcdn.com/image/fetch/$s_!TnQP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ff39cf225-cf00-4a88-8c0f-49fba9a8cb0f_624x374.png)

- Next, download your HoneyDoc and place it somewhere – a network share, on your harddrive, in an email with a tempting subject line, etc.

  [![](https://substackcdn.com/image/fetch/$s_!nuqR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1f6585b0-f36d-4a4a-ab2f-64884ecad3e7_624x477.png)](https://substackcdn.com/image/fetch/$s_!nuqR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1f6585b0-f36d-4a4a-ab2f-64884ecad3e7_624x477.png)

Boom. That’s it. Once the file is opened, it will send an automated email to the account you entered in step 3. If you want to tweak the document and add fake usernames and pass, have at it.

[![](https://substackcdn.com/image/fetch/$s_!54xG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1bb0eef5-0ee1-4221-a584-b5d3659912bc_669x780.png)](https://substackcdn.com/image/fetch/$s_!54xG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F1bb0eef5-0ee1-4221-a584-b5d3659912bc_669x780.png)

Additional types of Canarytokens include tokens for alerts…

- when a specific URL is visited
- when a DNS hostname is requested
- when an email is sent to a specific address
- when an uploaded image is viewed
- when a PDF is opened
- when a Windows Folder is browsed in Windows Explorer
- LOTS more options…
