---
title: "Who’s Actually Attacking K12?"
subtitle: "Pt 3: Ransomware Crews, Scammers, Students, and Vendors"
date: 2026-03-06
author: Andy Lombardo
source: https://www.edtechirl.com/p/whos-actually-attacking-k12
---

# Who’s Actually Attacking K12?

*Pt 3: Ransomware Crews, Scammers, Students, and Vendors*

[![](images/6a728df2-cdb9-4933-82c7-f43cab725c19_1536x1024.png)](images/6a728df2-cdb9-4933-82c7-f43cab725c19_1536x1024.png)

When school leaders hear “cyber threat actors,” the mental image is often vague and intimidating: anonymous hackers, foreign governments, or shadowy groups with unlimited technical skill.

That image isn’t very useful for decision-making.

The reality in K12 is far more specific. Thankfully, it’s also more manageable. Most school cyber incidents come from a small set of repeatable threat actor types, each with distinct motivations, capabilities, and behaviors. Understanding who they are helps leaders prioritize controls that actually reduce risk, rather than planning for the wrong enemy.

This post maps the threat actor landscape that most commonly affects U.S. K12 public school districts and explains why clarity here is a leadership advantage.

## Ransomware groups: the dominant K12 adversary

If there is a single category of actor that defines K12 cybersecurity risk today, it is financially motivated ransomware groups.

These are not lone hackers. They are organized criminal operations that:

- Specialize in identifying vulnerable organizations
- Use repeatable intrusion methods
- Apply pressure through operational disruption and data exposure

### Why ransomware groups focus on schools

From an attacker’s perspective, K12 districts offer predictable dependence on IT systems, coupled with limited tolerance for prolonged outages and public pressure from families and communities. There is also inconsistent security maturity across districts

Many ransomware groups operate on a “ransomware-as-a-service” model, where affiliates deploy malware using proven techniques (phishing, stolen credentials, exposed remote access), then share profits with the core operators. Schools fit well into this scalable approach.

### How ransomware attacks typically unfold

In K12 incidents, the pattern often follows this flow:

1. Initial access via phishing or compromised credentials
2. Lateral movement across poorly segmented networks
3. Data exfiltration to enable extortion
4. Encryption and disruption timed for maximum impact

Importantly, technical sophistication is often moderate. What makes these attacks effective is not cutting-edge exploits, but weak identity controls and limited monitoring. This is good news for K12 defenders.

### Leadership implication

Ransomware groups succeed when districts are missing critical controls. A lack of MFA on email and remote access is the most common and most impactful. This is followed closely by having incomplete or untested backups. When it all hits the fan, if the district hasn’t rehearsed incident response decisions in advance, the advantage falls to the attackers.

This makes ransomware a governance issue as much as a technical one.

## Fraud rings and impersonators: quiet but costly

Not all cyber incidents involve malware. Financial fraud, especially email-based impersonation, remains one of the most damaging and under-discussed threats in K12.

These actors specialize in four main areas:

- Business Email Compromise (BEC)
- Vendor payment diversion
- Payroll and W-2 theft
- Social engineering of finance and HR staff

### Why districts are attractive fraud targets

As we’ve discussed previously in this series, school districts process large volumes of payments, time-sensitive invoices, seasonal payroll and tax filings, and vendor contracts with frequent changes. Attackers exploit routine workflows, not technical vulnerabilities. A well-timed email that appears to come from a trusted vendor or administrator can bypass controls if verification processes are weak.

### The hidden risk

Unlike ransomware, fraud incidents may go unnoticed for weeks or months. Sometimes, they may be discounted as accounting errors. Additionally, if no systems were breached, there may be no public disclosure. This can lead leaders to underestimate their prevalence, even though losses can be significant.

### Leadership implication

Fraud prevention depends heavily on process design, not security tools:

- Verification steps for payment changes
- Separation of duties
- Staff training that emphasizes pause and confirmation

From a leadership perspective, it’s noteworthy that these are not controls that take up space in the budget.

## Students as threat actors: not just “pranks”

One of the most distinctive features of K12 cybersecurity is the presence of students as insider threat actors.

These incidents range from curiosity-driven experimentation to intentional disruption, including:

- DDoS attacks to disrupt classes (esp. around standardized testing)
- Credential guessing or sharing
- Unauthorized access to grades or systems
- Online classroom disruptions

Many student incidents:

- Exploit weak internal controls rather than advanced techniques
- Reveal gaps in network segmentation and access management
- Scale quickly when tools are cheap and easily accessible

While intent may not be malicious in the traditional sense, impact still counts. District-wide outages or data exposure caused by a single student highlight systemic weaknesses.

In the past, I’ve encountered situations where students have even exploited security controls to cause disruption. For example, imagine you are following best practice recommendations and you have a lockout policy on your Active Directory, M365, or Google Workspace accounts. If students realize that, they can essentially DoS teacher and staff accounts by repeatedly logging in with intentionally invalid credentials. This is doubly impactful when students time this intentionally to coincide with testing.

These incidents are signals, not anomalies. They suggest some fundamental findings like overly broad access permissions and insufficient monitoring. Also unique to the school environment is frequently a lack of clear consequences and guidance. There have been many times when I’ve been part of a technical team that is escalated an issue that is essentially a classroom management issue. Even though all students and staff are governed by an Acceptable Use Policy, staff often have an inherent bias towards not intervening in cases involving technology.

Effective response balances accountability with education without dismissing the risk.

## Accidental insiders: mistakes with real consequences

Not every insider incident is intentional. Unintentional actions by staff remain a significant source of K12 cyber risk. Common scenarios include:

- Misconfigured cloud storage exposing data
- Lost or stolen unencrypted devices
- Emails sent to the wrong recipients
- Weak passwords reused across systems

These incidents rarely involve bad intent, but they can still trigger breach notifications, legal scrutiny, and loss of trust.

To gain perspective on the real-world impact this can have, I once spoke with a colleague who had a guidance counselor in their district who maintained a spreadsheet of all the students who were “on their radar,” along with detailed notes about WHY they were on their radar, including very sensitive personal information about traumas they had experienced. This counselor then, entirely by accident, set the sharing settings to “Anyone in the organization can view.” They don’t know how long it was shared that way, but it eventually surfaced that students had found the document.

### Leadership implication

Blame-based cultures discourage reporting. Districts that encourage early reporting, provide clear guidance, and invest in usability-focused security tend to contain damage faster and reduce repeat incidents.

As a personal anecdote, early in my career as a tech director, I implemented an industry-standard security awareness training program from a pre-eminent vendor in the space. I assumed that phishing staff and enrolling them in training for clicking on hinky links would be enough. However, what I learned was that a punitive program where clicking = 15+ minutes of training, users felt punished. This led them to hiding information when there was a real incident. In the years since, we’ve flipped to security awareness that focuses more on building a positive and healthy culture around reporting. Recently, a K12-specific human risk and security awareness training vendor called [CyberNut](https://www.cybernut.com) has emerged who is doing great work to gamify and create engagement around phishing simulations. CyberNut also offers free phishing baseline assessments.

## Vendors as “shadow threat actors”

One of the least intuitive but most consequential threat actor categories in K12 is third-party vendors.

When a vendor is breached, district data may be exposed even if district systems are secure. Even worse, when a vendor is compromised multiple districts can be impacted simultaneously. A great example of this is the [PowerSchool breach from Dec. 2024](https://www.edtechirl.com/p/the-powerschool-data-breach-what).

Additionally, since the vendors control the infrastructure, districts may have limited visibility into both the root cause of the incident and into the depth of impact.

Edtech ecosystems are dense, and security maturity varies widely among providers. Attackers know this.

Districts often adopt tools rapidly to meet instructional needs. Especially in small- to medium-sized school districts, vendors may not see a district as having enough buying power to create enough leverage to demand strong security controls. That also leaves schools having to rely on vendor assurances without independent verification

From a criminal perspective, one vendor breach can yield hundreds of victims.

### Leadership implication

Vendor risk management is not optional. It requires prioritizing high-impact vendors and asking basic security questions. It also includes ensuring that there are breach notification and security requirements in contracts.

## What about nation-state actors?

In contrast to higher education, there is little evidence that nation-state cyber actors systematically target K12 school districts.

While schools may be indirectly affected by broad supply chain incidents, K12 districts are not typical espionage targets. This matters because it helps leaders avoid over-investing in defenses aimed at rare threats while under-investing in controls that stop common ones.

## Matching defenses to real attackers

The value of understanding threat actors is alignment.

Different actors require different responses:

- Ransomware groups → MFA, backups, network segmentation, incident planning
- Fraud rings → process controls and verification
- Students → access management and monitoring
- Vendors → procurement and contract governance

When districts plan for the right threats, security becomes more practical AND more achievable.

## Leadership questions to ask next

To translate threat awareness into action, district leaders can ask:

1. Which threat actor type would cause the most disruption if successful. Are we prioritizing defenses accordingly?
2. Are our incident plans built around ransomware realities or generic “cyber events”?
3. Do our procurement practices reduce or amplify vendor risk?
4. Are internal incidents treated as learning opportunities or failures?
5. Are we investing in controls that stop common attacks, or rare ones?
