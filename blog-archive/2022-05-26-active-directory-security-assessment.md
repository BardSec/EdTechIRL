---
title: "Active Directory Security Assessment on a Budget"
date: 2022-05-26
author: Andy Lombardo
source: https://www.edtechirl.com/p/active-directory-security-assessment
---

# Active Directory Security Assessment on a Budget

[![](images/9f7bfdf9-e037-4254-a76a-3c1a338bdc87_720x356.png)](images/9f7bfdf9-e037-4254-a76a-3c1a338bdc87_720x356.png)

Reviewing Active Directory auditing tools can be painful. You know there are baselines you need to check, and you know that you can technically do the job for free with PowerShell, but the time it takes to develop and run the scripts, analyze the results, and generate any kind of actionable report is wholly unrealistic, especially if you’re part of a skeleton IT crew in a K-12 environment. Vendors know this, and they price AD audit tools accordingly. Most tools I’ve looked at in this area are just a graphical front end for a PowerShell backend, and for my size institution quotes usually run between $2-$5/AD account per year, which doesn’t sound that bad till you figure in the thousands and thousands of student user accounts in AD.

Enter a new tool called Purple Knight from [Semperis](https://www.semperis.com/).

Purple Knight is a free AD security assessment tool. While it is free, the download requires a request for access at purple-knight.com. In my case approval came the same business day and I was running scans with PK within hours of first stumbling upon it.

The best description I have for PK is like Nessus for AD, but setup and configuration is even less involved than setting up a Nessus scan.

After a 10-15 minute installation process on a domain-joined machine, you’re able to run tests against 91 security indicators across 5 areas: AD Delegation, Account Security, AD Infrastructure Security, Group Policy Security, and Kerberos Security. I would include step-by-step instructions, but it’s literally as simple as checking the boxes for which of the 5 security indicators you want to scan and clicking “Run Tests.”

Once you run a scan, it generates an in-depth report card that gives an overview of each one of the 91 security indicators with correlations to the MITRE ATT&CK framework, description of the indicator, likelihood of compromise, evidence of exposure, and remediation steps if needed.

The dashboard shows an overview report summary like below.

[![](images/d0e1f093-47e8-42f5-a0bb-5740315978ab_622x574.png)](images/d0e1f093-47e8-42f5-a0bb-5740315978ab_622x574.png)

When viewing the full report (which can be saved as a PDF or CSV), you get an in-depth summary of findings for each of the security indicators that were tested.

[![](images/b1ef8eec-664e-4d97-961d-784b640b5964_625x378.png)](images/b1ef8eec-664e-4d97-961d-784b640b5964_625x378.png)

[![](images/85952d5e-b0b8-40fa-ac7b-f29151f3a334_589x406.png)](images/85952d5e-b0b8-40fa-ac7b-f29151f3a334_589x406.png)

In terms of support, there is a Purple Knight Slack channel, and on the one occasion I’ve had to use support they were prompt and invested in making sure I was able to use the tool. Something that may help cut out the need for contacting support - be sure you install PK in a directory that the software can write to. And, if you need to troubleshoot, log files are kept in the %programdata%\Semperis\Logs directory.

Happy hunting!
