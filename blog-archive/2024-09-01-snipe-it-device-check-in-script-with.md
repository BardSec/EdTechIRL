---
title: "Snipe IT - Device Check-in Script with Powershell"
subtitle: "Bringing in the missing feature of Snipe IT!"
date: 2024-09-01
author: Andy Lombardo
source: https://www.edtechirl.com/p/snipe-it-device-check-in-script-with
---

# Snipe IT - Device Check-in Script with Powershell

*Bringing in the missing feature of Snipe IT!*

[![](images/122188e2-2c26-47af-a39d-5b1980f2d64e_2048x2048.jpeg)](images/122188e2-2c26-47af-a39d-5b1980f2d64e_2048x2048.jpeg)

### Introduction

Though I am an absolutely huge fan of Snipe IT, one of glaring missing features is a way to mass check-in a list of devices through the Import feature. There are some work arounds for this missing feature, but in general, these work arounds are more confusing than just having the device listed as available and not checked out to a user. While searching online to see if anyone else had made a solution, I found that this feature is wanted by a handful of others as well.

To fix this, I wrote a PowerShell script that will allow you to check-in a list of devices from a CSV, by using the Snipe IT API.

### Download the Script

First, you will need to [download the script](https://github.com/bradywidener/Snipe-IT-CheckIn-Script) from my GitHub. There is also a sample, blank CSV there as well. Download a copy of these items.

[![](images/89af82c2-d9c8-4d31-ae0f-0d68f2742026_1191x353.png)](images/89af82c2-d9c8-4d31-ae0f-0d68f2742026_1191x353.png)

### Creating an API Token in Snipe

1. First, you will need to log into Snipe API and click on your profile in the top right, then **Manage API Keys**

[![](images/870f302b-384c-4c83-9069-07c9b9ff1089_496x339.png)](images/870f302b-384c-4c83-9069-07c9b9ff1089_496x339.png)

1. Click **Create New Token**
2. Give it a name. As soon as you do, it will show you a long string. Copy this and keep it somewhere safe, after you close the window there is no way to view it again. You will also want to paste this in our script on line 2. The variable will look something like this after it is filled in. Note that Bearer must come before your token.

   **$SnipeToken = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1N…”**
3. Next, on the API Keys page in Snipe, it also has your base API URL in the right corner. We will want to copy this down on the next line. It will look something like this.  
   **$SnipeAPIBase = "https://domain.snipe-it.com/api/vi"**
4. After this we need to figure out what status ID we would like to use. In general, I think it makes the most sense to use the status **Deployable**, when checking in devices. To find the status label you need, go to **Settings > Status Labels** in Snipe. When you hover your mouse cursor over one of the statuses, you can see what ID number is used for it in the URL preview at the bottom of the browser. For this example, Deployable uses status ID 12.

   [![](images/0475ee8e-887d-4d1e-aee4-67e1e0d2e4e9_1068x713.png)](images/0475ee8e-887d-4d1e-aee4-67e1e0d2e4e9_1068x713.png)
5. Once you have your status label, be sure it is correct on Line 34 of the script, like in my sample below.

   [![](images/46556a78-68cb-4345-a6c2-ab481121804a_1771x412.png)](images/46556a78-68cb-4345-a6c2-ab481121804a_1771x412.png)
6. After this, we have all of the information we need from Snipe.

### Filling out the CSV

As you’ll notice the Sample CSV is pretty blank. All you need to do is scan away and make a list of the Asset Tags you would like to check in, under the cell A1 that says **ID**.

[![](images/0d8f4ca1-6325-40b6-bfc4-2d88b2aad3bc_526x446.png)](images/0d8f4ca1-6325-40b6-bfc4-2d88b2aad3bc_526x446.png)

Lastly, before you run the script, you will need to add the path of the CSV to line 6 on the script.

[![](images/f20d3e1c-4f97-476c-85ab-dadd159d5955_942x171.png)](images/f20d3e1c-4f97-476c-85ab-dadd159d5955_942x171.png)

Once you have done all of this, you are ready to run the script. To start, I would recommend trying to run the script with just one asset to check-in, just to make sure everything behaves as expected.

Cheers!
