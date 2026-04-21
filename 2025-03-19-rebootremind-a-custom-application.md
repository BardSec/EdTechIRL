---
title: "RebootRemind: A custom application to remind your Intune users to reboot"
subtitle: "Computers need sleep too!"
date: 2025-03-19
author: Andy Lombardo
source: https://www.edtechirl.com/p/rebootremind-a-custom-application
---

# RebootRemind: A custom application to remind your Intune users to reboot

*Computers need sleep too!*

[![A cartoon-style computer with a tired and exhausted expression. The monitor screen displays droopy eyes with bags underneath, and the keyboard appears slouched. The CPU looks fatigued but without sweat drops. A coffee cup sits beside it, half-empty. The background is a dimly lit office desk with scattered papers and wires.](https://substackcdn.com/image/fetch/$s_!sHa1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1171217f-cb66-42cb-a3a3-446a2aa4c0c9_1024x1024.webp "A cartoon-style computer with a tired and exhausted expression. The monitor screen displays droopy eyes with bags underneath, and the keyboard appears slouched. The CPU looks fatigued but without sweat drops. A coffee cup sits beside it, half-empty. The background is a dimly lit office desk with scattered papers and wires.")](https://substackcdn.com/image/fetch/$s_!sHa1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1171217f-cb66-42cb-a3a3-446a2aa4c0c9_1024x1024.webp)

### Introduction

About a year ago, I came across a post on the sysadmin subreddit asking what things admins have done that help cut down on ticket load. Throughout that post, I saw multiple people mentioning a reboot reminder that reminds users to restart their computers if they’ve been on for too long.

There’s a handful of tools that do this already, so you may be wondering why I bothered to create my own. Well, the issue is that my organization blocks opening cmd or powershell on standard user accounts. This causes an issue as the vast majority of these solutions I found were powershell scripts that have to be ran as the user to display the toast notification.

To avoid these issues, I wrote my own application in python so standard users could execute it.

(Also, I mentioned Intune in the title of this and will be walking through how to deploy this with Intune, but I’m sure it could be pushed with other MDMs as well)

[![](https://substackcdn.com/image/fetch/$s_!zpVO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd76fbf9e-b272-4e39-b3ea-62613e202c33_645x352.png)](https://substackcdn.com/image/fetch/$s_!zpVO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd76fbf9e-b272-4e39-b3ea-62613e202c33_645x352.png)

Just pretend that says 115 days instead of 0

### GitHub and File Breakdown

[The script can be found here on my GitHub account.](https://github.com/bradywidener/RebootRemind)

Here’s a breakdown of what files are in that repo.

- **HeroImage.png** - This is an icon that will display on your toast notification. This can be changed to any image, but I would recommend images with 96x96 resolution for the best results.
- **RebootRemind.xml** - This is an exported scheduled task that is imported whenever you run the install-rebootremind.ps1 file. The scheduled task is set to kick off our python program whenever a user logs in, and every 4 hours after that. You can change this frequency by editing the XML.
- **install-rebootremind.intunewin** - The packaged version of the application if you are fine with all of the defaults and want to directly upload. I tried to make this fairly generic so anyone who just wanted a quick and easy solution could deploy it. For the people who want to give it a more official touch, I will go over the customizations later.
- **install-rebootremind.ps1** - a script that will be used later for installing the application on devices by adding the program file folder to C:\Program Files and setting a scheduled task to kick it off. By default, the script is set to check the uptime every 4 hours in the scheduled task. You can change this frequency in this script.
- **rebootremind.py** - The python script. I’ll break down what it does in the next section.
- **remove-rebootremind.ps1** - a script used for uninstalling the program and scheduled task.

You may notice that the Python file isn’t compiled. I left it this way so you can make customizations before you package it up.

### rebootremind.py

The way this python script works, is that it gets the uptime of the device it is run on. By default, if the uptime shows as 7 days or more, it will create a toast notification for the end user telling them their uptime and asking them to restart at their earliest convenience. If the user clicks on the notification, by default, it will bring them to the Microsoft help guide on restarting your computer in windows. In my environment, I have the notification linked to an internal knowledge base article for restarting.

##### Here are the things you can customize

- **UpTime grade period** - by default it is 7 days. To change this, change the 7 in line 15.
- **Notification Title** - The toast notification title is located on line 20. Change Reboot Reminder to whatever you would like.
- **Notification Message** - There are effectively two messages set. First, it displays ‘Your computer needs a restart’ followed by the message with their uptime. Check lines 17 and 24 to change these.
- **Click Action** - As far as I know, the python module for toast notifications only supports having the toast notification take you to a hyperlink. Change the link on line 25 for a new site, or simply take the line out if you don’t want anything to happen.
- **HeroImage -** To change the logo that is used in the toast message, just replace the image once you download the repo with your own image named the same. I would recommend 96x96 pixel images for best practice!

### Compiling the program

Let’s go ahead and compile our python program. I’m doing this in VS Code with python and pip (python’s package manager) already installed.

1. First, let’s install the toast notification module by running the following command in cmd or powershell.  
   **pip install Windows-Toasts**
2. After a moment, this should finish. Next, let’s install the module we need to convert the python file to an exe.  
   **pip install auto-py-to-exe**
3. Next, type the following command, and the GUI below should pop up.  
   **python -m auto\_py\_to\_exe**

   [![](https://substackcdn.com/image/fetch/$s_!P9ij!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2c16f29-8b75-4012-a54f-5308717a9e4d_945x991.png)](https://substackcdn.com/image/fetch/$s_!P9ij!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb2c16f29-8b75-4012-a54f-5308717a9e4d_945x991.png)

   There’s a lot of buttons here, but there’s only 4 things you have to configure.  
     
   > Browse to the script location at the top.  
   > Change Console Window to Window Based.  
   > Under the Settings drop down, choose an output location. This is where the program will be saved after it is compiled.  
   > Under the Settings drop down, copy and paste the following into the box for Manual Argument Input.

   ```
   --hidden-import winrt.windows.foundation.collections --hidden-import winrt.windows.ui.notifications --hidden-import windows_toasts
   ```
4. This will run for a minute or two, and once it’s done, you should see this folder wherever you specified for your output directory.

[![](https://substackcdn.com/image/fetch/$s_!zmvj!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a652a57-51a6-4fb0-999c-80f9e2325823_1062x337.png)](https://substackcdn.com/image/fetch/$s_!zmvj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a652a57-51a6-4fb0-999c-80f9e2325823_1062x337.png)

Great! Now on to packaging this up for Intune.

### Packaging for Intune

Let’s go ahead and start piecing together a source folder for our Intune package. You are going to need the following things in a folder.

- The **rebootremind** folder that contains our exe that we just made.
- Both the install and remove script from my Github
- The RebootRemind.xml file that contains the blueprint for our Scheduled Task.
- The HeroImage.png from my github, or your own custom image. **Put this inside the rebootremind folder with the exe.**

  [![](https://substackcdn.com/image/fetch/$s_!vW4M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb430252d-69c8-4cab-9aca-d7f5b1d21e4d_707x135.png)](https://substackcdn.com/image/fetch/$s_!vW4M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb430252d-69c8-4cab-9aca-d7f5b1d21e4d_707x135.png)

I’m going to assume you’re familiar with IntuneWinAppUtil.exe for packaging apps as win32.

Once you have this packaged, I would use the following for your install command, uninstall command, and the detection.

**Install**

powershell.exe -ExecutionPolicy Bypass -file install-rebootremind.ps1

**Uninstall**

powershell.exe -ExecutionPolicy Bypass -file remove-rebootremind.ps1

**Detection**

[![](https://substackcdn.com/image/fetch/$s_!BqNq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d6cbcda-35a3-4f97-99ef-bb749ee75545_848x540.png)](https://substackcdn.com/image/fetch/$s_!BqNq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6d6cbcda-35a3-4f97-99ef-bb749ee75545_848x540.png)

### Conclusion

Once you’ve got it packaged, always be sure to test it out before deploying it to your environment. I have some Intune test VMs that were a perfect fit to test on as they hadn’t been restarted in a couple of weeks.

Enjoy!
