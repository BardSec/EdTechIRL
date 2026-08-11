---
title: "Simplify Your Isolated Browser Workflow"
subtitle: "Kasm pt 3: Using the Kasm Browser Extension"
date: 2024-02-19
author: Andy Lombardo
source: https://www.edtechirl.com/p/simplify-your-isolated-browser-workflow
---

# Simplify Your Isolated Browser Workflow

*Kasm pt 3: Using the Kasm Browser Extension*

[![](https://substackcdn.com/image/fetch/$s_!BeDa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93114b13-64e0-4dc7-a996-9d64ca897840_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!BeDa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F93114b13-64e0-4dc7-a996-9d64ca897840_1024x1024.webp)

If you’ve created a Kasm instance to use for safely opening links, the next step to make it indispensable is to install the Kasm browser extension - available for [Chrome, Edge](https://chrome.google.com/webstore/detail/kasm-open-in-isolation/pamimfbchojeflegdjgijcgnoghgfemn?hl=en-US), and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/kasm-open-in-isolation).

Once installed and configured, you’ll have the ability to right-click on any link and choose “Open Link in Kasm” …

[![](https://substackcdn.com/image/fetch/$s_!h2Fw!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4eb4410-83e8-4c51-a2d8-f7a6502f0686_613x512.png)](https://substackcdn.com/image/fetch/$s_!h2Fw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4eb4410-83e8-4c51-a2d8-f7a6502f0686_613x512.png)

… And it will open the link in the Kasm isolated browser within your browser:

[![](https://substackcdn.com/image/fetch/$s_!gSJh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f300c7f-5887-4d99-8032-b35fad26888b_1920x1164.png)](https://substackcdn.com/image/fetch/$s_!gSJh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9f300c7f-5887-4d99-8032-b35fad26888b_1920x1164.png)

## Configuring the Extension

The main configuration of the extension is super simple. Click on the Kasm extension in your browser toolbar and it will bring up this menu:

[![](https://substackcdn.com/image/fetch/$s_!shFp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb05bbd7-8c8d-494e-920f-cd2658cfd08d_259x306.png)](https://substackcdn.com/image/fetch/$s_!shFp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbb05bbd7-8c8d-494e-920f-cd2658cfd08d_259x306.png)

Select “Extension Options.” In the window that opens, put your Kasm URL in the top field. This can be either the local IP address if you’re accessing from the same network or the IP address of your cloud server if you’re using a service like Linode or Digital Ocean, or you can use the domain name if you’ve set up a Cloudflare tunnel. Finally, scroll down and Save.

[![](https://substackcdn.com/image/fetch/$s_!BA5e!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabab2c28-83db-40b9-b1cf-2c61ebb8a4ba_391x507.png)](https://substackcdn.com/image/fetch/$s_!BA5e!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fabab2c28-83db-40b9-b1cf-2c61ebb8a4ba_391x507.png)

Now, as long as you’re signed in to Kasm, right-clicking a link and selecting Open in Kasm will open the link in isolation. If you aren’t signed in to Kasm, you’ll first be prompted to sign in.

## A little bit of additional configuration…

For this to work as seamlessly as we’d like, you’ll also want to set the default Kasm Workspace for your account. That way, the link will open without prompting you to pick a workspace. To set the default Workspace, click on your user icon in the upper right hand side of the main Kasm dashboard and select “Edit Profile”:

[![](https://substackcdn.com/image/fetch/$s_!-8Uo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e42cbe5-c2db-48a2-9211-176ee6bbe835_314x478.png)](https://substackcdn.com/image/fetch/$s_!-8Uo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9e42cbe5-c2db-48a2-9211-176ee6bbe835_314x478.png)

Click on “Settings” in the left-hand navigation panel and then under Default Workspace Image select the browser you’d like to use as your Default Workspace.

[![](https://substackcdn.com/image/fetch/$s_!T4gr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97581953-c070-4a2f-8aa0-2cf2ef1b9aaa_1181x641.png)](https://substackcdn.com/image/fetch/$s_!T4gr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F97581953-c070-4a2f-8aa0-2cf2ef1b9aaa_1181x641.png)

## Resources:

[Kasm Workspaces](https://kasmweb.com/)

[Part 1 of this series](https://www.edtechirl.com/p/creating-a-safe-space-for-web-browsing): [Creating a Safe Space for Web Browsing and Checking Out Hinky Links](https://www.edtechirl.com/p/creating-a-safe-space-for-web-browsing)

[Part 2 of this series: Kasm in the Cloud](https://www.edtechirl.com/p/kasm-in-the-cloud)
