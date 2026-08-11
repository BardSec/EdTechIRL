---
title: "Teams Security Baselines: Unmanaged User Access"
subtitle: "Spending 10 minutes or less will help your M365 environment be a little more secure"
date: 2023-07-03
author: Andy Lombardo
source: https://www.edtechirl.com/p/teams-security-baselines-unmanaged
---

# Teams Security Baselines: Unmanaged User Access

*Spending 10 minutes or less will help your M365 environment be a little more secure*

[![](https://substackcdn.com/image/fetch/$s_!neHu!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F622403c6-4f01-4177-9d6e-1498ef5ab850_800x500.png)](https://substackcdn.com/image/fetch/$s_!neHu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F622403c6-4f01-4177-9d6e-1498ef5ab850_800x500.png)

In Oct. 2022, CISA released a document called [Microsoft Teams: M365 Minimum Viable Secure Configuration Baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf). This document outlines 13 steps to take to raise your Microsoft Teams environment to a minimum viable security posture. In this series, we’ll take a look at these 13 steps over a series of articles.

# Baseline 5: Unmanaged User Access

This baseline reads “Unmanaged user access SHALL be restricted.”

## What is it?

Unmanaged user access refers to users outside of your tenant who do not have an organizationally managed Microsoft identity. By default, they have the ability to find, call, and chat with people who have managed Microsoft identities.

## Why is it bad?

When unmanaged user access is unrestricted, they are able to look up internal users and initiate chats and calls within Teams, which carries a high risk for phishing and social engineering.

## What should you know before enforcement?

In legitimate use cases where you want to allow this ability for unmanaged users, it’s best to limit their ability to initiate contact and only allow the ability for internal users to initiate contact if necessary. The concern in a K-12 setting is that if you’re using Teams to hold meetings with parents or other stakeholders who don’t have accounts in the tenant, you may restrict legitimate access needs. To ensure that these users can still join a Teams call, anonymous join should be enabled.

## How do you enforce it?

Login to the Teams Admin Center (teams.cmd.ms) and navigate to Users —> External Access and scroll down to “Teams accounts not managed by an organization.” They’re not labeled as such, but you will have three options to choose from:

### Two- way communication

*No restrictions on communication between internal users and external unmanaged users*

Two-way communication is not recommended, so if your settings look like the settings below, they should be reconfigured.

[![](https://substackcdn.com/image/fetch/$s_!XX1U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5834afb6-057a-4f2c-bc8d-fc2842a163bf_797x247.png)](https://substackcdn.com/image/fetch/$s_!XX1U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5834afb6-057a-4f2c-bc8d-fc2842a163bf_797x247.png)

### One-way communication

*Can be initiated by an internal user to an external unmanaged user*

This security baseline recommends that this setting should not be enabled, but can be to support a legitimate use case. To allow one-way communication initiated by your internal users, under “Teams accounts not managed by an organization,” set the toggle for “People in my org can communicate with Teams users whose accounts aren’t managed by an organization” to ON, but leave the “External users with Teams accounts not managed by an organization can contact users in my organization” unchecked like below:

[![](https://substackcdn.com/image/fetch/$s_!3E_B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e3ea2a5-3d8e-42d4-bef7-37b2693fe832_778x245.png)](https://substackcdn.com/image/fetch/$s_!3E_B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0e3ea2a5-3d8e-42d4-bef7-37b2693fe832_778x245.png)

### No-way communication

*Internal users and unmanaged users cannot communicate*

This is the recommended and most secure option. To disallow communication between your internal users and external unmanaged users, under “Teams accounts not managed by an organization,” set the toggle for “People in my org can communicate with Teams users whose accounts aren’t managed by an organization” to OFF like below:

[![](https://substackcdn.com/image/fetch/$s_!dAJa!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4554858-c09a-44c0-9005-b65a5b20e880_760x137.png)](https://substackcdn.com/image/fetch/$s_!dAJa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe4554858-c09a-44c0-9005-b65a5b20e880_760x137.png)

## Resources:

[Manage external meetings and chat with people and organizations using Microsoft identities - Microsoft Teams | Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/trusted-organizations-external-meetings-chat?tabs=organization-settings)

[Teams settings and policies reference - Microsoft Teams | Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/settings-policies-reference#allow-anonymous-users-to-join-meetings)

[Use guest access and external access to collaborate with people outside your organization - Microsoft Teams | Microsoft Learn](https://learn.microsoft.com/en-us/microsoftteams/communicate-with-users-from-other-organizations)

Note: The articles in the Security Baselines series aren’t being sent via the subscriber emails. Once the series is complete, I’ll be publishing a single article with links to all of the articles in the series.
