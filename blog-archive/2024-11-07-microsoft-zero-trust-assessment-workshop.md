---
title: "Microsoft Zero Trust Assessment Workshop"
subtitle: "Robustly analyze my tenant's security posture from a Zero Trust POV in 5 minutes? Yes, please!"
date: 2024-11-07
author: Andy Lombardo
source: https://www.edtechirl.com/p/microsoft-zero-trust-assessment-workshop
---

# Microsoft Zero Trust Assessment Workshop

*Robustly analyze my tenant's security posture from a Zero Trust POV in 5 minutes? Yes, please!*

[![A vibrant, detailed illustration depicting the concept of performing a self-assessment. A person sits at a desk with a checklist, mirror, or computer screen showing self-reflective questions or metrics. They are thoughtfully examining the list or data, perhaps with indicators or markers showing areas for improvement and strengths. The setting is bright, organized, and encouraging, with symbols of growth (like plants or upward arrows) around them, emphasizing introspection and self-evaluation. The style is friendly and motivating, as if in an educational or productivity guide.](https://substackcdn.com/image/fetch/$s_!LOVW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed137dc1-1e16-483a-abef-8e76899adf0b_1024x1024.webp "A vibrant, detailed illustration depicting the concept of performing a self-assessment. A person sits at a desk with a checklist, mirror, or computer screen showing self-reflective questions or metrics. They are thoughtfully examining the list or data, perhaps with indicators or markers showing areas for improvement and strengths. The setting is bright, organized, and encouraging, with symbols of growth (like plants or upward arrows) around them, emphasizing introspection and self-evaluation. The style is friendly and motivating, as if in an educational or productivity guide.")](https://substackcdn.com/image/fetch/$s_!LOVW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fed137dc1-1e16-483a-abef-8e76899adf0b_1024x1024.webp)

Microsoft recently launched a new community project for Zero Trust Workshops / Zero Trust Assessments that can be run against your environment to provide you with a list of configurations that you can use to guide you in implementing Zero Trust controls. Though a lot of people hear “Zero Trust” and automatically relegate it to Buzz Word status (thank you, cyber marketing teams), Zero Trust is a concept that really deserves to be at the center of your security strategy. This Workshop / Assessment tool is free and open to everyone to run on your own in your tenant.

## What’s Involved

Essentially, there are two parts to this tool. First, there is a Zero Trust Assessment Tool that is a PowerShell Module. When you run the assessment, the tool creates an Excel file with its findings. Second, there is a framework for a Zero Trust Workshop. The Zero Trust Workshop guides users in creating a structured, actionable strategy to establish a secure Zero Trust approach. The workshop’s goal is to assist users in identifying key projects and initiatives that will enhance their Microsoft security posture. Currently, three workshops are offered, focusing on the pillars of Identity, Devices, and Data, with future pillars of Apps, Infrastructure, and Network coming online later. As a framework, you can choose to run all or only some workshops, based on your priorities and available resources. When planning your workshop, there is a [Workshop Delivery Guide](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance/delivery-guide) available that includes a description of applicable stakeholders, engagement model, and time constraints. There are several options for running these workshops: you can request Microsoft to conduct them (by contacting your Microsoft representative), collaborate with Microsoft Partners who are trained to lead the workshops, or run them as a self-assessment if you have in-house expertise. Each pillar-focused workshop typically lasts about two hours, and the initial release covers the three core areas: Identity, Device, and Data.

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.

## The Output

We’ll do a step-by-step of how to install and run the Assessment Tool at the end of this article, but first let’s look at what the tool provides for you. After running the tool, you’ll be provided with a locally-saved Excel document with the findings from the assessment. The spreadsheet will be broken out in the following areas:

### Home Tab

On the home tab of the document, you’ll see an overview of your Zero Trust posture divided into pillars for Identity, Device, Data, Apps, Infrastructure, and Network. Right now, the Identity, Device, and Data pillars are active in the workshop, and the tool assesses the Identity and Device pillars. The additional pillars are slated for future rollout. On this dashboard, areas are measured as **Not Deployed**, **Partially Deployed**, or **Fully Deployed** (or, in the case of the future pillars, **Not Evaluated**).

[![](https://substackcdn.com/image/fetch/$s_!JGGH!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a7723ed-036e-424f-91cd-89f3cc79d58b_1013x909.png)](https://substackcdn.com/image/fetch/$s_!JGGH!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9a7723ed-036e-424f-91cd-89f3cc79d58b_1013x909.png)

### Roadmaps

The next three tabs in the Excel document are the Roadmaps for Identity, Devices, and Data. These are intended for use in the Zero Trust Workshop. In short, these are a roadmap for implementation of Zero Trust controls in each of these pillars. Within each one, they are further subdivided into domains. The Identity Pillar, for example, includes sub-categories for Apps, Users and Groups, Devices, and Operations. Within each of these categories, you’re provided with projects to complete that will move you closer to a Zero Trust configuration. Each item is also linked to [Microsoft Zero Trust Workshop Documentation](https://microsoft.github.io/zerotrustassessment/docs/intro) on that configuration.

[![](https://substackcdn.com/image/fetch/$s_!OTMK!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7dc79b6-4979-4355-bb5c-32cc580f872e_1607x761.png)](https://substackcdn.com/image/fetch/$s_!OTMK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd7dc79b6-4979-4355-bb5c-32cc580f872e_1607x761.png)

When evaluating where your organization is in the process, each of the project cards in the roadmap can be assigned a status, ranging from **Not Started** to **Completed**.

[![](https://substackcdn.com/image/fetch/$s_!gKON!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5cf5c8a-7f88-450f-9255-4a831c29ff6d_1038x790.png)](https://substackcdn.com/image/fetch/$s_!gKON!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe5cf5c8a-7f88-450f-9255-4a831c29ff6d_1038x790.png)

Above are the full list of statuses and descriptions provided in the [Workshop documentation from Microsoft](https://microsoft.github.io/zerotrustassessment/docs/workshop-guidance).

### Config Tabs

The next two tabs for Identity Config and Device Config provide details on your tenant’s current configuration. In my example, these sheets are pretty scant on details, which may be a result of this being a test tenant without a lot of setup.

[![](https://substackcdn.com/image/fetch/$s_!xy_U!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fb75454-58b8-4221-a81c-396145d714bd_1248x883.png)](https://substackcdn.com/image/fetch/$s_!xy_U!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fb75454-58b8-4221-a81c-396145d714bd_1248x883.png)

Once some of these configurations are present, you’ll see some pretty granular information and details about specific policies and settings, like the sample below taken from [one of the project’s documentation videos](https://microsoft.github.io/zerotrustassessment/docs/videos).

[![](https://substackcdn.com/image/fetch/$s_!Qe1l!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F705aad1e-fdfe-4e90-8a28-19aaf657141f_994x319.png)](https://substackcdn.com/image/fetch/$s_!Qe1l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F705aad1e-fdfe-4e90-8a28-19aaf657141f_994x319.png)

### Assessment Tabs

The Assessment Tabs are the part of this project that I’m currently geeking-out over. I enjoy doing my own research and developing policies and planning activities to improve my organization’s security posture, but being on a small team and wearing many hats can make that difficult. I find a lot of value in tools that can evaluate my security posture against best practices and provide me with very detailed, prescriptive remediations. The assessment tab does exactly that, letting you see actionable steps you can take to improve your environment. Additionally, it provides details on user impact and risk level, letting you prioritize how you want to attack the deficiencies. A great way to start is by hitting things that are **Low User Impact** and **High** or **Moderate Risk**. This provides the most bang for your buck in speedy implementation and low likelihood of introducing problems for users. When prioritizing what items to remediate, it’s also notable in the Results column that there is a prioritization scale from **P0-P2**. **P0** are the highest priorities, and **P2** are the lowest priorities.

[![](https://substackcdn.com/image/fetch/$s_!s9mb!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff372b155-b02e-4ee3-850c-a0c26ac36d54_1129x602.png)](https://substackcdn.com/image/fetch/$s_!s9mb!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff372b155-b02e-4ee3-850c-a0c26ac36d54_1129x602.png)

It’s also helpful that each of the lines of results is linked to a card with additional information. For example, the “Workload Identities authentication methods” line from the image above links to the card below:

[![](https://substackcdn.com/image/fetch/$s_!N3ex!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F472d9ec2-4341-437c-a528-696093be2144_843x286.png)](https://substackcdn.com/image/fetch/$s_!N3ex!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F472d9ec2-4341-437c-a528-696093be2144_843x286.png)

This helps you to see at a glance a description of the configuration, what the priority level is (P0=highest), the type of threat this presents, remediation needed, remediation impact, and a link to documentation to learn more.

## How to Run It

#### Prerequisite

Note, you need to be using PowerShell ver. 7.0 or greater. To check your PowerShell version, you can run the command

```
$PSVersionTable
```

If you need to install PowerShell 7+, you can install with winget:

```
winget install Microsoft.Powershell
```

It’s worth mentioning that since this tool runs on PowerShell 7, it’s truly cross-platform and can run the same way on Windows, Mac, and Linux.

#### Installing the Zero Trust Assessment Module

To install the Zero Trust Assessment tool, run this PowerShell command:

```
Install-Module ZeroTrustAssessment
```

then,

```
Invoke-ZTAssessment
```

You’ll then be prompted to sign in to Microsoft. Once you sign in, the Zero Trust Assessment will begin.

[![](https://substackcdn.com/image/fetch/$s_!mbuo!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d1fe5d1-58a5-49cb-8e3a-3af4e6ddc659_486x79.png)](https://substackcdn.com/image/fetch/$s_!mbuo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4d1fe5d1-58a5-49cb-8e3a-3af4e6ddc659_486x79.png)

Once the assessment completes (less than 5 minutes when I ran it), you’ll be directed to a locally-saved Excel file with the results.

And just like that, you’re one step farther along the journey to Zero Trust.

## Resources:

[Introduction | Microsoft Zero Trust Workshop](https://microsoft.github.io/zerotrustassessment/docs/intro)

[Zero Trust Guidance Center | Microsoft Learn](https://learn.microsoft.com/en-us/security/zero-trust/)

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.
