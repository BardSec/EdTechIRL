---
title: "Advanced Tips and Tricks for Win32 Application Packaging in Intune"
subtitle: "Win32 for the win!"
date: 2023-05-25
author: Andy Lombardo
source: https://www.edtechirl.com/p/advanced-tips-and-tricks-for-win32
---

# Advanced Tips and Tricks for Win32 Application Packaging in Intune

*Win32 for the win!*

[![](https://substackcdn.com/image/fetch/$s_!GrH2!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3585fb9-dded-44dd-a22e-08e8821268c7_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!GrH2!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa3585fb9-dded-44dd-a22e-08e8821268c7_1024x1024.png)

### Intro

I recently went through and packaged all my school district’s current software into win32 apps that can be pushed through Intune. This article is meant to give advice on making application packaging in Intune easier and some tricks to try when you’re having trouble. This article assumes that you have knowledge on how to package programs into win32 packages using the IntuneWinAppUtil.exe tool. If you have never used this, there are many great guides on doing this if you’re a beginner. This is meant to be a next step from that point.

Note that a lot of these tips aren’t necessarily Intune specific and can be applied to other MDMs too! Intune is just the focus for this article.

Also, I am continuing to add new tricks to this article as I find them. If you see a new one that wasn’t there before, that is why :)

### So why Win32?

Intune offers many different methods for packaging apps, but everyone recommends Win32. Why is this?

Well, Win32 has by far the most compatibility with programs. If you can find a way to have the installation run silently in the command line, then there will be a way you can get it to work using the Win32 method. It is also best practice to try and push all programs using the same method. If you push one program as a line-of-business app, and one as a Win32, there is a chance they could cause conflicts with each other. If you push everything as a Win32, each installer will run one at a time preventing this.

In a nutshell, you pretty much always want to use Win32 unless you don’t have any other options.

### My Process

Whenever I’m packaging a bunch of installers, I have found an order in doing things that speeds things up and helps save on the back-and-forth nature of packaging the programs. Here is what that looks like.

1. Download your installer.
2. Create a source and destination folder for your installer.
3. Figure out how to install your program from the command line. 99% of the time, if you get the install command correct for installing it from the folder, it will then work when packaged and uploaded to Intune. This helps with checking your installer arguments as well.
4. Find where the program files are located for your installer and copy that directory and a random file down. We will use this for our detection rule.
5. Uninstall the program through the command line, copy this command down as well.
6. Package the installer using the Win32 tool and upload.

(I highly recommend turning on clipboard history when doing this process, as it will save you lots of time being able to copy multiple things at once.)

### Tip 1: Look it up.

This one may seem obvious, but before you try to package a program as a Win32 (unless it appears to be very straight forward), try looking it up to see if anyone else has packaged the same program. We’re all about working smarter and not harder right? One of the best resources for this kind of thing is [Silent Install HQ](https://silentinstallhq.com/). They have some great articles for tricky installs.

### Tip 2: Try the MSI first!

Whenever you are going to package your installer, if the company who makes the program offers both an EXE and an MSI installer for the same program, I will go with the MSI installer almost every time. The reason for this is because when you package an MSI as a Win32, once you upload it to Intune, it will automatically fill in your install and uninstall commands. This saves a bit of time and can make life easier.

### Tip 3: Finding the Command Line Arguments for your installer.

Finding command line arguments for EXE installers can be very tricky if you’re new to MDM program deployment. Notice I said for EXE installers. For MSI installers, they use a standard format for command line arguments, so every MSI installer will use the same switches for basic functions like silent installing, no restart, etc.

[MSI Command Line Options](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/msiexec)

If you need to find the install arguments of an EXE, you can often go to command prompt, change directory so that you are in the same folder as the installer, and run *installername.exe /? **.*** This will often provide you with a pop-up box of the silent install switches. This also works with MSIs.

[![Command line arguments from Microsoft Remote Help](https://substackcdn.com/image/fetch/$s_!Ndkh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F637d9d9f-2958-4a89-bb9c-31cee66456d5_1353x746.png "Command line arguments from Microsoft Remote Help")](https://substackcdn.com/image/fetch/$s_!Ndkh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F637d9d9f-2958-4a89-bb9c-31cee66456d5_1353x746.png)

Command line arguments from Microsoft Remote Help

Unfortunately, this doesn’t work 100% of the time, but is definitely worthwhile to give a shot. The next best thing to do is to look up to see if the developers of the program have a solutions article with the install switches for their program. Sometimes they’ll even have additional switches that you can use to pre-modify settings. A good example of this is Zoom, which gives you the options to allow auto updates, configure your SSO Host, skip adding the desktop shortcut, and many more settings in the form of install switches.

[Zoom Install Switches](https://support.zoom.us/hc/en-us/articles/201362163-Mass-deploying-with-preconfigured-settings-for-Windows)

### Tip 4: 7Zip

Sometimes you can use 7Zip to unpackage installers and find other installers inside that are easier to work with. For example, if you unzip the consumer version of adobe acrobat reader, you have an MSI installer on the inside.

[![](https://substackcdn.com/image/fetch/$s_!UPvG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd00a3de-2429-49c2-9ef6-e021f993e61f_1147x477.png)](https://substackcdn.com/image/fetch/$s_!UPvG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbd00a3de-2429-49c2-9ef6-e021f993e61f_1147x477.png)

### Tip 5: Installer Shield

If you’ve worked with computers long enough, chances are that you will recognize this logo.

[![InstallShield: App Reviews, Features, Pricing & Download | AlternativeTo](https://substackcdn.com/image/fetch/$s_!ZMgO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a9130b6-b86d-4c35-b584-357beaa6d7bd_280x280.png "InstallShield: App Reviews, Features, Pricing & Download | AlternativeTo")](https://substackcdn.com/image/fetch/$s_!ZMgO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7a9130b6-b86d-4c35-b584-357beaa6d7bd_280x280.png)

This is the logo for InstallShield, a proprietary software used to create installers. It is pretty commonly used by many companies for packaging their software into an installer. If you have a software with this logo, you can try extracting it and sometimes there is an MSI inside. To do this, use the following command.

> setup.exe /s /x /b"C:\FolderInWhichMSIWillBeExtracted" /v"/qn"

[![](https://substackcdn.com/image/fetch/$s_!QlKR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91ade91c-d028-47ef-bc74-0c1593dbaae3_160x39.png)](https://substackcdn.com/image/fetch/$s_!QlKR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91ade91c-d028-47ef-bc74-0c1593dbaae3_160x39.png)

[![Image preview](https://substackcdn.com/image/fetch/$s_!YYsE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b0b4e5-0f42-4cdb-a1c0-41623181edb8_806x338.png "Image preview")](https://substackcdn.com/image/fetch/$s_!YYsE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b0b4e5-0f42-4cdb-a1c0-41623181edb8_806x338.png)

### Tip 6: Pushing Powershell Scripts as Win32

I know, you can also upload powershell scripts under the devices tab without packaging it as a Win32. However, you get lots of added benefits from doing this as a Win32. For one, it seems to be much faster in my experience. Another is that you get the option to add a powershell script to Company Portal as a kiosk install. I have done this to add ‘hotfixes’ to company portal. I have one in mine that will activate windows on the end user device (in case of emergencies), allowing them to self-service the issue without them ever seeing the license and without me needing to put it in for them.

[![](https://substackcdn.com/image/fetch/$s_!VeeB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c582898-92e8-4c53-9cf0-c6bda6c7fae6_1498x281.png)](https://substackcdn.com/image/fetch/$s_!VeeB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4c582898-92e8-4c53-9cf0-c6bda6c7fae6_1498x281.png)

To create something like this, all you need to do is create your powershell script and package it with Win32. Your install script should look something like this.

> powershell.exe -ExecutionPolicy Bypass -file thescript.ps1

Note that you will need to create an uninstall script for whatever function you are trying to accomplish, and you will need to figure out how to validate it with detection rules, depending on the function of the script.

### Tip 7: Multiple Installers for One Program

Sometimes it can be handy to create ‘create your own installer’ by packaging a script to kick off multiple installers. Typically, I would suggest using the dependencies feature in Intune opposed to doing it this way, but I have run into situations where I needed to write a script to kick off my multiple installers for one program, I needed to do something before/after the install, or maybe I wanted to create a suite of programs in one installer for programs that often go together.

To do this, you will want to package your installers and a powershell script in the source folder.

> Start-Process msiexec.exe -Wait -ArgumentList '/I installer1Setup.msi /quiet'
>
> Start-Process msiexec.exe -Wait -ArgumentList '/I installer2Setup.msi /quiet'
>
> Start-Process msiexec.exe -Wait -ArgumentList '/I installer3Setup.msi /quiet'

Here’s the basic setup of what that script should look like. The way this works is that it will kick off each installer one at a time and wait until the current installer is finished before starting the next. Note that all of these in the example are MSI installers. If you wanted to do this for an exe, you would simply replace msiexec.exe with your executable and add in the arguments/switches needed for silent install.

Then you would package this with the Win32 Utility and upload to Intune. For the install command, refer to tip 6 above.

### Tip 8: PSADT

If you have pushed applications before, you may be familiar with PSADT, or the PowerShell App Deployment Toolkit. This is a fairly complex, but powerful tool that can be used for manipulating package installs. PSADT is also pretty well known, so sometimes you can find silent install guides for PSADT, but not using other methods. Then once you have the installer created, you can package it and add it to Intune. Below is a guide to getting started with PSADT and Intune.

### Tip 9: Repackaging Tools

There’s also a bunch of repackaging tools available that let you manipulate installers, scan changes that are made by installers, rewrap the application, etc. Currently I am using the free version of [Master Packager](https://www.masterpackager.com/) and enjoying the additional functionality it provides.

### Tip 10: Winget to Find Parameters

Winget is the windows package manager. Winget can be used for installing programs on a device silently. Though this has many different ways you can use it to help with Win32 packaging, one way I want to highlight is finding install parameters using Winget.

For example, let’s say I am trying to install Silhouette Design Studio. Silhouette says on their sight they don’t support any silent install parameters, but the package is available on winget and supports silent installs there, so clearly there is a way to silently install it.

What we can do is we can download the package intune uses without installing it using the following command.

`winget download "SilouhetteStudio.Silouhette"`

After we run this, it will download the installer to a folder in the current users downloads. In this folder, we have the installer and a yaml file.

[![](https://substackcdn.com/image/fetch/$s_!csFH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a5e9237-ed95-4d40-940b-c39d88cbf996_862x465.png)](https://substackcdn.com/image/fetch/$s_!csFH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a5e9237-ed95-4d40-940b-c39d88cbf996_862x465.png)

If you open the yaml file in a text editor, it will give you lots of information about the package, including install parameters.

[![](https://substackcdn.com/image/fetch/$s_!1pAx!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1710a4ac-6565-4432-a841-a601bec44da6_878x694.png)](https://substackcdn.com/image/fetch/$s_!1pAx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1710a4ac-6565-4432-a841-a601bec44da6_878x694.png)

Not sure how often this works, but definitely worth checking on trickier program installs.
