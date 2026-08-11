---
title: "Get in the Loop!"
subtitle: "Enabling Microsoft Loop Public Preview Tenant-Wide"
date: 2023-05-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/get-in-the-loop
---

# Get in the Loop!

*Enabling Microsoft Loop Public Preview Tenant-Wide*

[![New Microsoft Loop app is built for co-creation | Microsoft 365 Blog](https://substackcdn.com/image/fetch/$s_!9YcO!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24e1381e-7254-4c02-9723-89e48b428217_1024x577.jpeg "New Microsoft Loop app is built for co-creation | Microsoft 365 Blog")](https://substackcdn.com/image/fetch/$s_!9YcO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24e1381e-7254-4c02-9723-89e48b428217_1024x577.jpeg)

As a rabid Notion fan, I’m downright giddy to see Microsoft Loop. After launching in public preview a few weeks ago, I wanted to see if Loop could replace my paid Notion subscription, but the first hurdle was being able to access it.

To enable Loop in public preview, you first need to decide if you want to provide access to a specific group or your whole tenant. It’s always a good practice to test small before rolling out to everyone, so I’ve already done this process with users in my department. We’re three weeks in and everything has gone smoothly (knock on wood), so I’m now ready to provide access district-wide. As you’re going through this process, after deciding on the group, you’ll have to create a Cloud Policy and attach it to the group. The final step is the easiest, as it’s just wait an hour or so for the policy to propagate to your users.

**Here we go…**

1. Go to config.office.com and sign in with your M365 account.
2. Navigate to Customization —> Policy Management to create a new policy to allow Loop. Name the policy something obvious, and add a description. I also like to include my initials and a date created tag to my descriptions so Future-Me can have a little help when I come back and look at this a year or two from now.

[![](https://substackcdn.com/image/fetch/$s_!XWd-!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbdbb39c-b8d7-49ae-92c7-c1b23b7f9e46_1439x390.png)](https://substackcdn.com/image/fetch/$s_!XWd-!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdbdbb39c-b8d7-49ae-92c7-c1b23b7f9e46_1439x390.png)

3. Choose the appropriate scope that you want to push Loop to. I’ve already tested loop in a smaller test group, so I’m just going to go ahead and scope it to all users:

[![](https://substackcdn.com/image/fetch/$s_!IbT9!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91de0fd9-8eb8-48bb-b265-3f25cd2f755e_1151x343.png)](https://substackcdn.com/image/fetch/$s_!IbT9!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F91de0fd9-8eb8-48bb-b265-3f25cd2f755e_1151x343.png)

4. On the policies screen, search for Loop and select Create and view Loop files in Loop. You don’t need to configure the other two settings related to Outlook and other Microsoft apps because they’re on by default when you select “Create and view Loop files in Loop.”

[![](https://substackcdn.com/image/fetch/$s_!kgS_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88e58af1-b6ad-4275-beec-32878e110a60_1267x394.png)](https://substackcdn.com/image/fetch/$s_!kgS_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88e58af1-b6ad-4275-beec-32878e110a60_1267x394.png)

5. In the blade that opens when selecting Create and view Loop files in Loop, be sure to Enable the configuration setting:

[![](https://substackcdn.com/image/fetch/$s_!QvNK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18da7caf-0281-45f7-a9ba-4cc9b5858843_625x370.png)](https://substackcdn.com/image/fetch/$s_!QvNK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F18da7caf-0281-45f7-a9ba-4cc9b5858843_625x370.png)

6. Apply the setting above, then click Next, and you’ll be at the Review and Publish tab:

[![](https://substackcdn.com/image/fetch/$s_!Kkzh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6393e62-c157-4a2f-8761-6fcaa7ad5104_1013x750.png)](https://substackcdn.com/image/fetch/$s_!Kkzh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa6393e62-c157-4a2f-8761-6fcaa7ad5104_1013x750.png)

7. Make sure the scope and settings look appropriate, then click “Create” at the bottom of the page.

**At this point, Loop should be enabled for your scoped users, and should be accessible after the policy has a chance to propagate within an hour or so.**

[![](https://substackcdn.com/image/fetch/$s_!-lal!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9d2328e-28d9-4501-b475-a7cc13b3f56d_797x308.png)](https://substackcdn.com/image/fetch/$s_!-lal!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd9d2328e-28d9-4501-b475-a7cc13b3f56d_797x308.png)

In my demo tenant, this took about 5 minutes to become active. When I did it in my actual production tenant, it took about 45 minutes before all of my test users were able to access Loop.

Until the policy has taken effect, your users will see a message like below:

[![](https://substackcdn.com/image/fetch/$s_!6Liq!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8781a2be-be15-4124-a1e4-cb42a5957e19_600x327.png)](https://substackcdn.com/image/fetch/$s_!6Liq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8781a2be-be15-4124-a1e4-cb42a5957e19_600x327.png)

Once it’s ready, your users should see something like this when they log in to Loop.Microsoft.com:

[![](https://substackcdn.com/image/fetch/$s_!g7k3!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F454bd9ae-a922-440d-abbd-8835db248ca2_1677x1090.png)](https://substackcdn.com/image/fetch/$s_!g7k3!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F454bd9ae-a922-440d-abbd-8835db248ca2_1677x1090.png)

**Additional Resources:**

[Manage Loop experiences (Loop app and Loop components) in SharePoint - SharePoint in Microsoft 365 | Microsoft Learn](https://learn.microsoft.com/en-us/sharepoint/manage-loop-components)

[First things to know about Loop components in Microsoft Teams - Microsoft Support](https://support.microsoft.com/en-us/office/first-things-to-know-about-loop-components-in-microsoft-teams-ee2a584b-5785-4dd6-8a2d-956131a29c81)

[New Microsoft Loop app is built for co-creation | Microsoft 365 Blog](https://www.microsoft.com/en-us/microsoft-365/blog/2023/03/22/new-microsoft-loop-app-is-built-for-modern-co-creation/)
