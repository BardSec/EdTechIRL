---
title: "Curated Software Deployments in the K12 Environment, using Intune."
subtitle: "Let's get granular with our grouping!!"
date: 2023-03-31
author: Andy Lombardo
source: https://www.edtechirl.com/p/curated-software-deployments-in-the
---

# Curated Software Deployments in the K12 Environment, using Intune.

*Let's get granular with our grouping!!*

[![](https://substackcdn.com/image/fetch/$s_!YhXZ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99874c88-ad5e-42ce-bfae-f47ffab28026_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!YhXZ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F99874c88-ad5e-42ce-bfae-f47ffab28026_1024x1024.png)

### Introduction

Device Administration can be very tricky in the K12 environment. When you consider the ranges of software you have to support for both students and staff, differing devices/OS’s, and terribly impractical software update cycles from state regulated lockdown browsers (you know who you are), K12 System Administrators have their hands full. In this article, I wanted to briefly go over what I call the ‘Intune Dream Scenario,’ and how my school district is planning to get there.

> **The Goal: We want reimaging a device to be incredibly simple and hands free. We want it to be so easy that we can hand a device to an end user that is on Windows Out-of-box experience, and all they need to do is sign in to receive software curated to that user based on their school, grade level, department, and the user type (staff or student), etc.**

### How do we accomplish this?

To make this magic happen, we will need to use a combination of resources.

- Windows AutoPilot
- Device Based Groups
- User Based Groups
- Extensible Attributes
- Data in our SIS

The idea being that we can create a device group that contains our basic software that every user will need (Microsoft 365, a web browser, Configuration Profiles and PS scripts to make the device behave the way it needs to, AppLocker policies to prevent the kids from playing Minecraft in class, etc.)

I see this as the basic way to use Intune and really most other MDMs. The great thing about Intune is that we can leverage User Groups as well to create groups full of users based on a certain criteria. Once we have this, we can assign software and configurations based on the groups the user is in. The tricky part about this is creating user groups based on a certain criteria.

In our first experience with this, we wanted to create individual user groups based on the school the user is housed at (for both staff and students). To do this, we used Classlink’s Roster Server to pull data from our Student Information System and write it back to our Local AD in the form of Extensible Attributes. After it is written back to AD, our Local AD server then syncs this information to Azure AD using the AAD connector. We are then able to create a group using dynamic rules that automatically adds all users from a particular school, based on that extensible attribute.

[![](https://substackcdn.com/image/fetch/$s_!Jr1X!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4b63c8e-18c7-4ef7-8be7-90434a189e89_1684x452.png)](https://substackcdn.com/image/fetch/$s_!Jr1X!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd4b63c8e-18c7-4ef7-8be7-90434a189e89_1684x452.png)

[![](https://substackcdn.com/image/fetch/$s_!Rfcz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0aceba8-568d-4bde-b110-38c3d699f899_1252x815.png)](https://substackcdn.com/image/fetch/$s_!Rfcz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0aceba8-568d-4bde-b110-38c3d699f899_1252x815.png)

Using this, we can create groups based on anything in our SIS. Some examples we have thought of that would be useful are Department codes, student grade level, class based groups, as long as the criteria exists in a field in your SIS, you should be able to make it an extensible attribute.

### Okay, so what do I do with these groups?

Now’s the good part. We push things to them! You can assign specific applications and configuration profiles to these groups. Instead of pushing everything to the device group bucket, we can assign things based on the user’s needs.

This way the SRO will get the camera software installed on their device based on their department code. The student can get a custom background that matches their school’s mascot and color scheme based on the school they’re at in the SIS. The central office gets the drivers for their desktop scanners preinstalled. Whatever best fits your school’s needs, the possibilities are truly endless.

For anything that doesn’t fit a particular criteria, or is more ‘one off situation’, we use the Company Portal Kiosk and make sure our staff/students have instructions and access to getting applications from here.

The best part about all of this is it will take place after an autopilot reset happens meaning the user gets the correct software and configurations, every time, with improved granularity and minimal interaction from the Technology Department.
