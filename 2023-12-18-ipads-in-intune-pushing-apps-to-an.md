---
title: "Intune iPad Device Staging - Pushing Apps to an iPad before Assigning a User"
subtitle: "The hidden Intune iPad enrollment option that allows for Device Staging!"
date: 2023-12-18
author: Andy Lombardo
source: https://www.edtechirl.com/p/ipads-in-intune-pushing-apps-to-an
---

# Intune iPad Device Staging - Pushing Apps to an iPad before Assigning a User

*The hidden Intune iPad enrollment option that allows for Device Staging!*

[![](https://substackcdn.com/image/fetch/$s_!gpnc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f5e9aba-bb67-47d2-a1f9-a5bc4f02588f_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!gpnc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3f5e9aba-bb67-47d2-a1f9-a5bc4f02588f_1024x1024.png)

### Introduction

I wanted to write a quick article about an issue I have seen other people run into online and a solution I found in the Microsoft Documents on iPad enrollment that gives you a whole other option when enrolling your iPads.

This enrollment option allows you to set up the iPad without assigning a user, push apps to the device group that will install, then assign a user by signing them into company portal on the ipad, this will then install all user-based policies and apps.

### Enrollment Options

As far as enrollment options you have two main options.

**Enroll with user affinity**

**Enroll without user affinity**

To put it simply, enrolling with user affinity means that intune will assign a primary user to the iPad which then allows you to push policies and apps to the iPad based on the groups that user is in. In general, if possible, you will more than likely want to have user affinity because it gives you more options. Here is the issue I ran into with this. We want to get the iPads set up with some basic apps before assigning a user. You would think the correct way to do this would be to use the enroll with user affinity option, then choosing Company Portal as your authentication method. However, when you do it this way, the iPad will not pull apps that are assigned directly to the device, until a primary user is assigned by signing them into company portal.

The way I discovered is to actually enroll without user affinity, and then using an App Configuration Policy to assign the first user to sign into company portal as the device’s primary user.

### Enrollment Profile

As mentioned before, the enrollment profile you are needing is **Enroll without user affinity**. The other settings do not matter as much, but here is what I have set.

[![](https://substackcdn.com/image/fetch/$s_!rRGP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79b98d35-192e-4fbc-a43b-fab35d032c8a_542x498.png)](https://substackcdn.com/image/fetch/$s_!rRGP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79b98d35-192e-4fbc-a43b-fab35d032c8a_542x498.png)

To create an enrollment profile, this is located under **Devices > iOS/iPadOS > iOS/iPadOS Enrollment > Enrollment Program Tokens > (your enrollment token you have set up) > Profiles**

### Company Portal App Configuration Profile

Next, we will create an App Configuration Profile. This is found under **Apps > App Configuration Profiles.**

Here are the settings you will want to apply.

[![](https://substackcdn.com/image/fetch/$s_!UF5V!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa312e62b-402e-4f32-a4d0-194dc1ab8974_917x430.png)](https://substackcdn.com/image/fetch/$s_!UF5V!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa312e62b-402e-4f32-a4d0-194dc1ab8974_917x430.png)

`<dict>`

`<key>IntuneUDAUserlessDevice</key>`

`<string>{{SIGNEDDEVICEID}}</string>`

`</dict>`

I should note that when you push this policy, for some reason it shows up as an error when it applies, however as far as my testing goes, it works consistently on the devices I have applied it to.

### Last Steps

After this, you will need to create a dynamic group in Intune that will catch your iOS devices (either by the device’s OS or by it fitting a name scheme that is applied with the enrollment profile, or both). Once you have that, you can assign the Company Portal VPP app to your group along with any other apps that you want to be installed before a user is assigned to the device. Those apps will push to the device and once a user signs into Company Portal, they will be set as the primary user and any policies or apps that are assigned to that user will be applied to the device.

This is handy for me because I work in Education. We can assign basic apps to the iPads for students so they are ready and available on the first day of school, but once they sign into the iPad’s company portal app, we can then have different apps pushed based on grade level, class groups, etc. I hope it is also helpful for you!

[Microsoft documentation on this](https://learn.microsoft.com/en-us/mem/intune/apps/app-configuration-policies-use-ios#configure-the-company-portal-app-to-support-ios-and-ipados-devices-enrolled-with-automated-device-enrollment)
