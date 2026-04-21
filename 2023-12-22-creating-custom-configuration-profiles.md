---
title: "Creating custom configuration profiles for Apple Devices for Intune"
subtitle: "Gain access to settings that aren't built into Intune yet!"
date: 2023-12-22
author: Andy Lombardo
source: https://www.edtechirl.com/p/creating-custom-configuration-profiles
---

# Creating custom configuration profiles for Apple Devices for Intune

*Gain access to settings that aren't built into Intune yet!*

[![](https://substackcdn.com/image/fetch/$s_!r0Hs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d08890d-0f83-4d10-84ad-161beb69d430_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!r0Hs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d08890d-0f83-4d10-84ad-161beb69d430_1024x1024.png)

### Introduction

Though Intune has come a long way with apple device management, there is still quite a bit of work to be done. However, Microsoft did give us a way to bridge the gap while we wait for specific policies to be added into Intune, this being Custom profiles.

If you’re familiar with creating custom profiles for windows that target CSPs, this is a similar process. Apple devices can be managed by using a .mobileconfig file. These are effectively an XML file that allows you to configure settings on your apple devices. The inclusion of custom profiles in Intune allows for access to a lot of extra settings by uploading your own .mobileconfig files into intune to manage settings.

### Creating Custom Profiles

To create a custom profile, you will either need Apple Configurator 2 (if you’re wanting to build it on MacOS), or you can use [iMazing Profile Editor](https://imazing.com/profile-editor) (available on both MacOS and Windows). For this tutorial, I am going to show you the process using iMazing.

After you install the program and launch it, you will first need to give the profile a name in the **General** section. The general section is required for all profiles. You can also add more information on the profile on this page.

[![](https://substackcdn.com/image/fetch/$s_!kHGX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd689729d-0fb3-4304-a5d8-c2a6660458e1_1010x761.png)](https://substackcdn.com/image/fetch/$s_!kHGX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd689729d-0fb3-4304-a5d8-c2a6660458e1_1010x761.png)

Once you put in the name of the profile, you can scroll down the list of available configurations. There’s a lot of control in here, but almost to the point where it’s overwhelming. I would recommend filtering at the top for which OS you are planning on pushing this to and the searching for your profile through the profile types on the left side bar.

In this example, I am going to create a custom profile that adds a new font to an iPad. Currently, I believe this is not a functionality that is built into Intune, so we will be able to do it this way instead.

When I choose the **Font** profile from the side bar, it asked me to upload a font and to give it a name. Note that depending on what settings you are trying to configure, you will have different options to toggle.

[![](https://substackcdn.com/image/fetch/$s_!fN_B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6cbeb70-8847-4457-be89-6065e105005c_1010x761.png)](https://substackcdn.com/image/fetch/$s_!fN_B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6cbeb70-8847-4457-be89-6065e105005c_1010x761.png)

Then once you are done, you can choose **File > Save** at the top to save the .mobileconfig file to your computer.

[![](https://substackcdn.com/image/fetch/$s_!uRJb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe984f0b0-7499-47ad-91ed-f8bfdb1e442d_290x266.png)](https://substackcdn.com/image/fetch/$s_!uRJb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe984f0b0-7499-47ad-91ed-f8bfdb1e442d_290x266.png)

### Upload and Deploy!

Last step is to upload and deploy the profile to see if it worked! To do this, go to Intune then **Devices > iOS/iPadOS > Configuration Profiles > Create > New Policy > Profile Type: Templates > Custom**

You will have to give the Configuration Profile a name and then name it again before browsing for your .mobileconfig file. Once you select your .mobileconfig file, it will display the XML. Pretty cool huh?

[![](https://substackcdn.com/image/fetch/$s_!-_b_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76c95a42-37a9-4920-82d1-6da212600db8_801x690.png)](https://substackcdn.com/image/fetch/$s_!-_b_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F76c95a42-37a9-4920-82d1-6da212600db8_801x690.png)

After this, assign it to your test iPad or Mac device and wait to see if it reports back as a successful install before pushing it to other devices. To speed up the process, you can sync your device from Intune.
