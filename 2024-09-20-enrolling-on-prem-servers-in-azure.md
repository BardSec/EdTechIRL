---
title: "Enrolling On-Prem Servers in Azure Arc"
subtitle: "Getting Started on the Path of Remotely Managing On-Prem Resources in Azure"
date: 2024-09-20
author: Andy Lombardo
source: https://www.edtechirl.com/p/enrolling-on-prem-servers-in-azure
---

# Enrolling On-Prem Servers in Azure Arc

*Getting Started on the Path of Remotely Managing On-Prem Resources in Azure*

[![](https://substackcdn.com/image/fetch/$s_!Na74!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98871a54-e75d-4f06-b968-ae69ca4d4f44_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!Na74!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98871a54-e75d-4f06-b968-ae69ca4d4f44_1024x1024.webp)

If you manage servers on-premises but have shifted to a cloud-centric state of mind, Azure Arc is worth looking into. Arc is a hybrid and/or multi-cloud management solution that lets you manage resources like servers in a single control plane within Azure. In short, it makes it so you can cloud-manage on-prem servers as if they were a machine hosted in Azure. The primary thing I use this for is automating Windows patching on my fleet of servers, but there are a lot of other applications that we’ll explore later.

Getting set up will involve installing a connector agent on each Windows or Linux server that you want to manage in the cloud. This can be done onsie-twosie, or you can deploy an onboarding script. We’ll discuss both options below.

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.

### Finding the Right Place to Start

Go to the Azure Arc blade on your Azure portal by going to [Azure.cmd.ms](https://azure.cmd.ms) —> Azure Arc —> Azure Arc Resources —> Machines. Or, you can get there directly from [azhybridcompute.cmd.ms](http://azhybridcompute.cmd.ms).

Next, click on **+Add/Create** and select **Add a machine**.

[![](https://substackcdn.com/image/fetch/$s_!GCaE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2101e219-b949-416d-a174-8c9098e47562_379x296.png)](https://substackcdn.com/image/fetch/$s_!GCaE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2101e219-b949-416d-a174-8c9098e47562_379x296.png)

You will now have choices:

[![](https://substackcdn.com/image/fetch/$s_!n40R!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F345a1355-d666-4b1a-8a26-85d551255232_1507x711.png)](https://substackcdn.com/image/fetch/$s_!n40R!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F345a1355-d666-4b1a-8a26-85d551255232_1507x711.png)

The three options we’ll look at are the first three presented:

- Add a single server
- Add Windows Server with installer
- Add multiple servers

### Add A Single Server

#### Generate an Installation Script

This is my preferred method for one-off Arc installs, and for just giving it a test drive. Select this option, and it will walk you through a wizard like this:

[![](https://substackcdn.com/image/fetch/$s_!A8Rw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3732d7d-febd-41eb-8b90-5a942113fcb0_854x1044.png)](https://substackcdn.com/image/fetch/$s_!A8Rw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3732d7d-febd-41eb-8b90-5a942113fcb0_854x1044.png)

1. Select which Azure subscription you want to add it to. If you don’t have any Azure subscriptions, you’ll need to create one by going to the Azure portal ([azure.cmd.ms](https://azure.cmd.ms)) and search for Subscriptions. On the Subscription page click on **+Add** and create a subscription. When deciding what subscription to create, think of a subscription as a billing source. Anything I want to come from a specific organization, department, or account, I put into its own subscription.
2. Select a Resource group. If you don’t have any resource groups, you can click on **Create new**. For my resource group, I sort things based on project, so I just went with AzureArc, and I’ll use this resource group for anything AzureArc adjacent.
3. Select the Region closest to you.
4. Select the operating system — Windows or Linux. The examples below are assume we’re doing Windows Server, but the scripting processes will create Bash scripts for Linux as opposed to the PowerShell scripts generated for Windows.
5. Unless you have specialized requirements, you can leave the defaults for SQL Server and Public Endpoint as they are.
6. Click on **Download and run script**. It will bring up this screen:

[![](https://substackcdn.com/image/fetch/$s_!Ofi7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43641dc0-3fa3-406c-9181-9cd051692126_820x828.png)](https://substackcdn.com/image/fetch/$s_!Ofi7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43641dc0-3fa3-406c-9181-9cd051692126_820x828.png)

From here, you can download or copy the PowerShell script.

To run this script, save it on the server you want to enroll in Azure Arc and Run As Administrator. If you don’t run it as Administrator, it will kick back with an error message.

#### Add Windows Server with Installer

If you’re onboarding Linux servers this option won’t work, but you can onboard Windows Servers by running an EXE file as admin. To get the executable, go back to the **Add a machine** screen and select **Download installer**. It should look something like this:

[![](https://substackcdn.com/image/fetch/$s_!pbyK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2b8dd72-1265-4dec-a6b9-06c70c29e1c0_126x26.png)](https://substackcdn.com/image/fetch/$s_!pbyK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2b8dd72-1265-4dec-a6b9-06c70c29e1c0_126x26.png)

Right-click on it and select Run As Administrator (or select it and hit ctrl+shift+enter).

You may be prompted with a warning about an untrusted file. Since you just downloaded this directly from Microsoft, it’s ok to say ok and proceed. You should get an install progress bar for a moment, then when the installer launches, you click Next through this screen

[![](https://substackcdn.com/image/fetch/$s_!4dAr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11a44179-d99b-4adf-8378-4ed0de986488_743x557.png)](https://substackcdn.com/image/fetch/$s_!4dAr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F11a44179-d99b-4adf-8378-4ed0de986488_743x557.png)

Then, you’ll sign in to Azure by clicking on the **Sign in to Azure** button. Once signed in, click **Next**

[![](https://substackcdn.com/image/fetch/$s_!UfZo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b3063ba-83fe-47c2-ba9d-fdbb696ff6af_744x551.png)](https://substackcdn.com/image/fetch/$s_!UfZo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b3063ba-83fe-47c2-ba9d-fdbb696ff6af_744x551.png)

On the next screen, select your Azure Tenant, choose a Subscription and Resource Group like in the Script example above, and select the region you are physically closest to, then click Next.

[![](https://substackcdn.com/image/fetch/$s_!BDQt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dc91e2d-8524-4b94-9409-3f6aef307a53_726x538.png)](https://substackcdn.com/image/fetch/$s_!BDQt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1dc91e2d-8524-4b94-9409-3f6aef307a53_726x538.png)

When finished, you should see a confirmation like below:

[![](https://substackcdn.com/image/fetch/$s_!XRqA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1da5ec0-e0db-481c-b99a-7e20c65138d8_730x540.png)](https://substackcdn.com/image/fetch/$s_!XRqA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff1da5ec0-e0db-481c-b99a-7e20c65138d8_730x540.png)

### Power User: Onboard All the Servers

If you’re onboarding many servers, it speeds up the process to use a Service Principal for authentication inside the script. To do this, go back to the main **Add a machine** screen and select **Add multiple servers:**

[![](https://substackcdn.com/image/fetch/$s_!00rr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b2f12dd-d418-409b-bc3d-c2ed73280658_1531x752.png)](https://substackcdn.com/image/fetch/$s_!00rr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1b2f12dd-d418-409b-bc3d-c2ed73280658_1531x752.png)

The initial choices are EXACTLY like creating a script for a single server:

[![](https://substackcdn.com/image/fetch/$s_!6YQc!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F179543e8-c6b9-4017-a798-a43e378136d1_822x960.png)](https://substackcdn.com/image/fetch/$s_!6YQc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F179543e8-c6b9-4017-a798-a43e378136d1_822x960.png)

But once you scroll down, the power comes in the **Authentication** section:

[![](https://substackcdn.com/image/fetch/$s_!LlMz!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb5172f5-7c8c-4a6d-8031-47695610971c_807x221.png)](https://substackcdn.com/image/fetch/$s_!LlMz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb5172f5-7c8c-4a6d-8031-47695610971c_807x221.png)

You can select an existing Service principal, but most likely you will want to click **Create new** and make one just for this project. You’ll want to give it a name (1), description (2), expiration (3), select a role (4)… for our purposes, we’re going to select Azure Connected Machine Onboarding, and click **Create** (5).

It will look like this:

[![](https://substackcdn.com/image/fetch/$s_!bUHF!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d41697a-8baf-4da3-af1c-dcd4790ae34c_576x991.png)](https://substackcdn.com/image/fetch/$s_!bUHF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0d41697a-8baf-4da3-af1c-dcd4790ae34c_576x991.png)

After it’s created, you’ll see a dialog box pop up that has a download button and lists the expiration date for your service principal client secret.

[![](https://substackcdn.com/image/fetch/$s_!x04T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d8922cb-dc69-40ac-9bb1-3adeff440233_445x241.png)](https://substackcdn.com/image/fetch/$s_!x04T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d8922cb-dc69-40ac-9bb1-3adeff440233_445x241.png)

Click Download and close, and it will download the **servicePrincipal.txt** file that contains your Principal ID and Client Secret. Be sure to do this, because you won’t have another opportunity to capture this information. Safeguard this, and it is a form of administrative credentials. This is also why it’s important to have an expiration date, and why you should target the scope of this Service Principal only to the specific Resource Group you’re working with.

Now, back on the **Add multiple servers with Azure Arc** page, the newly created Service Principal should show up in the drop down menu:

[![](https://substackcdn.com/image/fetch/$s_!c1HS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6187517f-2d1a-4997-a600-8c6b6c10af04_807x210.png)](https://substackcdn.com/image/fetch/$s_!c1HS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6187517f-2d1a-4997-a600-8c6b6c10af04_807x210.png)

Once that’s select, click **Download and run script.**

Now you’re presented with a deployment choice. We’re going to select **Basic script**, but you can use any of the deployment methods that apply to your environment. Next, click the **Download** button.

[![](https://substackcdn.com/image/fetch/$s_!NEgT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2338e7d-3d64-4093-ab25-8f1a8ef094cb_658x922.png)](https://substackcdn.com/image/fetch/$s_!NEgT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd2338e7d-3d64-4093-ab25-8f1a8ef094cb_658x922.png)

At this point, you’re ALMOST there but there’s a critical step to do after downloading the script. Open the script in an editor like Notepad or PowerShell ISE. There is a line for **$ServicePrincipalClientSecret=”<ENTER SECRET HERE>”;**

You need to edit that line and include the secret you downloaded in the servicePrincipal.txt file a few moments ago. The edits line should look something like this:

**$ServicePrincipalClientSecret=”zx.8Q<more seemingly random characters>xvc0H”;**

After making that edit, save the script and it’s ready to deploy to the server type you specified. Like before, be careful where this script is visible, because you don’t want the ServicePrincipal ID and Secret floating around in cleartext for everyone to see. That’s why I go with the 1 day expiration.

### What Should the End Result Look Like?

After successfully onboarding a server using one of the methods above, you should be able to go to the Azure Arc —> Machines page and see your machines listed.

[![](https://substackcdn.com/image/fetch/$s_!zpoD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F364f04c2-65b1-4d2c-b55d-4b15e22b0486_1812x804.png)](https://substackcdn.com/image/fetch/$s_!zpoD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F364f04c2-65b1-4d2c-b55d-4b15e22b0486_1812x804.png)

### What Can You Do with This?

Now this is where the fun starts. Next time, we’re going to look at using Azure Update Manager to automate Windows Server Updates for Azure Arc enabled servers. We’ll also look at how to create remote RDP and SSH sessions to onboarded devices. There are also possibilities for managing the device in Windows Admin Center, Change Tracking, event log viewing, and MUCH more.

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.
