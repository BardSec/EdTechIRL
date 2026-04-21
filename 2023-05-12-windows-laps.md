---
title: "Windows LAPS"
subtitle: "Managing the Built-in Admin Password with Intune and the new Windows LAPS"
date: 2023-05-12
author: Andy Lombardo
source: https://www.edtechirl.com/p/windows-laps
---

# Windows LAPS

*Managing the Built-in Admin Password with Intune and the new Windows LAPS*

[![](https://substackcdn.com/image/fetch/$s_!m_-D!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fac2229-b4d8-43cb-8a44-0d5adb039c11_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!m_-D!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8fac2229-b4d8-43cb-8a44-0d5adb039c11_1024x1024.png)

During the first year of our district’s 1:1 initiative back in 2014, we saw a good example of how persistent students can be when we found that a kiddo had removed a hard drive from their device, connected to their own computer, and used L0phtCrack to crack the local administrator password on the device. Since we were manually managing our devices, all of the local administrator passwords has been set by hand, and they were identical on all 3500 devices. The combination of reusing the password and having a simple enough password that could be hand-entered *en masse* was a double-whammy, and also incredibly hard to remediate with all of the deployed devices.

In the years since, we’ve lived and learned. With on-prem AD, Microsoft LAPS - short for Local Administrator Password Solution - was a solution for using Active Directory to automatically set unique local administrator passwords on devices, but in our transition to Azure AD, we’ve looked at third party solutions like [Cloud LAPS](https://msendpointmgr.com/cloudlaps/), but starting with the Windows update released on Patch Tuesday last month, Windows is including LAPS as a built-in part of Windows. With LAPS built-in, setting it up for Azure AD is a snap in Intune.

### **Setting up Windows LAPS with Intune**

1. Sign in to the [Intune Admin Center (intune.cmd.ms)](http://intune.cmd.ms) and navigate to **Endpoint Security** —> **Account Protection** —> **Create Policy**. On the **Create a profile** blade, choose **Windows 10 and later** for the Platform, and under **Account Protection** choose **Local admin password solution (Windows LAPS)** and click **Create.**

[![](https://substackcdn.com/image/fetch/$s_!l1au!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1407d60-3884-40e4-898c-7be2a6ee9f07_1920x892.png)](https://substackcdn.com/image/fetch/$s_!l1au!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1407d60-3884-40e4-898c-7be2a6ee9f07_1920x892.png)

2. Give the Profile a name and description and click Next

[![](https://substackcdn.com/image/fetch/$s_!lR_O!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F322f1642-db5d-4e58-9b2c-9f0440a07dfd_968x454.png)](https://substackcdn.com/image/fetch/$s_!lR_O!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F322f1642-db5d-4e58-9b2c-9f0440a07dfd_968x454.png)

3. Under Configuration Settings, select the configuration that makes the most sense for your environment. For an AAD/Intune environment, backing up the password to Azure AD makes the most sense. This Backup Directory refers to where the password will actually be managed and can be viewed from. The default for password rotation is 30 days, which is fine for me. For password complexity, I reference the [Hive Systems Password table](https://www.hivesystems.io/password)

   [![](https://substackcdn.com/image/fetch/$s_!OPI1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb45554a-6cec-43ad-986f-b416327471b7_939x612.png)](https://substackcdn.com/image/fetch/$s_!OPI1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb45554a-6cec-43ad-986f-b416327471b7_939x612.png)

   [![](https://substackcdn.com/image/fetch/$s_!s1wm!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6b39748-2820-471d-8919-f81c7b98adc2_532x531.png)](https://www.hivesystems.io/password)
4. Select a scope if appropriate
5. On the assignments tab, apply the LAPS policy to the group you want to manage local administrator passwords for. While there isn’t much that can go wrong that would need to be remediated, it’s always a good idea to test with a sample user or group first. After I was confident that everything worked as expected, I revised the policy to push to all devices. As LAPS is tied to the local administrator account for the machine, I definitely recommend using Device Groups as opposed to User Groups.

   Since the appropriate Windows update for LAPS was just released, the policy has only been successfully applying as devices pull the correct Windows update.

[![](https://substackcdn.com/image/fetch/$s_!3uCw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F108fe2a0-890e-4a04-bd11-8b9ad24ddc00_1107x517.png)](https://substackcdn.com/image/fetch/$s_!3uCw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F108fe2a0-890e-4a04-bd11-8b9ad24ddc00_1107x517.png)

6. Review and create policy.

   [![](https://substackcdn.com/image/fetch/$s_!MGx8!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65eaa894-ef4c-4275-b20b-be91a2a55076_867x785.png)](https://substackcdn.com/image/fetch/$s_!MGx8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65eaa894-ef4c-4275-b20b-be91a2a55076_867x785.png)

   ### Checking a Device’s Local Admin Password in LAPS

   Now that the Intune policy has pushed and the magic has happened, you can check a device’s local administrator password from Azure AD. From the AAD Manage —> Devices tab, select Local Administrator Password Recovery

   [![](https://substackcdn.com/image/fetch/$s_!Lkap!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9dabd90-0f04-4857-87be-055871f8f2a0_387x511.png)](https://substackcdn.com/image/fetch/$s_!Lkap!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9dabd90-0f04-4857-87be-055871f8f2a0_387x511.png)

From the Local Administrator Password Recovery screen, you can search for device.

[![](https://substackcdn.com/image/fetch/$s_!_XnR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192f2a1e-6677-44cf-9d32-87c8980b2650_1855x635.png)](https://substackcdn.com/image/fetch/$s_!_XnR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F192f2a1e-6677-44cf-9d32-87c8980b2650_1855x635.png)

Clicking the “Show local administrator password” link will bring up a blade like below where you can view the local admin password in clear text. You can also see when that password was set, and when its set for rotation.

[![](https://substackcdn.com/image/fetch/$s_!p7Pg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9528ee39-5df7-4355-bcc3-26cdcc6e5316_503x457.png)](https://substackcdn.com/image/fetch/$s_!p7Pg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9528ee39-5df7-4355-bcc3-26cdcc6e5316_503x457.png)

### Further Reading

[Manage Windows LAPS with Microsoft Intune policies | Microsoft Learn | https://learn.microsoft.com/en-us/mem/intune/protect/windows-laps-overview?source=recommendations](https://learn.microsoft.com/en-us/mem/intune/protect/windows-laps-overview?source=recommendations)
