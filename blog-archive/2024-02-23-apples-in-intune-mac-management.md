---
title: "Apples in Intune - Mac Management"
subtitle: "Exploring how far Intune has come for managing MacOS devices. The final part of my Apples in Intune series."
date: 2024-02-23
author: Andy Lombardo
source: https://www.edtechirl.com/p/apples-in-intune-mac-management
---

# Apples in Intune - Mac Management

*Exploring how far Intune has come for managing MacOS devices. The final part of my Apples in Intune series.*

[![](https://substackcdn.com/image/fetch/$s_!OrP5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff51259b5-8488-46c2-8cf4-562db7c48be9_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!OrP5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff51259b5-8488-46c2-8cf4-562db7c48be9_1024x1024.webp)

### Introduction

This article is to give a brief overview of my experience managing Mac devices in Intune for a school district.

Full Disclosure: we are primarily a windows district but do have a handful of users who use organizationally owned MacBooks and a computer lab full of Macs. I say this just to say that our needs differ a lot from what an “apple purist” school district would need. Also, Intune is continuing to add features that make this transition more worth it. If you’re reading this article in the future, a lot of my gripes may be fixed.

### Getting Started

To get your Macs in Intune, you will first need to enroll Intune as an MDM in apple school/business manager. There are lots of great articles and videos that cover how to do this. If you haven’t already, I also have an article that covers the process of Apple device management.

[Apples in Intune - Getting Started](https://www.edtechirl.com/p/apples-in-intune-getting-started)

### What does enrollment look like?

The biggest gripe I have with managing Macs in Intune is the enrollment process. Once you have the device assigned an enrollment profile and are setting up the device, the user will be prompted to create a local admin account. Microsoft has made this better with a new feature that will be coming out soon called Platform SSO. This will sync the local account created during the setup with a user’s Entra ID account, making sure their password for Entra ID is always set to the Mac’s local account. It also allows for SSO into Microsoft 365 applications on the device. A really cool feature, but it also requires enrollment once the device is setup and pulls the Company Portal app. Once you get the mac set up there, it’s really good.

However, this creates a new issue. What about shared device scenarios?

This is an issue we ran into with our Mac lab. The way we resolved this was by using a configuration profile in Intune to point to our local AD infrastructure for authentication. This works for a shared device scenario but requires hands-on from IT for the setup as they will need to make a local admin account and wait for it to pull that profile before other users are signed in.

The dream scenario will be when Platform SSO enrollment is simplified and if it ever gets to the point of allowing multiple users for shared device scenarios.

### How is managing?

Once you have your devices set up and ready to be distributed, the management side is actually really good. VPP Apps, DMG, and PKG programs can be easily pushed to devices. You can push shell scripts to devices for a lot of extra customization. The configuration profiles in Intune contain the vast majority of settings you would want to manage on end user devices, and other settings could be managed through custom Apple Profiles that can be imported in. Device actions such as remote locking, restarting the device, syncing, etc. are honestly more consistent and faster than they are often on Windows devices. Company portal allows for on-demand app installs (only for VPP apps at the moment, though PKG/DMG are to come) and easy device syncing.

Microsoft also has a lot of new features coming for mac that are very exciting. During the Microsoft Technical Takeoff, employees from Microsoft shared with us the following roadmap.

[![](https://substackcdn.com/image/fetch/$s_!tIFU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba8da52a-1099-45e2-b56e-5a766f27b399_2511x1273.png)](https://substackcdn.com/image/fetch/$s_!tIFU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fba8da52a-1099-45e2-b56e-5a766f27b399_2511x1273.png)

[Link to Video](https://www.youtube.com/watch?v=dviJhnCax-Q)

It has also been mentioned that Universal Print is coming to MacOS.  
[Link to Microsoft Roadmap Entry](https://www.microsoft.com/en-us/microsoft-365/roadmap?filters=&searchterms=124785)

### Conclusion

To me, MacOS devices in Intune isn’t a possibility for Apple Only organizations, but a very real solution for Windows Districts that are forced to have oddball macs. That being said, it seems obvious that Microsoft wants to improve their support for MacOS in Intune and are doing so rapidly. I imagine this conversation will be very different in a year or two time, as Microsoft continues to develop with MacOS in mind.
