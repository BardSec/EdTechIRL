---
title: "Escalating Privileges Using Touch ID in the Mac Terminal"
date: 2024-05-29
author: Andy Lombardo
source: https://www.edtechirl.com/p/escalating-privileges-using-touch
---

# Escalating Privileges Using Touch ID in the Mac Terminal

[![A person standing in front of a giant combination lock, entering a password, depicted in a silk screen style. The combination lock is massive, with large, numbered dials. The person is turning one of the dials, focused on the task. The background shows a high-tech security room with various control panels and screens. The colors are bold and vibrant, with a simplified, graphic look typical of silk screen art.](images/0f34937a-0e62-47b1-ab11-e178d8fbc979_1024x1024.webp "A person standing in front of a giant combination lock, entering a password, depicted in a silk screen style. The combination lock is massive, with large, numbered dials. The person is turning one of the dials, focused on the task. The background shows a high-tech security room with various control panels and screens. The colors are bold and vibrant, with a simplified, graphic look typical of silk screen art.")](images/0f34937a-0e62-47b1-ab11-e178d8fbc979_1024x1024.webp)

As a new Mac user, I’m a stranger in a strange land. Using the Terminal helps provide a thread of continuity for me, but I’m sick of typing in my sudo password. To enable TouchID to allow admin access in the Terminal, start by going to this directory:

> `cd /etc/pam.d`

and then make a new sudo\_local config file from the sudo\_local.template template file:

> `sudo cp sudo_local.template sudo_local`

Next, open sudo\_local and remove the comment from the indicated line by deleting the # at the beginning of the row.

> `sudo nano sudo_local`

The file should look like the example below:

[![](images/2d1fb37b-979c-46b6-a445-d365ed158fd7_1138x748.png)](images/2d1fb37b-979c-46b6-a445-d365ed158fd7_1138x748.png)

Finally, hit Ctrl-X and Y to save the change. Now, when trying to escalate your privileges to sudo in the Mac terminal, you can use Touch ID. If you want to use your Apple Watch, selecting the Use Password option on the sudo prompt will give you the option of unlocking with Watch.

[![](images/fd86043a-7c0f-4381-ad71-0e17f9afdef1_1574x1252.png)](images/fd86043a-7c0f-4381-ad71-0e17f9afdef1_1574x1252.png)

Note: This (and similar methods) were previously lost when performing macOS updates and upgrades. As of Sonoma, the config change persists through updates.
