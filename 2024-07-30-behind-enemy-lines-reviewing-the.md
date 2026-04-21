---
title: "Behind Enemy Lines: Reviewing the Work of a Student Who Hacked His School Laptop"
subtitle: "We're going to be going over a video of a student hacking their school issued laptop and go through the steps on how to defend against the exploits in the video."
date: 2024-07-30
author: Andy Lombardo
source: https://www.edtechirl.com/p/behind-enemy-lines-reviewing-the
---

# Behind Enemy Lines: Reviewing the Work of a Student Who Hacked His School Laptop

*We're going to be going over a video of a student hacking their school issued laptop and go through the steps on how to defend against the exploits in the video.*

[![](https://substackcdn.com/image/fetch/$s_!466v!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4a07f7f-5329-4598-b0e2-9e12dfbca0fa_1024x1024.jpeg)](https://substackcdn.com/image/fetch/$s_!466v!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4a07f7f-5329-4598-b0e2-9e12dfbca0fa_1024x1024.jpeg)

One of the best compliments I had gotten during my IT career came from a student. While assisting in a classroom and trying to manually install a testing software, I said to the teacher “I’m not 100% sure, but I believe it is getting blocked by our Application Blocker policy”. To which the student replied “I’m sure it is! These things are locked down like Fort Knox!”. Little did this kid know, I am the one who blocks the games they’re trying to smuggle onto their devices.

### The Video

One day while on YouTube, I came across an interesting video. It was a video of a student explaining how they ‘hacked’ their school’s laptop through a series of exploits.

(**Warning**, in the video the student does use some explicit language and at times has some edgy/rude humor.)

While absolutely horrified of the things this student had found out, I was also the slightest bit intrigued with the student’s computer knowledge at that age. In a lot of ways, this video shifted my views on defending laptops from student misuse. Instead of looking at “What would ***a student*** do to misuse this laptop?” I started thinking of it as “How would ***I, myself,*** get around my own settings to misuse this laptop?”. Security through obscurity simply isn’t enough for the pesky 1% of students who are going to be pen testing their device to no end.

### The Exploits

In the video, the student does the following.

- Boots to a flash drive to use Linux.
- Moved files over from a game to play it on the windows.
- Installed Steam (gaming marketplace program) to load and install even more games.
- Created himself a local admin account in windows.
- Accessed the school’s Wi-Fi password.

Scary stuff, right? So, let’s talk about how to defend against it.

### Defense! Defense!

#### BIOS Protection

First off, **BIOS passwords are essential**. Without them, a student can turn a laptop into a brick, or reset windows and remove all other restrictions. Though it can be an incredible pain to set BIOS passwords, there are some options on how to automate this. For example, many computer manufacturers now offer ways to manage BIOS settings from within windows. I wrote an article on how to do this for Dell’s, and there is [a tool for doing this on Lenovo Thinkpads](https://blog.lenovocdrt.com/changing-the-bios-supervisor-password-with-intune-and-the-think-bios-config-tool/#solution-overview). I’m not sure the exact model of the device used in the video, but this would be worth looking into for the school’s IT admin.

If it comes down to it, we have also made scripts on Hak5 Rubber Duckies (a hacking tool that looks like a flash drive that allows you to create scripts that will execute keystrokes on a computer) to boot to BIOS and walk through the steps of creating a BIOS password. This takes a lot of frustration and time out of the process while also eliminating almost all human error.

#### Hide BitLocker Keys!

The student was also able to circumvent many of the settings because he had his BitLocker key accessible on their Microsoft Account. Luckily, this is a fairly easy [setting to turn off in Entra.](https://ourcloudnetwork.com/how-to-block-user-access-to-bitlocker-keys-in-microsoft-entra/)

Both the BIOS password and BitLocker key would have made it to where the student couldn’t boot to another OS/drive. This then prevents the windows exploit the student uses to gain a Local Admin account, which prevents his game installs, and access to the school’s hidden network Wi-Fi password (more on that later…)

#### End to all PUPs!

One of the bigger challenges to overcome in K12 are PUPs (potentially unwanted programs). Students are notorious for trying to install programs on their laptops that don’t require admin rights (I’ve seen versions of Minecraft, Roblox, Steam, and many modern web browsers that install to the user’s ‘AppData’ folder and because of this, don’t require admin rights as the program doesn’t write to the ‘Program Files’ folder). These are a real booger to deal with. The answer to solving this is to implement some form of application blocker on the device. Windows offers two ways to do this. [WDAC and AppLocker.](https://learn.microsoft.com/en-us/windows/security/application-security/application-control/windows-defender-application-control/wdac-and-applocker-overview)

In my opinion, I think WDAC is the future, but it’s risky to make work as you are risking preventing some of your allowed programs if you don’t whitelist correctly. Instead, I have opted to use AppLocker as I have found more consistency with it. Both of these tools let you define the apps you want to allow and the apps you want to block from running on computers.

I may end up writing a guide on implementing AppLocker, but for now I will say to be sure to ***test thoroughly,*** if you decide to implement or ever make any changes to an AppLocker policy. AppLocker is risky as it can be easy to accidentally block a process needed by windows and then suddenly the computer doesn’t function as it should. I have accidentally bricked test computers before to the point where I had to full on reimage, all because of a bad AppLocker policy. If I had assigned this to all devices, it would have been a Resume Generating Event for me. Though these policies are risky, they do work incredibly well once you get them going. The difference in unwanted programs on our devices have dropped dramatically since we started blocking signed executables from popular game publishers, from running on our devices.

#### Wireless Protection

Though I’m not a big network guy, I feel like I should mention that a hidden network with a PSK is not an ideal solution and the IT team for this school district should really opt for something else. Preferably, something with MAC filtering that would allow personal devices to be obsolete without access to the NAC. Perhaps some 802.1x for certificate-based authentication as well.

In conclusion, it’s always best to not assume what students are capable of when it comes to accessing games. You know what they say about assuming!
