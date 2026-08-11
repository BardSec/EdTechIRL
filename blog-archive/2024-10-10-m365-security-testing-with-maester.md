---
title: "M365 Security Testing with Maester"
subtitle: "Brain-meltingly simple security configuration audit for your tenant"
date: 2024-10-10
author: Andy Lombardo
source: https://www.edtechirl.com/p/m365-security-testing-with-maester
---

# M365 Security Testing with Maester

*Brain-meltingly simple security configuration audit for your tenant*

[![](https://substackcdn.com/image/fetch/$s_!aW2C!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f93dc5c-7dd9-4f14-bf7f-50d6a1727376_1024x1024.webp)](https://substackcdn.com/image/fetch/$s_!aW2C!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7f93dc5c-7dd9-4f14-bf7f-50d6a1727376_1024x1024.webp)

First off, if you do anything with Microsoft Entra, and specifically if you deal with Identity, you should keep track of Merill Fernando if you don’t already do so. His website is [here (merill.net)](https://merill.net/about/) and he puts out an [Entra News Substack (found here)](https://entra.news/) that should be required reading for folks in this space. I’ve done articles previously on some of his work like [cmd.ms (article here)](https://www.edtechirl.com/p/navigating-m365-admin-portals-in?r=ef58q) and [Conditional Access Analyer (here)](https://www.edtechirl.com/p/document-conditional-access-in-a)

One of his more recent tools (along with Faben Bader and Thomas Naunheim) is a Microsoft security test automation framework called Maester ([maester.dev](https://www.maester.dev)). I saw it a few months ago, but at first glance I was worried that it was going to take a ton of time to implement and tune and tweak, so I kept saving it for “when I have time.” Students and teachers are on Fall Break this week, so no time like the present, right? I settled down with a coffee and some background music and mentally prepared to dig through documentation. Ten minutes later, I’d already finished installation, completed my first Maester test, and was scrolling through test results 😲

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.

## TL;DR - What’s Maester Do?

At its most basic level, Maester gives you a quick snapshot of your tenant’s security posture as measured against security standards from Microsoft and CISA. The snapshot comes in the form of an interactive click-through report that lets you drill down to the details of each test, including configuration guidance and details on remediation. Beyond the basic level, Maester has the power to automate continuous testing and perform regression testing for validating changes to your tenant’s security configuration.

## Why Is this Important?

[Gartner predicts](https://www.gartner.com/smarterwithgartner/is-the-cloud-secure) that through 2025, 99% of cloud security failures will be “the customer’s fault” — the result of misconfigurations in their cloud environment. Maester is a tool that checks your tenant’s configuration against 140+ security baselines in SECONDS, helping point you to areas that need attention either through reconfiguration or implementation of mitigating controls.

## Output

Let’s start with what Maester gives you first, then we’ll work backwards to how to set it up.

After running Maester, you’ll receive an HTML file that will look like below:

[![](https://substackcdn.com/image/fetch/$s_!ekee!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74e320cc-5308-4f67-8f92-a36003e0428c_1272x1029.png)](https://substackcdn.com/image/fetch/$s_!ekee!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F74e320cc-5308-4f67-8f92-a36003e0428c_1272x1029.png)

### Test Summary

The Test Summary dashboard gives you an overview of how many tests were run, how many passed, how many failed, and how many weren’t tested for some reason. My 14 “Not tested” items were for some custom tests and tests that were designed for a tenant with different Microsoft licensing than what I have in my tenant. Like the Microsoft Secure Score, this test summary gives you a snapshot of how your Microsoft tenant security looks at a point in time. If you run this regularly, you can have an on-going snapshot of your security posture in this area, with the additional bonus that it’s all already documented in an easy to digest format.

[![](https://substackcdn.com/image/fetch/$s_!zatW!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcce497b9-62ce-446d-bbab-08afa0271491_1228x481.png)](https://substackcdn.com/image/fetch/$s_!zatW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcce497b9-62ce-446d-bbab-08afa0271491_1228x481.png)

### Test Details

In the Test Details section, there is a rundown of the tests that were run against your Microsoft environment:

[![](https://substackcdn.com/image/fetch/$s_!TaNv!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5001611a-a675-4d22-843f-6c40cd251aef_1235x641.png)](https://substackcdn.com/image/fetch/$s_!TaNv!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5001611a-a675-4d22-843f-6c40cd251aef_1235x641.png)

Out of the box, they’re from three different sources:

**Maester Tests:**

The tests with the prefix **MT** are tests that were created by the Maester community. These focus primarily on Conditional Access policy configuration. These are based on Microsoft recommendations, and they include references to Microsoft documentation.

**EIDSCA Tests:**

The tests with the prefix **EIDSCA** (like the screenshot above) are based on the [Entra ID Attack and Defense Playbook](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense), specifically the [Entra ID Security Config Analyzer (EIDSCA)](https://github.com/Cloud-Architekt/AzureAD-Attack-Defense/blob/main/AADSecurityConfigAnalyzer.md). The tests from this source have been mapped to the MITRE ATT&CK framework and are designed to verify that mitigations for common attack scenarios are in place.

**CISA SCUBA Tests:**

The tests with the prefix **MS** are based on the CISA Secure Cloud Business Applications (SCuBA) minimal viable security configuration baseline [documents](https://github.com/cisagov/ScubaGear/blob/main/baselines/README.md). To get a better idea about what the baselines look like, you can check out [my series of articles on the baselines for Teams](https://www.edtechirl.com/p/security-baselines-for-microsoft). The baseline document for Entra, Defender, and Exchange are priceless, **especially** if you’re at the beginning of your Microsoft hardening journey. I learned more from going through these configuration guides than from most of the M365 courses, books, and videos I’ve consummed.

The layout of the Test Details page is simple but powerful. At a glance, you can see the standard/control being assessed and whether it passed or failed. The power for using this tool for improvement comes in viewing the **Info** link for failed tests. Clicking on the info link provides a view like this:

[![](https://substackcdn.com/image/fetch/$s_!ew20!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36cfd351-4d47-4022-9eed-bd4b1d612833_722x949.png)](https://substackcdn.com/image/fetch/$s_!ew20!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F36cfd351-4d47-4022-9eed-bd4b1d612833_722x949.png)

The **Info** dialog window shows what configuration setting caused the test to fail, along with how the control should be configured to pass. There are links to documentation at both Maester.dev and Micrsoft to explain the control. The script or API query used for the test is also included. In short — it tells you what you need to change to pass the test.

## Setting Up Maester

Throughout the process you’ll be prompted a few times to sign in to your Microsoft/Azure account. Be sure to use the account for the tenant being tested. You’ll also be asked if you want to trust the source of these modules (you’ll say **yes** **to all**).

Open a Terminal session as Admin. Since Maester works through PowerShell, this can be done from a Windows, Mac, or Linux machine as long as PowerShell is installed.

Install the Pester PowerShell Module that Maester is built on:

> Install-Module Pester -SkipPublisherCheck -Force -Scope CurrentUser

Install the Maester PowerShell Module:

> Install-Module Maester -Scope CurrentUser

Install the Azure and Exchange modules needed to run all of the CISA tests. The AZ module may take a few minutes. For me, installing the Az module took longer than the rest of the entire process combined.

> Install-Module Az -Scope CurrentUser
>
> Install-Module ExchangeOnlineManagement -Scope CurrentUser

Create a directory for your Maester tests:

> md maester-tests

Move to that directory:

> cd maester-tests

Install Maester Tests:

> Install-MaesterTests

Connect to Maester for all of the services:

> Connect-Maester -Service All

Finally, start Maester with:

> Invoke-Maester

That’s it — a minute or two after the **Invoke-Maester** command, the report should be ready to view.

(For a more full explanation of the set up process, be sure to visit [Maester’s Installation Guide](https://maester.dev/docs/installation).)

## Next Steps:

[Automating Maester with Github Actions, Azure Automate, or Azure DevOps Pipeline: https://maester.dev/docs/monitoring/](https://maester.dev/docs/monitoring/)

[Set up Email Notifications for Test Results: https://maester.dev/docs/monitoring/email](https://maester.dev/docs/monitoring/email)

[Create Custom Tests: https://maester.dev/docs/writing-tests](https://maester.dev/docs/writing-tests)

[Conditional Access What-If Testing: https://maester.dev/docs/ca-what-if](https://maester.dev/docs/ca-what-if)

Thanks for reading EdTech IRL! Subscribe for free to receive new posts and support my work.
