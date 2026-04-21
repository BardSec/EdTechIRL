---
title: "Set it and Forget it: Daily Silent Update of All Your Winget Apps"
subtitle: "Clicking \"Yes\" on UAC 1,000 times not required"
date: 2024-09-16
author: Andy Lombardo
source: https://www.edtechirl.com/p/set-it-and-forget-it-daily-silent
---

# Set it and Forget it: Daily Silent Update of All Your Winget Apps 

*Clicking "Yes" on UAC 1,000 times not required*

[![](https://substackcdn.com/image/fetch/$s_!A2xP!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30a971b0-fc53-45c4-b138-4fd7ab0ebf8e_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!A2xP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30a971b0-fc53-45c4-b138-4fd7ab0ebf8e_1024x1024.webp)

When it comes to updating software, there’s a debate between staying on the bleeding edge or waiting for others to test updates before you deploy. On my personal devices, I usually lean bleeding edge with Windows 11 Insider builds and MacOS Dev Beta. With the rate at which software vulnerabilities are discovered and exploited, I like to keep my installed software up to date, too. Manually managing this can be a nightmare, and there are tools that can help ([PatchMyPc’s Home Updater](https://patchmypc.com/home-updater) comes to mind for personal devices, and [Windows AutoPatch for Microsoft apps](https://learn.microsoft.com/en-us/windows/deployment/windows-autopatch/overview/windows-autopatch-overview)). Since I try to manage as many of my applicable software packages through [Winget](https://www.edtechirl.com/p/winget-with-the-program) as I can, I wanted to automate running Winget updates on a schedule.

---

*More on Winget:*

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.

---

## Winget Update Command

Updating all of your Winget and Microsoft Store software is a pretty basic command, just:

```
winget update --all
```

However, if you have a lot of software packages, this gets annoying fast, because it will prompt you with a UAC admin prompt prior to updating EACH package. I have one desktop with 39 packages installed. This is a pain. To get Winget to update all of the packages silently WITHOUT UAC prompts, there are 2 steps:

1. Make sure you’re running CMD (or Terminal or PowerShell) as Admin.
2. Run this command:   
   winget update --all --silent

[![](https://substackcdn.com/image/fetch/$s_!bJSg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eefb5f8-fcec-4e03-82e0-45e50749ee20_1956x1312.png)](https://substackcdn.com/image/fetch/$s_!bJSg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4eefb5f8-fcec-4e03-82e0-45e50749ee20_1956x1312.png)

Now that you have the command for these updates down, the next step is to automate it. Patching software is important, and it’s very easy to get behind. To automate this, I go old school and create a batch file and run it as a scheduled task.

## Batch File

To create the batch file, open Notepad and enter the following text:

```
winget update --all --silent
```

Next, save as wingetupdate.bat.

*NOTE: Make sure you save the file as wingetupdate.bat and **not** wingetupdate.bat.txt. To verify, find the file in File Explorer, make sure View —> File name extensions is checked. It should look like below:*

[![](https://substackcdn.com/image/fetch/$s_!lZ0y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0b63d5-8458-4625-a752-34a69b6d9e9e_1738x496.png)](https://substackcdn.com/image/fetch/$s_!lZ0y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffd0b63d5-8458-4625-a752-34a69b6d9e9e_1738x496.png)

Once the batch file is ready, you can test it by right-clicking on it and selecting Run As Administrator. If all is good, it will launch the CLI, pop up with a single UAC prompt for approval, and then run the update command.

## Scheduling Updates

Now that the batch file is tested and ready, open the Task Scheduler app. This is a pre-installed Windows app, so it should already be on your device. Click on Task Scheduler Library and then select Create Task…

[![](https://substackcdn.com/image/fetch/$s_!7nre!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69ac5355-bc6c-49f0-9784-b8de44505380_1568x692.png)](https://substackcdn.com/image/fetch/$s_!7nre!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F69ac5355-bc6c-49f0-9784-b8de44505380_1568x692.png)

On the Create Task screen, on the General tab give the task a descriptive name, then select “Run with the highest privileges” option, which is critical if you don’t want to have multiple UAC prompts. For my scenarios, I also leave this set to “Run only when user is logged on” as it doesn’t play well with the running whether user is logged on or not option.

[![](https://substackcdn.com/image/fetch/$s_!XdbH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12b302ca-c6d2-472a-b4ec-e80526d32551_626x476.png)](https://substackcdn.com/image/fetch/$s_!XdbH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F12b302ca-c6d2-472a-b4ec-e80526d32551_626x476.png)

On the Trigger tab, click new, select a frequency and time, and make sure the “Enabled” box is checked.

[![](https://substackcdn.com/image/fetch/$s_!8FRB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F923a0405-afd9-47da-87b5-884c34b1e86a_1630x1140.png)](https://substackcdn.com/image/fetch/$s_!8FRB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F923a0405-afd9-47da-87b5-884c34b1e86a_1630x1140.png)

On the Actions tab, click New, then select “Start a program” and browse for the batch file we previously saved and click OK.

[![](https://substackcdn.com/image/fetch/$s_!RQbS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65e73fdc-6cf4-4c0f-ae25-5bbb4a3d9b69_455x501.png)](https://substackcdn.com/image/fetch/$s_!RQbS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F65e73fdc-6cf4-4c0f-ae25-5bbb4a3d9b69_455x501.png)

On the Settings tab the defaults should be acceptable, but can be tweaked based on your needs. To be able to test it, make sure “Allow task to be run on demand” is checked. Click OK when you’re done. Mine is set like this:

[![](https://substackcdn.com/image/fetch/$s_!YteY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b56c1eb-9267-448e-afee-1e1a02a6259c_635x481.png)](https://substackcdn.com/image/fetch/$s_!YteY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9b56c1eb-9267-448e-afee-1e1a02a6259c_635x481.png)

Now, in Task Scheduler, click on the newly created task to select it, then click Run.

[![](https://substackcdn.com/image/fetch/$s_!1dku!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd989f33f-ee1b-4365-bdcc-bfbb3a42bbde_1129x794.png)](https://substackcdn.com/image/fetch/$s_!1dku!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd989f33f-ee1b-4365-bdcc-bfbb3a42bbde_1129x794.png)

When this runs, a CLI window should pop up and run with no need for intervention. It should disappear when it finishes running.

[![](https://substackcdn.com/image/fetch/$s_!om2y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f82d9fb-6612-4880-bdfc-a740a9de1881_730x487.png)](https://substackcdn.com/image/fetch/$s_!om2y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f82d9fb-6612-4880-bdfc-a740a9de1881_730x487.png)

Under the Last Run Result column in Task Scheduler, you should now see “The operation completed successfully” like below:

[![](https://substackcdn.com/image/fetch/$s_!uNcD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e608b8e-f09b-48b3-a518-e2fde8576993_770x348.png)](https://substackcdn.com/image/fetch/$s_!uNcD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8e608b8e-f09b-48b3-a518-e2fde8576993_770x348.png)

From now on, this script should run based on the schedule you set.

## Level Up

Take this to the next level by tweaking your command line arguments in the batch file.

### Possible helpful arguments:

#### --wait

Requires user interaction (hit enter) to close the window when Winget finishes running. This lets you see that the command was run if you like having that confirmation without having to open Task Scheduler

#### --accept-package-agreements / --accept-source-agreements

Auto-accepts package and / or source agreements

#### --allow-reboot

If an install requires reboot (rare in my experience), this allows reboot

#### --verbose

Enables verbose logging

Further documentation on arguments in Winget can be found [here](https://learn.microsoft.com/en-us/windows/package-manager/winget/install).

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.
