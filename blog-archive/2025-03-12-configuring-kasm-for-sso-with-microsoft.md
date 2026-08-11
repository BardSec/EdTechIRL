---
title: "Configuring KASM for SSO with Microsoft"
subtitle: "Level up your KASM instance by doubling down on Least Privilege, RBAC, and MFA"
date: 2025-03-12
author: Andy Lombardo
source: https://www.edtechirl.com/p/configuring-kasm-for-sso-with-microsoft
---

# Configuring KASM for SSO with Microsoft

*Level up your KASM instance by doubling down on Least Privilege, RBAC, and MFA*

[![A vibrant and colorful illustration of a computer trapped inside a birdcage. A person is unlocking the cage with a large, ornate key. The scene has a whimsical and slightly surreal feel, with glowing light emanating from the computer screen, symbolizing freedom. The background is artistic and dreamlike, enhancing the sense of liberation.](https://substackcdn.com/image/fetch/$s_!KDUB!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc893f886-27cd-4a89-a306-283e8eb818a0_1024x1024.webp "A vibrant and colorful illustration of a computer trapped inside a birdcage. A person is unlocking the cage with a large, ornate key. The scene has a whimsical and slightly surreal feel, with glowing light emanating from the computer screen, symbolizing freedom. The background is artistic and dreamlike, enhancing the sense of liberation.")](https://substackcdn.com/image/fetch/$s_!KDUB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc893f886-27cd-4a89-a306-283e8eb818a0_1024x1024.webp)

In the previous three KASM articles, we talked about setting up KASM on-prem and in the cloud. We also mentioned using CloudFlare for reverse proxy and being able to require MFA for signin. To kill two birds with one stone, this article will look at changing MFA to Microsoft and then allowing Microsoft to also handle user provisioning based on Entra ID groups.

**So what?**

The desired state at the end of this tutorial is to be able to take your existing KASM instance and allow users in your organization to sign in and be assigned specific Workspaces based on Entra ID group memberships. If your Microsoft accounts require MFA (WHICH THEY SHOULD), you’ll pick up that added bonus. If you haven’t set up your KASM instance yet, checkout the previous articles in this series here: [part 1](https://www.edtechirl.com/p/creating-a-safe-space-for-web-browsing), [part 2](https://www.edtechirl.com/p/kasm-in-the-cloud), and [part 3](https://www.edtechirl.com/p/simplify-your-isolated-browser-workflow).

**Below, we’ll go through the process of setting up an App Registration in Azure, we’ll configure SSO in KASM to use Microsoft for authentication, and we’ll delegate access to KASM workspaces based on Entra security group membership.**

## **Getting Started:**

### **Creating an App Registration in Azure**

Go to portal.azure.com and search for App Registrations. On the App Registrations page, click **+ New Registration**.

On the New Registration page, there are 4 things that need to be completed:

1. Name your application
2. Select **Accounts in this organizational directory only** (otherwise anyone with an MS account can sign in)
3. For redirect URI, select Web
4. Enter your OIDC callback address. For KASM, this will be your KASM’s domain name followed by **/api/oidc\_callback**. In my case, **https://kasm.lomlabs.work/api/oidc\_callback**

[![](https://substackcdn.com/image/fetch/$s_!iQ3I!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88f19f62-4cb5-4545-92c0-49378cae4616_866x647.png)](https://substackcdn.com/image/fetch/$s_!iQ3I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88f19f62-4cb5-4545-92c0-49378cae4616_866x647.png)

Next, click Register at the bottom of the screen.

After registering, you’ll be back at the new App’s Overview page. Copy the **Application (client) ID** (1 below) and save it for later. Then click on **Client Credentials: Add a certificate or secret** (2).

[![](https://substackcdn.com/image/fetch/$s_!xr-A!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72ff6e5b-e43f-4f0c-93a6-2767463a3784_1450x358.png)](https://substackcdn.com/image/fetch/$s_!xr-A!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72ff6e5b-e43f-4f0c-93a6-2767463a3784_1450x358.png)

Under Client Secrets, click + New client secret

[![](https://substackcdn.com/image/fetch/$s_!69QW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F669c6315-6983-4fff-ad94-7de27752c6a5_498x201.png)](https://substackcdn.com/image/fetch/$s_!69QW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F669c6315-6983-4fff-ad94-7de27752c6a5_498x201.png)

Give it a name, and pick an expiration date:

[![](https://substackcdn.com/image/fetch/$s_!Lxpt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9cbb429-b10e-4d9e-9ddd-9d2fe0908624_578x145.png)](https://substackcdn.com/image/fetch/$s_!Lxpt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9cbb429-b10e-4d9e-9ddd-9d2fe0908624_578x145.png)

IMPORTANT: On the next screen, copy the Client Secret Value (not the Secret ID). The Secret Value can only be seen immediately after creation. If you forget to copy it, you’ll need to delete the secret and make a new one.

[![](https://substackcdn.com/image/fetch/$s_!lbAU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c70ad76-1c2f-416b-8c37-0b328f77304f_1031x223.png)](https://substackcdn.com/image/fetch/$s_!lbAU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c70ad76-1c2f-416b-8c37-0b328f77304f_1031x223.png)

Next, from the Overview page again, click Endpoints near the top of the page.

[![](https://substackcdn.com/image/fetch/$s_!njZR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb422404f-734d-471d-98cd-89230910cf2d_618x225.png)](https://substackcdn.com/image/fetch/$s_!njZR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb422404f-734d-471d-98cd-89230910cf2d_618x225.png)

It will open up a blade on the side of the page with a lot of website addresses. You need to copy the ones for **OAuth 2.0 authorization endpoint (v2)** and **OAuth 2.0 token endpoint (v2)**. NOTE: Be sure to pick v2 instead of v1.

Next, click on the Token Configuration link under the Manage menu on the left-hand navigation menu, then +Add Group Claim. Check the box for Security Groups, and then click Add.

[![](https://substackcdn.com/image/fetch/$s_!KQN_!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c4fea90-b795-4a2e-afc1-20ed73fe3be3_1273x895.png)](https://substackcdn.com/image/fetch/$s_!KQN_!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8c4fea90-b795-4a2e-afc1-20ed73fe3be3_1273x895.png)

### Configuring KASM

Once you have those details gathered, log in to your KASM instance and go to the Admin tab, then go to **Access Management —> Authentication —> OpenID** and then click on **+ Add Config**.

In the Display Name field, enter the text you want to show up next to the Login with Microsoft button on the KASM login page. I’m going to use **Microsoft Login**.

For logo URL, you can use **https://www.microsoft.com/favicon.ico**

Toggle on the **Enabled** switch

Toggle on the **Default** switch

If you toggle on the **Auto Login** switch, then when you visit your KASM page it will automatically kickoff the Microsoft sign in process.

[![](https://substackcdn.com/image/fetch/$s_!JjeY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42ac5f49-7cc0-4076-913d-76c5b51c57c0_526x503.png)](https://substackcdn.com/image/fetch/$s_!JjeY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F42ac5f49-7cc0-4076-913d-76c5b51c57c0_526x503.png)

In the Client ID field, enter the **Application (Client) ID** from Azure.

In the Client Secret field, enter the secret value from Azure.

For Authorization URL, use the web address you copied for the **OAuth 2.0 authorization endpoint (v2) value**

For the Token URL, use the web address you copied for the **OAuth 2.0 token endpoint (v2) value**

The User Info URL will be **https://graph.microsoft.com/oidc/userinfo**

[![](https://substackcdn.com/image/fetch/$s_!KmM5!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f341138-be70-4eb4-9443-4074fd5c8214_486x434.png)](https://substackcdn.com/image/fetch/$s_!KmM5!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5f341138-be70-4eb4-9443-4074fd5c8214_486x434.png)

Under Scope, enter **openid**, **email**, and **profile**, each on a separate line.

For username attribute, enter **email**, and for Groups Attribute put **groups**.

In the Redirect URL, put the same value you entered for URL Redirect in the Azure application (i.e., domain name followed by **/api/oidc\_callback**), and click Save.

[![](https://substackcdn.com/image/fetch/$s_!cqIr!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9509130-8a8b-4cc0-b97f-7c6e9e6bc8e0_513x712.png)](https://substackcdn.com/image/fetch/$s_!cqIr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9509130-8a8b-4cc0-b97f-7c6e9e6bc8e0_513x712.png)

### Testing It Out

At this point, your KASM login page should now have a Microsoft Login button.

[![](https://substackcdn.com/image/fetch/$s_!VZbQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d830bdc-7cc6-418e-9e7c-1a75e0938338_870x404.png)](https://substackcdn.com/image/fetch/$s_!VZbQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8d830bdc-7cc6-418e-9e7c-1a75e0938338_870x404.png)

The first time you login to this application, you’ll need to Consent to the use of the application for your organization (if you’re an M365 admin). If you aren’t an admin, you’ll have to submit a request for approval.

[![](https://substackcdn.com/image/fetch/$s_!n6Yd!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F168615f6-6ac6-4197-97bd-d8206db88748_480x639.png)](https://substackcdn.com/image/fetch/$s_!n6Yd!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F168615f6-6ac6-4197-97bd-d8206db88748_480x639.png)

### Granular Group Access

Now that the connection between Microsoft and KASM is complete, we can work on providing tailored KASM access based on Microsoft Security Group roles in Entra ID.

In KASM as an Administrator, go to **Access Management —> Groups —> + Add Group**.

We’re going to create an Admin group that’s tied to my IT-Admin Group in Azure. Enter the group name, Priority (lower numbers are higher priority… There is a default system Administrator group with priority 1, so we’re using 2), then click **Save**.

[![](https://substackcdn.com/image/fetch/$s_!GjeU!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4773114-2118-40e0-8159-83337f4545a7_943x476.png)](https://substackcdn.com/image/fetch/$s_!GjeU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4773114-2118-40e0-8159-83337f4545a7_943x476.png)

Now that the group is created, click on the group and select the edit icon so we can configure it. Once in edit mode, select **SSO Group Mappings** from the top tabs and then click on **+ Add SSO Mapping** and a dialog box will open. In the SSO Provider drop down, pick the display name of the OpenID connection we set up earlier. Then, leave this dialog box open and head to a new tab.

Now, take a short detour to Azure and search for the Security Group you want to map to this KASM group. Copy the Azure Object ID for the group like below:

[![](https://substackcdn.com/image/fetch/$s_!SfBA!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0844f106-4506-42e0-9ad2-52f7f68d2e31_1072x434.png)](https://substackcdn.com/image/fetch/$s_!SfBA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0844f106-4506-42e0-9ad2-52f7f68d2e31_1072x434.png)

Now, enter this Object ID in the Group Attributes box in the Add SSO Group Mapping Dialog box that’s open in KASM and click **Submit**.

[![](https://substackcdn.com/image/fetch/$s_!NrJG!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8f22874-3a15-4bf7-9feb-dc2613082376_835x696.png)](https://substackcdn.com/image/fetch/$s_!NrJG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd8f22874-3a15-4bf7-9feb-dc2613082376_835x696.png)

Now that the groups are mapped, go back to the **Access Management —> Groups** tab in KASM admin, click the Edit icon next to your new group, go to the **Permissions** tab at the top of the page, and then click **+ Add Permissions**. For an administrator group, select Global Administrator from the drop-down menu and then click **Submit.**

[![](https://substackcdn.com/image/fetch/$s_!c2SY!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0472a1d6-2acc-4847-94d9-3d88410f9869_536x320.png)](https://substackcdn.com/image/fetch/$s_!c2SY!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0472a1d6-2acc-4847-94d9-3d88410f9869_536x320.png)

To maintain the principle of least privilege, assign Global Admin sparingly. Instead, KASM supports granularly adding only the specific permissions you may need. So, instead of assigning all of the rights, start with none and build up from there. A [list of all permissions can be found here](https://kasmweb.com/docs/latest/guide/groups.html#group-permissions). By default, unless a user is added to a group with elevated permissions, they will be automatically assigned to the “All Users” group that is provided with only user-level Workspace access.

## Custom Workspace Groups

To further configure KASM for different groups, you can additionally create custom workspaces that only feature specific containers. For example, if you have an IT Admins group, it may have tools available like Nessus, Kali, or Maltego that you may not want every user to have access to. To tailor available apps in a group, simply go to Access Management → Groups → Select the Group → Click on the Workspaces tab, and click **+Add Workspaces.** Note that it will only allow you to choose from Workspaces that have already been installed from the registry.

[![](https://substackcdn.com/image/fetch/$s_!X_Yh!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e46d3af-1fc9-406b-815e-10bfcc73d694_872x552.png)](https://substackcdn.com/image/fetch/$s_!X_Yh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6e46d3af-1fc9-406b-815e-10bfcc73d694_872x552.png)

Generally, I don’t provide any tools in the default All Users group. Instead, to help make sure role-based assignments are maintained, apps are only assigned to groups that are validated against Entra groups.

## For Example…

In case the previous sections got a little muddy, let’s walk through setting up a Kasm group. The Entra security group I want to use is called “Lombardo Test User Group” and has a group Object ID that is like a9088……….35902. It has the members in it that I want to deploy Kali Linux to.

Step 1: Copy the Object ID from the security group in Azure

[![](https://substackcdn.com/image/fetch/$s_!Vv2c!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e975961-d57e-4422-8036-30d8289cf0c4_632x564.png)](https://substackcdn.com/image/fetch/$s_!Vv2c!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e975961-d57e-4422-8036-30d8289cf0c4_632x564.png)

Step 2: In KASM, go to Access Management → Groups → Add Group. On the Create Group page, name the group, and give it a priority that’s less than the priority of your All Users group (1000 by default). The logic here is Match First not Match All… so if a user belongs to multiple groups, they will be assigned to the group that has the lowest priority number. Click Save.

[![](https://substackcdn.com/image/fetch/$s_!SLnu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0e6538e-f3f0-4e75-8799-03f4b4ed4476_1329x664.png)](https://substackcdn.com/image/fetch/$s_!SLnu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb0e6538e-f3f0-4e75-8799-03f4b4ed4476_1329x664.png)

Step 3: In the new group, click on the SSO Group Mappings tab and click +Add SSO Mapping

[![](https://substackcdn.com/image/fetch/$s_!l15y!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9ee9427-9e56-4974-ab9d-2217983f9714_905x504.png)](https://substackcdn.com/image/fetch/$s_!l15y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb9ee9427-9e56-4974-ab9d-2217983f9714_905x504.png)

Step 4: Select the OID SSO Provider we previously set up, and paste the Group’s Object ID number from Entra in the **Group Attributes** box. Click Submit.

[![](https://substackcdn.com/image/fetch/$s_!g_ES!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff98cf980-5ed7-42d5-9fbb-4807aa605a6c_533x510.png)](https://substackcdn.com/image/fetch/$s_!g_ES!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff98cf980-5ed7-42d5-9fbb-4807aa605a6c_533x510.png)

Step 5: Back on the Groups page, click the Edit icon:

[![](https://substackcdn.com/image/fetch/$s_!PMjQ!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72badb72-f755-4167-85af-5fcd10c98cef_1355x591.png)](https://substackcdn.com/image/fetch/$s_!PMjQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F72badb72-f755-4167-85af-5fcd10c98cef_1355x591.png)

Step 6: Click on Workspace → +Add Workspaces → Select the Kali workspace and click submit.

[![](https://substackcdn.com/image/fetch/$s_!2Vrs!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50bb16db-e217-41dd-9f85-2ad3cc77e2d9_904x607.png)](https://substackcdn.com/image/fetch/$s_!2Vrs!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F50bb16db-e217-41dd-9f85-2ad3cc77e2d9_904x607.png)

Voila! Now anyone assigned to the Lombardo Test Group in Entra will have access to the Kali container in KASM. If the user is already signed in to a session, they will need to log out and back in.

[![](https://substackcdn.com/image/fetch/$s_!WfYX!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1f42128-0afa-4ccd-bcb4-6ed81d74019a_702x472.png)](https://substackcdn.com/image/fetch/$s_!WfYX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe1f42128-0afa-4ccd-bcb4-6ed81d74019a_702x472.png)

In contrast, if someone logs in who is a member of the IT Admin group, they’ll have the option to choose between Admin panel and Workspaces, and they will have access to both assigned workspaces, Kali and Edge:

[![](https://substackcdn.com/image/fetch/$s_!eriV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49dca9e8-41a3-49b2-87d9-a19f1ae918b3_950x572.png)](https://substackcdn.com/image/fetch/$s_!eriV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F49dca9e8-41a3-49b2-87d9-a19f1ae918b3_950x572.png)
