---
title: "Learning AWS #3: Are you down with CMD?"
subtitle: "AWS CLI Tools"
date: 2022-10-02
author: Andy Lombardo
source: https://www.edtechirl.com/p/3-are-you-down-with-cmd
---

# Learning AWS #3: Are you down with CMD?

*AWS CLI Tools*

[![opened black laptop computer](https://images.unsplash.com/photo-1526925539332-aa3b66e35444?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHwyN3x8Y29kaW5nfGVufDB8fHx8MTY2NDUxMDA1NQ&ixlib=rb-1.2.1&q=80&w=1080 "opened black laptop computer")](https://images.unsplash.com/photo-1526925539332-aa3b66e35444?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHwyN3x8Y29kaW5nfGVufDB8fHx8MTY2NDUxMDA1NQ&ixlib=rb-1.2.1&q=80&w=1080)

Photo by [AltumCode](https://unsplash.com/@altumcode) on [Unsplash](https://unsplash.com)

To help manage all the accounts that are in play with Project 1, I’m going to be setting up my terminal to connect to AWS using the AWS CLI tools. Inside of the AWS CLI, I’ll be able to create profiles for all of my accounts, and I can add Access Keys to the profiles to save the account credentials.

**Installing AWS CLI**

My favorite install tool for Windows is Winget. If you’ve never used winget, it’s a package manager for Windows that’s been included as part of Windows 11 and recent iterations of Windows 10. To find out if you have winget, open PowerShell and run the command

> ```
> winget
> ```

If you get a message that the cmdlet isn’t found, you’ll need to install winget. To install winget, head to the Microsoft Store and download the “App Installer” app from Microsoft. Winget is included in the App Installer app.

Once winget is installed, run this command to install AWS CLI:

```
winget install -e --id Amazon.AWSCLI
```

The AWS CLI can also be installed for Mac using Homebrew of Linux using APT or Yum, or you can go directly to aws for installers at [AWS Command Line Interface (amazon.com)](https://aws.amazon.com/cli/)

**Creating and Downloading Access Keys**

To be able to interact with AWS programmatically through the command line, I needed to create and download access keys that can be loaded into the AWS CLI tool. To do this, I logged in to both the General IAM Admin account and the Production IAM Admin account I created previously.

[![](https://substackcdn.com/image/fetch/$s_!D_lU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F40ec014d-d92f-484d-9601-ac611f17a34c_726x880.png)](https://substackcdn.com/image/fetch/$s_!D_lU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F40ec014d-d92f-484d-9601-ac611f17a34c_726x880.png)

After logging in, I open the account settings and selected “Security Credentials” and scrolled down to “Access keys for CLI, SDK, & API access”:

[![](https://substackcdn.com/image/fetch/$s_!qsYF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f4f60c2-9023-4465-8651-795f95707b15_2132x592.png)](https://substackcdn.com/image/fetch/$s_!qsYF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9f4f60c2-9023-4465-8651-795f95707b15_2132x592.png)

After clicking “Create access key,” there is an option to view the access key or download the access key to a csv. Your key is made up of a Public Key and a Private Secret. This screen is the only time you have a chance to see the Private Secret, so it’s super important to make a record of your note at this time, otherwise you’ll have to deactivate it and create a new one. It’s also important to note that this key pair has access to your account, so it should be safeguarded. Don’t share it. I wouldn’t even print it or save it to a cloud service. I would copy it and put it in my password manager, and leave it there.

After creating the access key for the first account, rinse and repeat with any other accounts you’ll be using in the CLI. For me, that means I now have key pairs for both my general and production IAM accounts.

**Creating Account Profiles**

After installing access keys and installing the AWS CLI, setting up profiles is just a matter of a few commands:

For my iamadmin-general account:

```
aws configure --profile iamadmin-general
```

The AWS CLI tool will then prompt for the Access Key ID and Secret Access Key. After entering these, it will prompt for the region. For this project, I am using us-east-1. It will also ask for the “default output format.” The default is none, which is fine for my purposes. After setting up the iamadmin-general profile, repeat with iamadmin-production. Now we’re ready to work in AWS using these 2 accounts through the command line.
