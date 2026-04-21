---
title: "Getting a list of last logged on users for an Intune Device"
subtitle: "Solving a common K-12 problem using the Microsoft Graph API!"
date: 2023-11-28
author: Andy Lombardo
source: https://www.edtechirl.com/p/getting-a-list-of-last-logged-on
---

# Getting a list of last logged on users for an Intune Device

*Solving a common K-12 problem using the Microsoft Graph API!*

[![](https://substackcdn.com/image/fetch/$s_!aCoP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f97b95d-3d70-473e-b358-cf99df1de181_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!aCoP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f97b95d-3d70-473e-b358-cf99df1de181_1024x1024.png)

### Introduction

About a month ago, I had a situation come up at our High School where a student placed their laptop down and another student picked it up and had taken it to their next class by mistake. This is a surprisingly common occurrence in the K-12 space. Every time this issue comes up, I let out a groan as there isn’t a great way to figure out who has the device from Intune. For some reason, Intune has it to where you can get login logs for a user and figure out which devices a user has logged into, but there isn’t an easy way to get a list of users that have logged into a specific device. Until now…

### The Script

I have created a script that leverages Microsoft Graph API to get a list of last logged on users on a given device along with time stamps. Pretty neat huh?

[![](https://substackcdn.com/image/fetch/$s_!01Xz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F399e2ec3-6cf6-41e9-989b-95c4163bbf05_1721x940.png)](https://substackcdn.com/image/fetch/$s_!01Xz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F399e2ec3-6cf6-41e9-989b-95c4163bbf05_1721x940.png)

The script can be found using the link below to my GitHub.

[GitHub - Intune-Device-User-Logins](https://github.com/bradywidener/Misc-Intune-Scripts/blob/main/Intune-Device-User-Logins.ps1)

Once you open the script, there are a couple of commands you will need to run to install the required modules that the script uses.

`Install-Module Microsoft.Graph.Beta.Devicemanagement`

`Install-Module Microsoft.Graph.Beta.Users`

Once they are installed and you run the script, it will ask you to authenticate to your Azure Tenant.

[![](https://substackcdn.com/image/fetch/$s_!b7VB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd674d622-14f5-4e6b-908f-3370b0550527_710x1005.png)](https://substackcdn.com/image/fetch/$s_!b7VB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd674d622-14f5-4e6b-908f-3370b0550527_710x1005.png)

After you sign in, you will be asked to give the device’s hostname. Once you type that in and hit enter, it will give you the data.

Another tool in the box!
