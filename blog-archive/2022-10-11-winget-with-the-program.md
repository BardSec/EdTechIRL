---
title: "Winget with the Program"
date: 2022-10-11
author: Andy Lombardo
source: https://www.edtechirl.com/p/winget-with-the-program
---

# Winget with the Program

[![cardboard box lot](https://images.unsplash.com/photo-1513672494107-cd9d848a383e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHw3fHxwYWNrYWdlc3xlbnwwfHx8fDE2NjU0MzE5NzE&ixlib=rb-1.2.1&q=80&w=1080 "cardboard box lot")](https://images.unsplash.com/photo-1513672494107-cd9d848a383e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHw3fHxwYWNrYWdlc3xlbnwwfHx8fDE2NjU0MzE5NzE&ixlib=rb-1.2.1&q=80&w=1080)

Photo by [CHUTTERSNAP](https://unsplash.com/@chuttersnap) on [Unsplash](https://unsplash.com)

What gets my vote as the most badass Windows improvement of recent memory?

**Winget.**

If you’re not familiar with winget but have been around computers for a while, it’s a package manager like APT or Yum on Linux, Homebrew on Mac, or Chocolatey for Windows.

Winget is part of all currently supported versions of Windows 10 and Windows 11, and is compatible with all Windows versions 1709 or later.

To find out if you have winget, open a command prompt (or PowerShell) and enter:

> `winget`

If the output looks like below, you’re in business. If not, head to the Microsoft Store and download an app from Microsoft called App Installer. Winget is included as part of this app.

[![](https://substackcdn.com/image/fetch/$s_!c30Y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0865a52-b071-468b-a4f5-14afdf6d436d_879x456.png)](https://substackcdn.com/image/fetch/$s_!c30Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc0865a52-b071-468b-a4f5-14afdf6d436d_879x456.png)

**What can you do with winget?**

Winget allows for one-line software installation or updates for software in the winget repository, which currently (Oct 2022) includes 3,822 applications. You can also install Windows Store apps through winget, but they’re a little trickier (more on this later).

For example, if you want to install Notepad++, you would enter this command:

> `winget install notepad++`

Alternatively, if you already had notepad++ installed and wanted to update it, you’d enter:

> `winget upgrade notepad++`

If you want winget to upgrade all the eligible winget-compatible packages on your computer, you could run CMD as Administrator and enter:

> `winget upgrade --all --silent`

and it will search your computer for compatible packages and update them. You can do this without running as admin, but it will stop and prompt you for credentials repeatedly.

**What makes this powerful?**

If you’re deploying a ton of software, you can create a script to install your software either by pushing the script through Group Policy, an MDM, or during your setup process. If you have an MDM with a kiosk or self-service function, you can create a script for a specific piece of software and include it in the kiosk without having to mess with repackaging an exe or any other weird MDM configuration. It also makes it easy to update the software. In our dream scenario, we can use our Windows update ring settings and winget to make summer laptop reimaging obsolete.

This is also helpful if you want to make application packages that are specific groups in your organization. If you know that you want your IT team to have specific apps that are different from HR or Students or Teachers, you can make packages that are group specific.

**Additional Scripting Resources:**

There are a handful of sites that help make pre-configured scripts for winget packages. The one I use most often is winstall.app.

You can go to Winstall.app and either pick from a pre-made “pack” of apps, or build your own. It enables you to search for apps and build a package of apps that you can then convert to a single script. For example, if I wanted to make a pack of applications that I wanted to be on every device I image, I could go to winstall.app, create a package called “Default Image Installs,” and add apps through a point and click interface. For my package, I’m going to add Loom, Edge, Teams, OneDrive, and Microsoft 365 Office.

Once I select the apps, I get the option to get the command for winget either as a batch script, PS script, or as a json import.

[![](https://substackcdn.com/image/fetch/$s_!on6N!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd028ea9-3d8f-4fc7-9ce2-14a0fb8fb5ae_813x463.png)](https://substackcdn.com/image/fetch/$s_!on6N!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd028ea9-3d8f-4fc7-9ce2-14a0fb8fb5ae_813x463.png)

I could also choose to have this package publicly available, so it’s also available here: <https://winstall.app/packs/KCaqbAS_W>

[![](https://substackcdn.com/image/fetch/$s_!Qdzn!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa94daadd-f39b-4861-8f9b-856bd8f3bbf1_606x558.png)](https://substackcdn.com/image/fetch/$s_!Qdzn!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa94daadd-f39b-4861-8f9b-856bd8f3bbf1_606x558.png)

[Packs created by @EdTechIRLdotcom - winstall](https://winstall.app/users/1503832942275186691)

**Installing Windows Store Apps with winget:**

Installing Windows Store Apps is a little trickier, because they aren’t included in the winget repository by default. You can note this when you search for an app in winget… when I searched for “notepad,” the output looked like below:

[![](https://substackcdn.com/image/fetch/$s_!hBF1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7df4fe03-7511-4f7a-8855-18ffa1a32eb2_801x481.png)](https://substackcdn.com/image/fetch/$s_!hBF1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7df4fe03-7511-4f7a-8855-18ffa1a32eb2_801x481.png)

Notice that under source, some are listed as “msstore” and some are listed as “winget.” Applications with the source “winget” are part of the winget repository and can be added through sites like Winstall.app. However, you can add items from either source by copying the string located in the Id column. For example, if you had a computer that didn’t have Windows Notepad installed for some reason, you could install it with

> `winget install --id=9MSMLRH6LZF3 -e`

and it will install the MS Store app. If you set up a winget install script in the previous steps, you can just append this to the script as

> `&& winget install --id=9MSMLRH6LZF3 -e`

and it would look something like

> `winget install --id=Microsoft.Teams -e && winget install --id=Microsoft.Office -e && winget install --id=Microsoft.OneDrive -e && winget install --id=Loom.Loom -e && winget install --id=Microsoft.Edge -e && winget install --id=9MSMLRH6LZF3 -e` `--accept-package-agreements`

In contrast, the PowerShell command would look like this:

> `winget install --id=Microsoft.Teams -e ; winget install --id=Microsoft.Office -e ; winget install --id=Microsoft.OneDrive -e ; winget install --id=Loom.Loom -e ; winget install --id=Microsoft.Edge -e ; winget install --id=9MSMLRH6LZF3 -e --accept-package-agreements`

*Notes: The -e option is to use the exact ID string in the command… this helps as there are many apps with similar names. The -e option also makes the command case-sensitive. Also, for any apps downloaded from the MS Store, it’s going to prompt you to accept the store terms and conditio*ns. *The* --accept-package-agreements *option silently accepts the EULA.*

**Uninstalling Winget Applications**

It should also be noted that anything you install with winget can also be uninstalled. Simply run it with the winget uninstall command. To uninstall Microsoft Teams, for example, you would run:

> `winget uninstall --id=Microsoft.Teams -e`

**One last bonus:**

If you’re in a state that needs TestNav as a program for standardized testing, winget can install the auto-updating Microsoft Store version with this command:

> `winget install --id=9ND5FC7RPPX1 -e --accept-package-agreements`
