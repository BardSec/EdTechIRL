---
title: "Teams Security Baselines: Teams Email Integration"
subtitle: "Spending 10 minutes or less will help your M365 environment be a little more secure"
date: 2023-07-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/teams-security-baselines-teams-email
---

# Teams Security Baselines: Teams Email Integration

*Spending 10 minutes or less will help your M365 environment be a little more secure*

[![](https://substackcdn.com/image/fetch/$s_!7j3x!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff452203d-0be8-488d-b74c-6cd8355e383a_800x500.png)](https://substackcdn.com/image/fetch/$s_!7j3x!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff452203d-0be8-488d-b74c-6cd8355e383a_800x500.png)

In Oct. 2022, CISA released a document called [Microsoft Teams: M365 Minimum Viable Secure Configuration Baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf). This document outlines 13 steps to take to raise your Microsoft Teams environment to a minimum viable security posture. In this series, we’ll take a look at these 13 steps over a series of articles.

# Baseline 7: Teams Email Integration

This baseline reads “Teams Email Integration SHALL be disabled.”

## What is it?

Teams has the option of giving a channel it’s own email address. The catch is that the email address isn’t addressed with your tenant’s domain, but rather with a Microsoft-owned domain - teams.ms.

## Why is it bad?

Because the email isn’t part of your tenant, it’s not subject to the same security policies as are used in your tenant. It can also be exploited for phishing and social engineering. For example, an attacker could create a Teams channel with a name that looks like it should be in your organization, but they don’t have to spoof or typosquat your domain. If your users are used to getting emails from teams.ms, they may not think critically about the email’s origin.

## What should you know before enforcement?

If users are already utilizing this feature, it would be wise to communicate the change in advance to limit disruptions.

## How do you enforce it?

Login to the Teams Admin Center (teams.cmd.ms) and navigate to Teams —> Teams Settings and scroll down to Email integration. Set the toggle for “Users can send emails to a channel email address” to OFF.

[![](https://substackcdn.com/image/fetch/$s_!f-N0!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0baffc66-6c3b-4072-83aa-df7c4240ff1d_854x169.png)](https://substackcdn.com/image/fetch/$s_!f-N0!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0baffc66-6c3b-4072-83aa-df7c4240ff1d_854x169.png)

### 

## Resources:

[Manage and Monitor Teams - Email Integration](https://learn.microsoft.com/en-us/microsoftteams/manage-teams-overview#email-integration)

Note: The articles in the Security Baselines series aren’t being sent via the subscriber emails. Once the series is complete, I’ll be publishing a single article with links to all of the articles in the series.
