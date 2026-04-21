---
title: "Teams Security Baselines: Protected Links"
subtitle: "Spending 10 minutes or less will help your M365 environment be a little more secure"
date: 2023-07-06
author: Andy Lombardo
source: https://www.edtechirl.com/p/teams-security-baselines-protected
---

# Teams Security Baselines: Protected Links

*Spending 10 minutes or less will help your M365 environment be a little more secure*

[![](https://substackcdn.com/image/fetch/$s_!C4NW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20a690ab-c1ee-429c-b602-3ca5076cf8e0_800x500.png)](https://substackcdn.com/image/fetch/$s_!C4NW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F20a690ab-c1ee-429c-b602-3ca5076cf8e0_800x500.png)

In Oct. 2022, CISA released a document called [Microsoft Teams: M365 Minimum Viable Secure Configuration Baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf). This document outlines 13 steps to take to raise your Microsoft Teams environment to a minimum viable security posture. In this series, we’ll take a look at these 13 steps over a series of articles.

# Baseline 13: Protected Links

This baseline reads “Link Protection SHOULD Be Enabled.”

## What is it?

To help protect against users clicking on malicious links, Microsoft Defender can be set to alter URLs to proxy them through a scanning service to check to see if the domain is on a block list or lists of other malicious sites. If the link points to a file, the file is scanned. After passing all the checks, the user is redirected back to the original URL.

## Why is it bad?

Phishing is one of the most common attack vectors, and the use of malicious links is the primary tactic.

## What should you know before enforcement?

Link scanning for Teams is configured outside of Teams in the Microsoft Security Center/Microsoft Defender portal at security.microsoft.com.

## How do you enforce it?

Login to Microsoft Defender at security.microsoft.com and navigate to Email and collaboration —> Policies and rules. Select Threat policies —> Policies —> Safe links. Create a Safe Links policy (or edit an existing policy if this has already been configured).

Walk through the Safe Links policy wizard. For Teams specifically, there is one toggle for turning Safe Links on for Teams. While outside the scope of this article, you can also set up Safe Links for Exchange and O365 from this same wizard.

[![](https://substackcdn.com/image/fetch/$s_!427w!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cc41e8a-a15e-4bf0-938b-9e3e902ac6b0_698x691.png)](https://substackcdn.com/image/fetch/$s_!427w!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6cc41e8a-a15e-4bf0-938b-9e3e902ac6b0_698x691.png)

## Resources

[Defender for Office 365 Minimum Viable Secure Configuration Baseline (cisa.gov)](https://www.cisa.gov/sites/default/files/publications/Microsoft%20365%20Defender%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf)

[Safe Links in Microsoft Defender for Office 365 | Microsoft Docs](https://docs.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links?view=o365-worldwide)

[Set up Safe Links policies in Microsoft Defender for Office 365 | Microsoft Doc](https://learn.microsoft.com/en-us/microsoft-365/security/office-365-security/safe-links-policies-configure?view=o365-worldwide)

Note: The articles in the Security Baselines series aren’t being sent via the subscriber emails. Once the series is complete, I’ll be publishing a single article with links to all of the articles in the series.
