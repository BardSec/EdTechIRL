---
title: "Weird VMware Quirk"
date: 2023-03-22
author: Andy Lombardo
source: https://www.edtechirl.com/p/weird-vmware-quirk
---

# Weird VMware Quirk

The first obstacle setting up my new server came early… with the first login to VMware. I’m not sure what the variable is, but on a fully updated Edge/Chrome browser and VMware 6.5 there’s an odd bug.

[![](https://substackcdn.com/image/fetch/$s_!5Tth!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaa13ce5-6950-4a14-9861-8453019998fc_562x241.png)](https://substackcdn.com/image/fetch/$s_!5Tth!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feaa13ce5-6950-4a14-9861-8453019998fc_562x241.png)

After entering the username and password, if you hit enter you’ll get this error message. When you hit reload, it logs you back out to repeat the process all over again.

[![](https://substackcdn.com/image/fetch/$s_!QH2-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf0951ad-5176-41c6-a6f3-061de618a057_904x322.png)](https://substackcdn.com/image/fetch/$s_!QH2-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcf0951ad-5176-41c6-a6f3-061de618a057_904x322.png)

Fortunately, there’s a really easy solution.

After entering username and password, click on Login instead of hitting enter.

Or, if you enter an incorrect password, and the page reloads with an incorrect password warning, entering username and password will then work when clicking enter. 🤷‍♂️🤷‍♂️🤷‍♂️

[![](https://substackcdn.com/image/fetch/$s_!xNt1!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4627d414-ce90-4444-ad8f-a84b33b1a8d0_1835x854.png)](https://substackcdn.com/image/fetch/$s_!xNt1!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4627d414-ce90-4444-ad8f-a84b33b1a8d0_1835x854.png)
