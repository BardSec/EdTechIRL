---
title: "Teams Security Baselines: Data Loss Prevention"
subtitle: "Spending 10 minutes or less will help your M365 environment be a little more secure"
date: 2023-07-06
author: Andy Lombardo
source: https://www.edtechirl.com/p/teams-security-baselines-data-loss
---

# Teams Security Baselines: Data Loss Prevention

*Spending 10 minutes or less will help your M365 environment be a little more secure*

[![](https://substackcdn.com/image/fetch/$s_!cjlS!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f0f391e-6255-4082-acb0-f0135c35f351_800x500.png)](https://substackcdn.com/image/fetch/$s_!cjlS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0f0f391e-6255-4082-acb0-f0135c35f351_800x500.png)

In Oct. 2022, CISA released a document called [Microsoft Teams: M365 Minimum Viable Secure Configuration Baseline](https://www.cisa.gov/sites/default/files/publications/Microsoft%20Teams%20M365%20Minimum%20Viable%20SCB%20Draft%20v0.1.pdf). This document outlines 13 steps to take to raise your Microsoft Teams environment to a minimum viable security posture. In this series, we’ll take a look at these 13 steps over a series of articles.

# Baseline 11: Data Loss Prevention

This baseline reads “Data Loss Prevention Solutions SHALL Be Enabled.”

## What is it?

Data Loss Prevention (DLP) refers to data leakage, either intentional or unintentional. Microsoft offers DLP services that can be accessed in the M365 compliance admin center. There are 3rd party DLP providers, as well.

## Why is it bad?

Any data leakage of sensitive information, whether intentional or unintentional, should be seen as a danger.

## What should you know before enforcement?

At a minimum, the sharing of credit card numbers, taxpayer ID numbers, and Social Security Numbers should be restricted.

## How do you enforce it?

DLP isn’t configured inside of Teams, but rather through the M365 compliance center at compliance.microsoft.com, then Policies —> Data Loss Prevention —> Policies. If you have current DLP policies configured, ensure that Teams has been added as a data source like below.

[![](https://substackcdn.com/image/fetch/$s_!02EE!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52e25e88-3c34-411f-81c7-e57b31ad1719_1211x687.png)](https://substackcdn.com/image/fetch/$s_!02EE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52e25e88-3c34-411f-81c7-e57b31ad1719_1211x687.png)

If you do not have any DLP policies configured, setting up a DLP policy is beyond the scope of this article, but in general will involve creating a policy from compliance.microsoft.com, then Policies —> Data Loss Prevention —> Policies —> + Create Policy. When setting up the policy, a wizard will walk you through selecting which data you would like to protect, and which MS products you’d like to use as protected data sources.

## 

Note: The articles in the Security Baselines series aren’t being sent via the subscriber emails. Once the series is complete, I’ll be publishing a single article with links to all of the articles in the series.
