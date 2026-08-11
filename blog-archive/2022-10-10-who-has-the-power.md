---
title: "Who has the power?"
subtitle: "Troubleshooting battery issues with the Windows Battery Report"
date: 2022-10-10
author: Andy Lombardo
source: https://www.edtechirl.com/p/who-has-the-power
---

# Who has the power?

*Troubleshooting battery issues with the Windows Battery Report*

[![black and silver flash drive](https://images.unsplash.com/photo-1608224873587-81ee37394b4e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHwxMHx8YmF0dGVyeXxlbnwwfHx8fDE2NjU0MTU4MzY&ixlib=rb-1.2.1&q=80&w=1080 "black and silver flash drive")](https://images.unsplash.com/photo-1608224873587-81ee37394b4e?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHwxMHx8YmF0dGVyeXxlbnwwfHx8fDE2NjU0MTU4MzY&ixlib=rb-1.2.1&q=80&w=1080)

Photo by [John Cameron](https://unsplash.com/@john_cameron) on [Unsplash](https://unsplash.com)

Batteries are a common laptop issue that needs troubleshooting, and without visibility into what’s going on with the battery, this can be tough. Battery problems can be any of a 1,000 possibilities, ranging from faulty hardware to a student insisting they charged their device when they didn’t. A good first step in figuring out where the problem lies is running a battery report.

To run the report, open the command prompt (press the Windows key, and when the search box comes up, search for cmd or Command Prompt... it will be the top option).

Depending on your environment’s security restrictions, if you're logged in as a student, you may need to run Command Prompt as Administrator to be able to launch the command prompt. To do this (if you have admin rights), press the Windows key, search for cmd or Command Prompt, and then right-click on it and choose "Run as Adminstrator." It will prompt you to enter admin credentials.

**Run this command:**

`powercfg /batteryreport`

It should give you a response that says "Battery life report saved to file path C:\WINDOWS\system32\battery-report.html." If you didn’t log in as the administrator, the path may be different, like

`C:\Users\your.name\battery-report.html`

**View the Report:**

Type or copy and paste the file path where your report is located into the command prompt and hit enter.

This will open the battery report for you to view. If it prompts you to ask what program you want to view it in, Edge is fine.

**Report Sections:**

The battery report “Installed Batteries” section provides details on the specific battery and how many times the battery has been charged in its life (cycle count) and what the battery health is, based on its designed capacity vs current full charge capacity. The example below shows a battery designed for 42,067 mWh and has a current full charge capacity of 38,844 mWh, which is about 93%. We consider 70-100% capacity remaining to be good… below that, we start to consider battery replacement, depending on cost and availability.

[![](https://substackcdn.com/image/fetch/$s_!mUd1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F251bbc22-dc7b-4c22-b015-b1e426f54887_382x288.png)](https://substackcdn.com/image/fetch/$s_!mUd1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F251bbc22-dc7b-4c22-b015-b1e426f54887_382x288.png)

The “Recent Usage” and “Battery Usage” sections show battery drain over the past 3 days. I’ve had mine on charge all weekend, so my recent usage is pretty boring. If you’re trying to figure out if a device is really being charged, this is the most helpful place to start:

[![](https://substackcdn.com/image/fetch/$s_!fBeq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F03365987-1df2-4bee-bfd0-cb1c9541a8d5_879x754.png)](https://substackcdn.com/image/fetch/$s_!fBeq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F03365987-1df2-4bee-bfd0-cb1c9541a8d5_879x754.png)

The “Usage History” section shows a comprehensive overview of when the device was on battery power vs. AC power with a breakdown of duration. This is a good place to look for trends. This does include time that the laptop was off but plugged in (note that it was charging for virtually 24 hours on 10-6, 10-7, 10-8, and 10-9, which I can confirm because it’s sat untouched on my desk while connected to power those days.

[![](https://substackcdn.com/image/fetch/$s_!uQ_7!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6443ce07-e6e1-4d75-bfea-455b681c61ce_717x773.png)](https://substackcdn.com/image/fetch/$s_!uQ_7!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F6443ce07-e6e1-4d75-bfea-455b681c61ce_717x773.png)

The “Battery Capacity History” section shows your batteries efficacy over time and whether or not it’s losing capacity. This is mostly helpful in the first year of a new device when the battery may still be under warranty. If you can show that there’s a discrepancy between Full Charge Capacity and Design Capacity, you may be able to get some warranty leverage - though I’ve very rarely had luck with any warranty claim involving a battery.

[![](https://substackcdn.com/image/fetch/$s_!zUE3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4c9421fa-50bd-406e-9128-56dad76fc2b5_453x775.png)](https://substackcdn.com/image/fetch/$s_!zUE3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4c9421fa-50bd-406e-9128-56dad76fc2b5_453x775.png)

Finally, the “Battery Life Estimates” section gives you an idea of how long the device \*should\* last on a full charge. If the battery life isn’t in this ballpark after a full charge, it’s likely due to the user using battery-intensive settings. I’ve noticed a really strong overlap in the Venn diagram between the folks who say their batteries die after a couple hours and the ones who are constantly watching YouTube at full screen brightness while also playing a game and listening to headphones.

[![](https://substackcdn.com/image/fetch/$s_!Ch_m!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7cf286d4-cac3-4a7e-84ab-1ceb696ef321_715x832.png)](https://substackcdn.com/image/fetch/$s_!Ch_m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7cf286d4-cac3-4a7e-84ab-1ceb696ef321_715x832.png)
