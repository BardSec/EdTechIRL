---
title: "Snipe IT and Azure: Asset Management Info in Intune!"
subtitle: "Using APIs to fill in asset details in Intune under the device's note section!"
date: 2023-11-25
author: Andy Lombardo
source: https://www.edtechirl.com/p/snipe-it-and-azure-asset-management
---

# Snipe IT and Azure: Asset Management Info in Intune!

*Using APIs to fill in asset details in Intune under the device's note section!*

[![](https://substackcdn.com/image/fetch/$s_!Owzb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32a0786b-7a20-4351-8b24-abe4b8305905_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!Owzb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F32a0786b-7a20-4351-8b24-abe4b8305905_1024x1024.png)

### Introduction

The script uses Microsoft Graph API and the Snipe IT API to query information from Snipe regarding the asset, and it feeds it back into Intune under the device’s notes. This article will show you how to set this up in your own organization. Currently, the script will writeback the Asset Tag, Status information, and the current checked out user from Snipe.

[![](https://substackcdn.com/image/fetch/$s_!GFsr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4281b609-c2dc-4e39-8266-2d7456a75910_844x773.png)](https://substackcdn.com/image/fetch/$s_!GFsr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4281b609-c2dc-4e39-8266-2d7456a75910_844x773.png)

### Pre-requisite

Outside of having to have accounts for both Snipe and Azure with privileges, the biggest pre-requisite is that you **must** have your device’s Serial Number field filled in for your devices in Snipe IT. This is how the script knows which asset in Snipe is the same as a device in Azure.

Also note, the way the script is now, this will remove any other notes that are made and overwrite them.

### Overview of how the script works

- The script pulls all devices from Azure.
- The script will then query each device it pulled from Azure by serial number and see if it exists in Snipe IT.
- If the device exists in Snipe IT, it will then query for additional information and set a variable equal to the information we desire.
- After this, it will then upload the information from Snipe to the notes field of the device in Azure, before moving to the next device.
- Devices that do not exist in Snipe will be given a message in the notes field saying it is not currently an Asset.

### Download the Script

First, we will need to download the script. I have it available on my GitHub.

[GitHub - SnipeIT-InfoImportToIntuneSample.ps1](https://github.com/bradywidener/Snipe-IT-Azure-Integration/blob/main/SnipeIT-InfoImportToIntuneSample.ps1)

After we create our APIs, we are going to fill in information from each at the top of our script.

[![](https://substackcdn.com/image/fetch/$s_!D0sK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41785dfc-adaa-455a-b0cf-d000327fe0bd_1412x225.png)](https://substackcdn.com/image/fetch/$s_!D0sK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F41785dfc-adaa-455a-b0cf-d000327fe0bd_1412x225.png)

### Creating the Snipe API

1. First, you will need to log into Snipe API and click on your profile in the top right, then **Manage API Keys**

   [![](https://substackcdn.com/image/fetch/$s_!QsfO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F870f302b-384c-4c83-9069-07c9b9ff1089_496x339.png)](https://substackcdn.com/image/fetch/$s_!QsfO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F870f302b-384c-4c83-9069-07c9b9ff1089_496x339.png)
2. Click **Create New Token**
3. Give it a name. As soon as you do, it will show you a long string. Copy this and keep it somewhere safe, after you close the window there is no way to view it again. You will also want to paste this in our script on line 2. The variable will look something like this after it is filled in. Note that Bearer must come before your token.

   **$SnipeToken = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1N…”**
4. Next, on the API Keys page in Snipe, it also has your base API URL in the right corner. We will want to copy this down on the next line. It will look something like this.  
   **$SnipeAPIBase = "https://domain.snipe-it.com/api/vi"**
5. After this we have the information we need from Snipe.

### Creating the Graph API App

1. First, go to the Azure AD Portal
2. Next, go to **App registrations** from the side bar.
3. Click **New registration** in the top left corner.
4. Here you will give it a name. Choose the first option for supported account types and use **Public client** with **http://localhost** for your Redirect URI

   [![](https://substackcdn.com/image/fetch/$s_!VloC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02bce071-54ab-4b3d-8d26-e83743cae038_1035x817.png)](https://substackcdn.com/image/fetch/$s_!VloC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02bce071-54ab-4b3d-8d26-e83743cae038_1035x817.png)
5. On the next screen, you will be able to get your Client ID and Tenant ID. Copy these values and paste them into the script on lines 6 and 8.

   [![](https://substackcdn.com/image/fetch/$s_!zBGD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98925201-2825-46c3-baee-b9a8cdb60ba3_1216x482.png)](https://substackcdn.com/image/fetch/$s_!zBGD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98925201-2825-46c3-baee-b9a8cdb60ba3_1216x482.png)
6. Next, go to **API Permissions** from the side bar. Click **Add permission > Microsoft Graph > Application Permissions > Click the DeviceManagementManagedDevices drop down and give it all 3 permissions.**

   [![](https://substackcdn.com/image/fetch/$s_!aDv1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe26d772b-beff-46e1-a28a-a83f4f988e73_757x244.png)](https://substackcdn.com/image/fetch/$s_!aDv1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe26d772b-beff-46e1-a28a-a83f4f988e73_757x244.png)
7. After this, click the **Grant admin consent for organization** button at the top of the API Permissions page.
8. Next, go to **Certificates & secrets** from the side bar. Click **New client secret**. Choose a name and an expiration for it.

   [![](https://substackcdn.com/image/fetch/$s_!OGEv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96213eee-16c9-41b0-a68d-dccefac5d1aa_703x172.png)](https://substackcdn.com/image/fetch/$s_!OGEv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96213eee-16c9-41b0-a68d-dccefac5d1aa_703x172.png)
9. Similar to the Snipe Token, after you create the secret, you will only be able to see its value once, on this page. Go ahead and copy the value of your secret and save it somewhere. We will also want to plug it into our script on line 7.

### Using the script

After this you are almost ready to use the script! One thing you will need to do is install the module that is imported at the top of the script. The command to do this is:

**Install-Module Microsoft.Graph.Beta.Devicemanagement**

Once you have this installed on the computer you wish to run it on, I would recommend letting it run on a few computers, then using **control + c** to cancel the script so you can check to make sure the notes field is updating in intune on the correct devices.

[![](https://substackcdn.com/image/fetch/$s_!T6bj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ccc5a76-d7cf-4f91-9122-f834756dc97b_482x451.png)](https://substackcdn.com/image/fetch/$s_!T6bj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9ccc5a76-d7cf-4f91-9122-f834756dc97b_482x451.png)

As the script goes, it lists the devices by serial that it has updated/processed. Once it finishes, it will give you the number of devices processed and the time it took to run.

[![](https://substackcdn.com/image/fetch/$s_!EzZ9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa80e3a4c-5644-4e30-9ed1-b81213835ce4_260x70.png)](https://substackcdn.com/image/fetch/$s_!EzZ9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa80e3a4c-5644-4e30-9ed1-b81213835ce4_260x70.png)

Long term, I would recommend putting this script on a computer and creating a scheduled task to kick off the script at the end of the workday. This way the notes field is kept up to date fairly consistently.

### Closing notes

I feel like I should note that this script may not be the best solution for every organization, but it does help mine a lot being able to see the devices checked out to a user from Intune so we can make sure our Primary users and Asset management are somewhat in sync. If you’re good with coding I highly recommend you take the script and make it work to your company’s needs. Snipe and Microsoft Graph both have some great documentation.

Next on my list is to create a user sync from Intune to Snipe to automatically create users. Stay tuned!
