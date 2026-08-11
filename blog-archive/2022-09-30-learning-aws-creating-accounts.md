---
title: "Learning AWS #2: Creating Accounts"
date: 2022-09-30
author: Andy Lombardo
source: https://www.edtechirl.com/p/learning-aws-creating-accounts
---

# Learning AWS #2: Creating Accounts

[![](https://images.unsplash.com/photo-1632594737623-bea601083890?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHw0fHxiZWdpbm5pbmd8ZW58MHx8fHwxNjY0NTA5NzA0&ixlib=rb-1.2.1&q=80&w=1080)](https://images.unsplash.com/photo-1632594737623-bea601083890?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHw0fHxiZWdpbm5pbmd8ZW58MHx8fHwxNjY0NTA5NzA0&ixlib=rb-1.2.1&q=80&w=1080)

Photo by [Maxime Horlaville](https://unsplash.com/@mxhpics) on [Unsplash](https://unsplash.com)

I’ve played in AWS before and used it for solving some very specific, small, niche problems. Now it’s time to start buckling down and learning for real.

**Setting the Stage**

To lay the foundation for my first project, I need to create accounts for what I’m lovingly calling Project 1. Part of this project will be utilizing AWS organizations to coordinate a single project amongst various accounts, so we’ll be creating 2 root accounts - A general account and a production account. Each of these root accounts will also have at least one IAM user account created, and the IAM accounts are the accounts I’ll be using to work on the project. We’ll be using IAM accounts because just like administering a computer, it’s not a good idea in AWS to work from the root account. Since we will be using an IAM account with admin rights, we won’t necessarily be adhering to the principle of least privilege here, but this gives us the infrastructure we need to be able to employ least privilege.

**Account Creation Tips**

To create a new root AWS account, you need to sign up with a unique email address. To keep from juggling tons of mailboxes, you can use a mail feature called Dynamic Alias that’s built into a lot of mail clients (Gmail, Outlook, iCloud for sure). To use dynamic aliases, you use your regular email address and use a + sign to concatenate extra info to the leading part of your address. For example, for my production account for Project 1, I used the address andy+Project1prod@edtechirl.com as the unique email address in Amazon. Because I use a mail host that supports dynamic aliases, that message goes to my regular andy@edtechirl.com inbox. With a bunch of accounts, though, that can make your inbox messy really quickly. To clean it up, I have a mail flow rule in my mailbox that redirects any messages sent to my AWS dynamic aliases to an AWS folder, so it doesn’t glut my inbox.

Creating AWS accounts also requires a credit card. The card does not have to be unique, however, so you can use the same card for all of the accounts. I’m super paranoid about crazy AWS billing if I turn something on and forget about it, so that makes me a little nervous. We ARE going to set up budgets at a later step, but something else I do is use a more disposable card that’s not directly tied to my bank account. AWS won’t let you use prepaid cards, but I use a Cash App card. That way if there is billing craziness, it won’t hit my primary bank account. My bank doesn’t support using Privacy.com so I’m not sure if Amazon will accept privacy.com cards with AWS, but if they do that would be a great option.

**Securing Accounts**

After creating the 2 root accounts, the next setup step is securing them. Since root account access can delete your AWS account, I set up MFA right off the bat. In my case, I’m using a virtual MFA token in a cell phone app. Once MFA was configured, I went to the account settings page for each account and activated IAM User and Role Access to Billing Information to help with later steps.

After creating the root accounts, I created an IAM Admin user for both accounts. When creating the IAM user through the AWS IAM console, for the purposes of Project 1 I assigned the IAM user the Administrator Access policy. This gives all the same features as the root user with a [few exceptions](https://docs.aws.amazon.com/accounts/latest/reference/root-user-tasks.html), most notably the ability to close the account.

**End result:**

At this point, I have 2 AWS accounts:

Project 1 General Root User

Project 1 Production Root User

**Each of these 2 accounts have a an IAM account associated with it:**

Project 1 General IAM Administrator

Project 1 Production IAM Administrator

**All 4 of these accounts have MFA enabled.**

At this point, the challenge seems to be managing accounts.

To sort this out, I signed into the two IAM accounts and replaced their random 12 digit prefix with a recognizable alias. This makes it so that it’s easy to see which account the IAM login page is connected to. I then made browser bookmarks, and threw all 4 account usernames, passwords, and login URLs into my password manager.

**What’s next?**

On tap next is setting up access keys for the IAM accounts and setting up the AWS CLI tools to be able to programmatically interact with the IAM accounts.
