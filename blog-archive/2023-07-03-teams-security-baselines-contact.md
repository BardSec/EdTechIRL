---
title: "Teams Security Baselines: Contact with Skype Users"
subtitle: "Spending 10 minutes or less will help your M365 environment be a little more secure"
date: 2023-07-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/teams-security-baselines-contact
---

# Teams Security Baselines: Contact with Skype Users

*Spending 10 minutes or less will help your M365 environment be a little more secure*

[![](https://substackcdn.com/image/fetch/$s_!k9h6!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10029b89-6a46-47b7-a485-c28d01721188_800x500.png)](https://substackcdn.com/image/fetch/$s_!k9h6!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F10029b89-6a46-47b7-a485-c28d01721188_800x500.png)

In Oct. 2022, CISA released a document called [Microsoft Teams: M365 Minimum Viable Secure Configuration Baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf). This document outlines 13 steps to take to raise your Microsoft Teams environment to a minimum viable security posture. In this series, we’ll take a look at these 13 steps over a series of articles.

# Baseline 6: Skype User Access

This baseline reads “Contact with Skype Users SHALL be Blocked.”

## What is it?

Skype for Business was retired in July 2021 and is no longer supported by Microsoft.

## Why is it bad?

While not inherently bad, the limitations and degraded user experience due to Skype’s deprecation, coupled with the lack of support from Microsoft, could lead to issues.

## What should you know before enforcement?

Users who are still using Skype for Business should already have the option of using Teams, which has more available features and support, so leaving Skype for Business is a win-win.

## How do you enforce it?

Login to the Teams Admin Center (teams.cmd.ms) and navigate to Users —> External Access and scroll down to “Skype Users.” Set the toggle for “Allow users in my organization to communicate with Skype users” to OFF.

[![](https://substackcdn.com/image/fetch/$s_!rr1M!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fa02bda-64b7-4346-b3a3-c5ec9f0f9558_437x152.png)](https://substackcdn.com/image/fetch/$s_!rr1M!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0fa02bda-64b7-4346-b3a3-c5ec9f0f9558_437x152.png)

### 

## Resources:

[Communicate with Skype Users | Microsoft Docs](https://docs.microsoft.com/en-us/microsoftteams/manage-external-access#communicate-with-skype-users)

[Skype for Business Online to Be Retired in 2021 | Microsoft Teams Blog](https://techcommunity.microsoft.com/t5/microsoft-teams-blog/skype-for-business-online-to-be-retired-in-2021/ba-p/777833)

Note: The articles in the Security Baselines series aren’t being sent via the subscriber emails. Once the series is complete, I’ll be publishing a single article with links to all of the articles in the series.
