---
title: "Teams Security Baselines: Approved Apps"
subtitle: "Spending 10 minutes or less will help your M365 environment be a little more secure"
date: 2023-07-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/teams-security-baselines-approved
---

# Teams Security Baselines: Approved Apps

*Spending 10 minutes or less will help your M365 environment be a little more secure*

[![](https://substackcdn.com/image/fetch/$s_!LyKR!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff458ae6c-0dea-4cb2-8cfa-966985b3b9d1_800x500.png)](https://substackcdn.com/image/fetch/$s_!LyKR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff458ae6c-0dea-4cb2-8cfa-966985b3b9d1_800x500.png)

In Oct. 2022, CISA released a document called [Microsoft Teams: M365 Minimum Viable Secure Configuration Baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf). This document outlines 13 steps to take to raise your Microsoft Teams environment to a minimum viable security posture. In this series, we’ll take a look at these 13 steps over a series of articles.

# Baseline 8: Approved Apps

This baseline reads “Only approved apps SHOULD be installed.”

## What is it?

There are 3 types of apps that can be integrated with Teams: Microsoft-published apps, Third-party apps, and Custom apps.

## Why is it bad?

Third-party apps and Custom apps carry a risk that they could be malicious. Any allowed third-party or custom app should be appropriately vetted.

## What should you know before enforcement?

In general, your app policies should be set to allow Microsoft-published apps and block third-party of custom apps. Your organization should also set up policies to review apps for approval, and custom allow any needed third-party or custom apps on a case-by-case basis.

## How do you enforce it?

Login to the Teams Admin Center (teams.cmd.ms) and navigate to **Teams apps**—> **Permission Policies**.

Select the **Global (Org-wide default) policy** and set the configuration to the appropriate sharing settings for your Organization. In general, this should be as follows:

**Microsoft Apps:** Either Allow all apps or Block specific apps and allow all others

**Third-party apps:** Either Block all apps or Allow specific apps and block all others

**Custom apps:** Block all apps, unless you have a specific custom app need.

[![](https://substackcdn.com/image/fetch/$s_!U4BI!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f25eef7-7235-4874-a718-03bbf70ed76b_585x530.png)](https://substackcdn.com/image/fetch/$s_!U4BI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6f25eef7-7235-4874-a718-03bbf70ed76b_585x530.png)

Note that if you choose one of the specific allow or specific deny options that you’ll need to indicate those apps in the policy before you can save it.

If you have additional policies created besides your Global (org-wide default) policy, you’ll need to repeat the above steps for each separate policy.

## Resources:

[Manage Teams Permission Policies](https://docs.microsoft.com/en-us/microsoftteams/teams-app-permission-policies)

[Upload Your App in Microsoft Teams](https://docs.microsoft.com/en-us/microsoftteams/platform/concepts/deploy-and-publish/apps-upload)

Note: The articles in the Security Baselines series aren’t being sent via the subscriber emails. Once the series is complete, I’ll be publishing a single article with links to all of the articles in the series.
