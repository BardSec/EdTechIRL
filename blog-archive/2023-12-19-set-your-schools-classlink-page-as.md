---
title: "Set your school's Classlink page as the default on your Intune iPads"
subtitle: "A quick tip that saves time and confusion!"
date: 2023-12-19
author: Andy Lombardo
source: https://www.edtechirl.com/p/set-your-schools-classlink-page-as
---

# Set your school's Classlink page as the default on your Intune iPads

*A quick tip that saves time and confusion!*

[![](https://substackcdn.com/image/fetch/$s_!Hmoy!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a79d36a-0141-4b19-b91c-bca43946b851_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!Hmoy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a79d36a-0141-4b19-b91c-bca43946b851_1024x1024.png)

### Introduction

This is meant to be a quick article with a handy tip for setting your school’s classlink sign in page as the default on the iPadOS/iOS app using Intune. This hasn’t been set on our iPads in the past and it causes confusion whenever students or staff need to search for your school’s sign in page before signing in.

[![](https://substackcdn.com/image/fetch/$s_!d3yR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40d4244f-dea9-4c14-836e-72b35db0cd9e_951x635.png)](https://substackcdn.com/image/fetch/$s_!d3yR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F40d4244f-dea9-4c14-836e-72b35db0cd9e_951x635.png)

### Setup

The way this works is by using an App Configuration Policy. To find this, go to **Apps > App Configuration Policies** in Intune.

For settings, you will want it to look like this.

[![](https://substackcdn.com/image/fetch/$s_!XFHj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89bb7c33-ac4c-43c7-862a-5f43b3236e42_362x418.png)](https://substackcdn.com/image/fetch/$s_!XFHj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89bb7c33-ac4c-43c7-862a-5f43b3236e42_362x418.png)

Note that you will need to add your school’s district ID as the string value.

`<dict>`

`<key>schoolDistrict</key>`

`<string>SchoolIDHere</string>`

`</dict>`

After the iPads pull the app and this policy, they will go straight to your school’s login page by default. Enjoy!
