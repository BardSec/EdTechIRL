---
title: "Apples in Intune: Reimagining our K-3 iPad Management"
subtitle: "Designing how we plan to manage class sets of iPads using Intune!"
date: 2023-12-20
author: Andy Lombardo
source: https://www.edtechirl.com/p/apples-in-intune-reimagining-our
---

# Apples in Intune: Reimagining our K-3 iPad Management

*Designing how we plan to manage class sets of iPads using Intune!*

[![](https://substackcdn.com/image/fetch/$s_!L2pU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00028e57-e82d-4cf7-bcf4-1581094fc6d0_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!L2pU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F00028e57-e82d-4cf7-bcf4-1581094fc6d0_1024x1024.png)

### Introduction

This article is meant to be an overview of what our iPad deployment process will be next school year when we switch over to using Intune for iPad management.

Currently we manage our devices in class sets at our K-3 schools, with each student having a designated iPad in the class set. This comes with a lot of unique challenges whenever it’s time to re-deploy devices. The biggest challenge here is actually rostering. Class schedules, especially in the lower grade levels, fluctuates a lot up to the week before school starts. This leaves tech staff having to scramble last second until they are able to finalize iPad numbers in each class set, and designate iPads to each student.

To summarize our overall goal, we want to find a process with Intune that allows us to continue to manage iPads in a class set, but leverage the benefits of having devices assigned per user in our MDM, and doing this in a way that works well with rostering… It’s a lofty goal, but we managed to find something that works for us.

### Overview of the model

- **Setup -** iPad is set up from the OOBE and pulls the enrollment profile (without user affinity).
- **Device Level Apps and Policies -** The iPad pulls all apps and policies assigned at the device level, including company portal.
- **Registering to a User** - The user signs into the iPad’s company portal app, making that account the primary user of the iPad.
- **User Level Apps and Policies -** The iPad then pulls apps and policies based on the primary user’s class group.

Let’s go over each of these steps of the process and what benefits this brings us.

### Setup

If you haven’t seen [my first article regarding apple devices in Intune](https://www.edtechirl.com/p/apples-in-intune-getting-started), I would recommend it as it gives a breakdown of the general process of managing apple devices in Intune.

As far as the Intune set up goes for our iPads, we are deploying devices without user affinity and then using an app configuration policy with the company portal app to assign the first user that signs in as the primary user in Intune. I have an overview of this process [in another article, if you are interested.](https://www.edtechirl.com/p/ipads-in-intune-pushing-apps-to-an)

### Device Level Apps and Policies

The big benefit of deploying your iPads with the setup process I mentioned before is that it allows you to ‘stage’ your devices, allowing them to pull all apps and policies that are pushed directly to the device and device group before assigning a user.

In our iPad group, we are pushing are basic policies that would go to every iPad, along with apps our staple educational apps that are also often needed day one. This includes our SSO app of choice, state assessment software, district/state regulated instructional software, and policies to manage and lock down the iPad.

Once the iPad finishes pulling these things, it will go in the ‘finished pile’ until we are closer to the start of school.

### Registering to a User

Once rosters at the school level are finalized, we can then have the teachers sign the students into their class set of iPads, in the Company Portal app. When they do this, this will assign the student as the primary user on the iPad.

### User Level Apps and Policies

Once the user is assigned to the iPad, it will pull user-based policies and apps. For this to happen, you’ll need to have your users in groups, preferably having your homeroom classes as groups in Intune.

The way we have this set up is by using Microsoft School Data Sync to create groups for each of our classes from our Student Information System.

Then we create a separate dynamic group in Intune that we will use to assign our policies and apps to that has the same student accounts as the group from school sync. The dynamic rule for this group will simply put all users from the MS School Data Sync group into our new group. The reason we do this as a separate group instead of assigning apps and policies directly to the homeroom group made by School Data Sync is so that way, we don’t have to recreate assignments each year.

The rule for the dynamic group looks like this. Note that you will need to replace **value** with the object ID of the homeroom group.

[![](https://substackcdn.com/image/fetch/$s_!uskd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feeba31f0-2278-4cfc-809f-03e24ba64bfb_841x552.png)](https://substackcdn.com/image/fetch/$s_!uskd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feeba31f0-2278-4cfc-809f-03e24ba64bfb_841x552.png)

`user.memberof -any (group.objectId -in ['value'])`

The only thing I do not like about this method is that tech staff will need to edit these groups each summer to point to the new homeroom group, but I think this is a fair and doable trade off.

After the iPad is assigned a primary user and it picks up that the primary user is in one of these ‘class’ groups, it pulls the apps and policies that are assigned to it. In testing, it can take the iPads up to a half hour to get the user-based assignments after the user is assigned, but this can be sped up but manually syncing the iPad and is still allows for teachers to have everything on the device before the first day of school.

### Closing Notes

Though this may not work for everyone, but for us, this is already shaping up to be a huge improvement for how we manage iPads. I am excited to continue improving our iPad management using Intune, and excited to see what changes Microsoft continues to release for iPadOS and iOS. There are lots of other features that Microsoft has added that I didn’t even touch on in this article, including the Entra SSO extension for automatic sign ins to Microsoft apps and websites, custom profiles that can be made and imported into Intune, and many others. I highly recommend you give Intune a try for iPad management!

###
