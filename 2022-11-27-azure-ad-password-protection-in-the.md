---
title: "Azure AD Password Protection in the Cloud and On-Prem"
date: 2022-11-27
author: Andy Lombardo
source: https://www.edtechirl.com/p/azure-ad-password-protection-in-the
---

# Azure AD Password Protection in the Cloud and On-Prem

[![](https://substackcdn.com/image/fetch/$s_!cRVt!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3b8fddd-5945-431a-ac61-d93c4e2c4379_1024x1024.png)](https://substackcdn.com/image/fetch/$s_!cRVt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fb3b8fddd-5945-431a-ac61-d93c4e2c4379_1024x1024.png)

So you have password history and complexity rules set up, but you know your users are using common, weak, or breached passwords. How do you tighten up those passwords?

In the cloud, there is a service called Azure Active Directory Password Protection. With AAD Password Protection, Microsoft maintains a Global Banned Words list. This list contains known common passwords and passwords that have been part of data breaches. Additionally, there is an option to create a custom word list of up to 1000 words. For the custom word list, it’s a good idea to enter common words in your community - sports team, organization name, mascots, etc. AAD Password Protection will check any new passwords in your environment against this global list and the custom list, plus it will automatically check for variations of words on your custom list (i.e., if you add Nashville to your list, it will check for Nashville, N@shville, n@shv1ll3, and other common substitutions). For cloud-only accounts, configuration is super simple: it’s just a dashboard in Azure under AAD —> Authentication Methods —> Password Protection:

[![](https://substackcdn.com/image/fetch/$s_!vb40!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc03c14aa-a34c-4b60-b616-65993433d01b_1329x903.png)](https://substackcdn.com/image/fetch/$s_!vb40!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fc03c14aa-a34c-4b60-b616-65993433d01b_1329x903.png)

To enforce AAD Password Protection on-prem, however, requires a little more setup and configuration than just toggling “Enable password protection on Windows Server Active Directory” to YES.

**What’s needed to connect AAD Password Protection to on-prem AD?**

1. At least 1 writeable domain controller per forest running the Azure AD Password Protection DC Agent
2. At least 1 Windows server 2012R2 or newer running the Azure AD Password Protection Proxy Agent
3. An Azure Global Admin account for 1-time configuration
4. AAD P1 or P2 license

I’ll link more specific step by step instructions at the end, but the basic process is that you need to connect your on-prem Active Directory environment to your Azure Active Directory environment. However, you don’t want to directly expose your domain controller to the internet to make that connection, so you’ll need a server to serve as a proxy between AD and AAD.

Once the DC agent and the Proxy agent are installed, the proxy services and the domain forest are registered with Azure via PowerShell and the AzureADPasswordProtection module.

After everything is configured, the agent on the DC will make an hourly call to the proxy server and request a new copy of the password policy with both the global and the custom banned word lists. After the lists are on the DC, they will replicate to the other controllers. Whenever a user initiates a password change, the new password will be evaluated against the most recent password policy. If the password policy is in audit mode, even if the password fails the policy, it will still be allowed. It’s a good idea to evaluate the policy in Audit mode to make sure it behaves as expected prior to moving to enforcement.

To check the results of audit mode, you’ll go to the DC with the installed agent and check out the event log (Event Viewer —> Applications and Services Logs —> Microsoft —> AzureADPasswordProtection —> ProxyService). The event logs will also log communication between the Proxy and the DC Agent, and can be used for troubleshooting to make sure you are set up and configured correctly.

It’s important to note that these password policies are not retroactive - the policies are only evaluated during the password change process. If you wanted to evaluate all of your current user passwords, you would need to conduct a mass password reset in your environment.

There are several moving pieces at play with this setup, but once configured, on-going maintenance is minimal and mostly consists of updating your banned word list in Azure AD.

***Resources:***

[Eliminate bad passwords using Azure Active Directory Password Protection](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad)

[Step-by-step Instructions](https://techcommunity.microsoft.com/t5/itops-talk-blog/step-by-step-implementing-azure-ad-password-protection-on/ba-p/563342)

[Plan and Deploy AAD Password Protection Microsoft Documentation](https://learn.microsoft.com/en-us/azure/active-directory/authentication/howto-password-ban-bad-on-premises-deploy)

[AAD Password Protection Design Principles](https://learn.microsoft.com/en-us/azure/active-directory/authentication/concept-password-ban-bad-on-premises#design-principlesunfortunately)
