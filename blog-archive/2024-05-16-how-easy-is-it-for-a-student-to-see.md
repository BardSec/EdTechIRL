---
title: "How easy is it for a student (or anyone) to see your passwords if you leave your computer unattended for 5 minutes?"
date: 2024-05-16
author: Andy Lombardo
source: https://www.edtechirl.com/p/how-easy-is-it-for-a-student-to-see
---

# How easy is it for a student (or anyone) to see your passwords if you leave your computer unattended for 5 minutes?

[![A cartoon-style illustration of a preschool student cracking the lock of a bank safe. The student, a small child with curly brown hair and wearing a bright red t-shirt and blue shorts, is intently focused on turning the large dial of a classic metal safe. The scene is whimsical, set in a vibrant classroom filled with colorful educational toys and posters. The safe is exaggerated in size, towering over the child, adding a humorous touch to the depiction of this unlikely scenario.](https://substackcdn.com/image/fetch/$s_!Fc0h!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07383a0e-c76d-455b-a520-61d6056ab16c_1024x1024.webp "A cartoon-style illustration of a preschool student cracking the lock of a bank safe. The student, a small child with curly brown hair and wearing a bright red t-shirt and blue shorts, is intently focused on turning the large dial of a classic metal safe. The scene is whimsical, set in a vibrant classroom filled with colorful educational toys and posters. The safe is exaggerated in size, towering over the child, adding a humorous touch to the depiction of this unlikely scenario.")](https://substackcdn.com/image/fetch/$s_!Fc0h!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07383a0e-c76d-455b-a520-61d6056ab16c_1024x1024.webp)

Ok, so I went for the clickbait headline. But a question I field from a lot of educators is, “Yeh, but, REALLY, who would try to break into my accounts?”

External attackers aside, after a decade of teaching middle school, I can say pretty confidently that in most classes of 30 students, there are a few who would like to access your account for a variety of reasons… some just to see if they can get in, others to disrupt or delay class, and some to see if they can embarrass you. Of those, there’s a good chance that at least one would try if they had the knowledge and were given the opportunity.

So, REALISTICALLY, how quickly could someone compromise your credentials?

If you save your passwords in your browser to autofill, it can take seconds. You can also follow along to see how easy it is.

If you have autofill enabled and your computer is unattended, a student can open a password protected site like PowerSchool and get a login page like below. From here, if the credentials are autofilled, they could sign in to your account and have access for as long as they have access to the device.

[![](https://substackcdn.com/image/fetch/$s_!jRgC!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6661089a-2266-4e3b-a24a-aa40df33cf36_1354x752.png)](https://substackcdn.com/image/fetch/$s_!jRgC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6661089a-2266-4e3b-a24a-aa40df33cf36_1354x752.png)

If they want to have continued access, however, they just need to right-click in the password box and select “Inspect.” On the Inspect pane that opens, next to “input type” it will say password. Double-click on the word **password** and replace it with the word **text**. The password will now be visible in the password box. They can then make a note of the password and change the input type from **text** back to **password** and they’ve harvested your credentials in a few seconds.

[![](https://substackcdn.com/image/fetch/$s_!igXu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16ae3045-eb09-4409-a6dc-1240311d38d8_2504x2212.png)](https://substackcdn.com/image/fetch/$s_!igXu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16ae3045-eb09-4409-a6dc-1240311d38d8_2504x2212.png)

## How can you protect against this?

1. For an administrative/technical solution, your technology staff can disable access to the Inspect tool. It’s very likely that they’ve already disabled Inspect for students. In my organization, we disabled Inspect for students because they learned they could check their grades online, open the Inspect tool, and change their grades on the screen to convince teachers that they’d “hacked” the gradebook. Changes made using the Inspect tool only happen on the screen of the device being used and not on the server where the grades live, so nothing was hacked, but it led to a bountiful harvest of panicked tickets and phone calls.
2. Limit time that your device is unlocked and unattended. Enforcing a 5, 10, or even 15-minute lockout policy on staff devices is difficult, because during the course of a lesson a teacher may have their device casting to a TV or interactive whiteboard without needing to be touched for the duration of a lesson, and having to go repeatedly unlock the device can be inconvenient every 15 minutes, but downright annoying if it’s happening every 5 minutes. Finding a good happy median lockout time is advisable, but also manually locking the screen if you leave the room.
3. Turn off autofill in your browser password settings, or set autofill to require entering a password before filling.
4. Enable Multi Factor Authentication (MFA) whenever and wherever you can. MFA won’t stop the attacker from finding out credentials in this example, but it will stop them from being able to use them.
5. Limit recycled passwords. Reusing the same password over and over can become a real killer — if one password is compromised, the effects can snowball if your TikTok, Instagram, Yahoo, Verizon, and Wells Fargo accounts all use the same email address and password. If the account is a school account, it could also unlock other resources, like access to wifi, local administrative rights, abilities to bypass network filtering, etc.
