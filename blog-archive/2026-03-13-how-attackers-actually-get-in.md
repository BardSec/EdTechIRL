---
title: "How Attackers Actually Get In"
subtitle: "Pt. 4: Phishing, Credentials, Vendors, and Remote Access in K12"
date: 2026-03-13
author: Andy Lombardo
source: https://www.edtechirl.com/p/how-attackers-actually-get-in
---

# How Attackers Actually Get In

*Pt. 4: Phishing, Credentials, Vendors, and Remote Access in K12*

[![](https://substackcdn.com/image/fetch/$s_!BATp!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F937fecb5-dc96-41b4-8011-96f3e9f95e68_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!BATp!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F937fecb5-dc96-41b4-8011-96f3e9f95e68_1536x1024.png)

When school districts experience a cyber incident, the first question leaders often ask is, *“How did they get in?”*

The answer is almost never a zero-day exploit or an impossibly sophisticated hack. In K12, most successful attacks enter through the same small set of front doors, year after year. These entry points are well-known, widely documented, and, largely preventable.

This post breaks down the most common attack paths into U.S. K12 school districts, explains why they keep working, and highlights the controls that consistently stop them. For district leaders, this is where cybersecurity shifts from abstract risk to concrete governance choices.

## The uncomfortable truth about K12 entry points

Across incident reports, investigations, and post-mortems, a consistent theme emerges: attackers don’t need to be clever when basic controls are missing or unevenly applied.

In K12, successful intrusions most often involve one of four methods:

- Human trust being exploited (phishing and impersonation)
- Credentials being stolen or misused
- Vendors serving as indirect entry points
- Remote access being exposed without sufficient safeguards

Understanding these patterns helps leaders focus on *systemic fixes*, not one-off reactions.

## 1. Phishing is still the front door

Phishing remains the most common initial access vector in K12 cyber incidents.

Though phishing attacks have evolved over time and have improved dramatically with the popularization of generative AI, phishing emails still frequently checks one of more of these boxes:

- **Spoofing/Impersonation.** Messages appear to come from colleagues, administrators, or vendors.
- **Malware**. Messages may contain malicious links or attachments.
- **Social Engineering.** Messages prompt urgent action (“invoice attached,” “account problem,” “document shared”).

Once a staff member clicks or enters credentials, attackers gain a foothold, often without triggering alarms.

### Why phishing works in schools

There are a number of reasons why phishing thrives in K12 environments. School staff attention has historically been divided. When I was training for the classroom, the head of the education department at my college always emphasized how one of the most necessary teacher traits is to be able to know what’s going on in every part of your classroom at all times, whether you’re facing the class, facing the board, or standing in the hallway. Education is a mentally taxing industry, even without worrying about technology or cyber attacks. When you add the additional layer of staff having to manage high volumes of email under pressure, and a well-crafted phish is poised to win.

As schools have become more connected and workloads have moved to the cloud, teachers have also had to contend with the abuse of cloud-based document sharing platforms like Google Drive, Microsoft OneDrive, or DropBox. While these platforms have solved an educational problem and enhanced teachers’ abilities to collaborate, they’ve also introduced a new attack surface that attackers can exploit to try to deceive teachers and administrators.

With this perfect storm of high workload and constant communication and collaboration, teachers also aren’t left with a lot of time for training. Even when time is dedicated to professional development, a constant murmur throughout the training is about how much more effective they could be using their time if they could be working in their classrooms. There is enough difficulty trying to pack in instructional training without having to find time to train on cybersecurity. To amplify that problem, most security awareness training platforms are designed for industry and not education.

Finally, due to the mechanics of a phishing email, there’s not immediate feedback for teachers when they do fall for a phish. The consequences of that interaction is not immediately visible or apparent. In many cases, I’ve helped clean up incidents where an educator with a compromised account didn’t make a connection between clicking on a phishing email and the eventual account compromise.

With everything going on in the daily life of an educator, there isn’t much room for error. Simultaneously, however, attackers don’t need many successes. One compromised account can be enough to pivot deeper into district systems.

### Leadership takeaway

Phishing resistance is not just a training issue. It depends on technical controls like enforcing MFA. While not perfect, MFA provided a second barrier between a user and a bad guy when their credentials are compromised.

Email security at the tenant level is also a necessary measure, both for preventing phishing emails from landing in a user’s mailbox, but also to conduct triage and clean up after an account compromise.

Finally, leadership messaging should prioritize reporting over blame. When I implemented a phishing simulation program for the first time in 2017, it was implemented in a punitive fashion. Over the first year of the deployment, some teachers got better at not clicking phishing emails, but the negative side was that educators felt like falling for a simulation resulted in punishment because they were being enrolled in training on top of their already over-packed workload. This led to negative feelings towards the IT department, but more importantly it led to people denying interacting with a phishing email when they did because they were worried about the repercussions. Fortunately, in the years since, this aspect of security awareness training has gained visibility, and vendors like [CyberNut](https://www.cybernut.com) have leaned into positive or gamified security awareness training programs.

## 2. Credential compromise: the root cause beneath many incidents

Stolen or misused credentials are at the heart of many K12 breaches, even when phishing isn’t the visible trigger.

Common credential-related failures include:

- Reused passwords across systems
- Shared administrative accounts
- Default or weak student passwords
- Accounts not disabled after staff leave

Once attackers obtain valid credentials, they often look like legitimate users, which makes detection exponentially more difficult.

### Why credentials matter so much in K12

School systems often trust authenticated users too broadly. Flat networks, single sign-on without strong safeguards, and legacy permissions mean that one compromised account can unlock far more than intended. In ransomware incidents, attackers frequently spend days or weeks moving quietly through systems before triggering disruption.

### Leadership takeaway

Credential hygiene is foundational. Leaders should expect:

- MFA on email, remote access, finance, and administrative systems
- Regular review of privileged accounts
- Clear ownership of identity lifecycle management

## 3. Vendor and third-party pathways: breaches without “being hacked”

One of the most counterintuitive entry points for district leaders is vendor compromise.

In these cases, district systems may never be directly attacked, but sensitive student or staff data can be exposed anyway. For a vendor that serves many districts, the blast radius can be expansive with multiple districts impacted simultaneously.

Attackers target vendors because it’s efficient. One breach can yield access to data from dozens, or even hundreds, of school systems.

### Why vendor risk is persistent

Districts rely on vendors for many core parts of the educational experience, ranging from student information systems to learning platforms, but also encompassing infrastructure like payments, transportation, food services, and communication.

Yet, security vetting is often informal, and contracts may lack strong breach notification or security requirements.

### Leadership takeaway

Vendor security is district security. Leaders influence this risk by:

- Prioritizing high-impact vendors for scrutiny
- Asking basic security questions during procurement
- Requiring timely breach notification and minimum controls

A key tenet of cybersecurity is that you can’t protect what you don’t know about. Many districts today don’t have an accurate or up-to-date asset inventory of all software used in their environment. This lack of visibility can hamstring a school’s ability to properly managed 3rd party risk.

## 4. Remote access exposure: convenience without guardrails

The rapid expansion of remote access during and after the pandemic created new entry points that attackers continue to exploit.

Common weaknesses include things like exposed Remote Desktop Protocol (RDP) ports. RDP didn’t earn the nickname of Ransomware Deployment Protocol for no reason. Beyond RDP, many systems have VPNs or other remote access tools that offer a path through the firewall, and if those systems aren’t properly protected by controls like MFA, they are a liability that exceeds the usefulness of its convenience.

In the same vein, there are many legacy systems that can offer remote access to a school’s network or cloud environment. If these systems aren’t protected with modern controls, they are absolutely a liability. This can come in unexpected forms. Say, for example, your facilities department purchased an HVAC monitoring system from a 3rd party vendor. They vendor integrates the system with the HVAC system and sets up a remote access portal so facilities can check HVAC alerts from home after hours. Chances are, the integrating vendor is not a security provider. If that portal isn’t protected by MFA or other conditional access policies, it also becomes an unexpected liability. Attackers routinely scan the internet for exposed services, then use stolen or brute-forced credentials to gain access.

A common theme in my posts is the idea that cybersecurity is not an IT problem. If basic workflows like account onboarding and off-boarding aren’t managed efficiently, that leaves the door open for access through accounts that should no longer be provisioned. In the very least, there should be regular audits to verify separated staff accounts are disabled. Preferably, though, HR processes like onboarding and off-boarding should be automated and tied directly to a source of truth like the Student Information System.

### Why this matters for leaders

Remote access failures don’t look dramatic, but they are highly effective. Once inside, attackers often encounter:

- Minimal network segmentation
- Limited monitoring
- Broad internal access

This combination enables rapid escalation.

### Leadership takeaway

Remote access should be treated as high-risk infrastructure, not convenience plumbing. Expect:

- MFA everywhere
- Regular audits of exposed services
- Clear ownership for shutting down temporary access

## 5. Weak access controls and misconfiguration

Not all incidents involve attackers. Some begin with configuration errors that expose data or functionality unintentionally.

Examples include:

- Cloud storage made public by mistake
- Sensitive data embedded in web pages or code
- Overly permissive access to student or staff records

These incidents often surface through journalists, researchers, or accidental discovery, but attackers can and do find the same weaknesses.

### Leadership takeaway

Configuration risk grows with complexity. Leaders can mitigate it by:

- Supporting change management and review processes
- Avoiding tool sprawl
- Investing in simplicity and standardization

## 6. DDoS and disruption attacks: low skill, high impact

Distributed denial-of-service (DDoS) attacks are another common K12 entry path. The difference here is that these attacked aren’t designed to steal data, but rather to disrupt operations.

These attacks form a dangerous triad:

- They flood district networks or platforms with traffic
- They can be launched cheaply
- They are sometimes carried out by students or local actors

While technically unsophisticated, they can halt instruction, especially during online learning or testing windows.

### Leadership takeaway

DDoS resilience is about preparedness, not perfection. Options include:

- Internet service provider protections
- Cloud-based mitigation
- Clear escalation and communication plans

## The pattern across all entry points

Across phishing, credentials, vendors, remote access, and misconfiguration, one pattern repeats:

> Most K12 cyber incidents exploit gaps in basic controls, not advanced vulnerabilities.

This is both sobering and encouraging. It means districts are not powerless, but it also means leadership choices matter.

## The controls that consistently break attack chains

Based on incident data, the following measures repeatedly reduce successful intrusions:

- Enforced multi-factor authentication for staff
- Strong identity and access management practices
- Regular patching and system updates
- Network segmentation
- Vendor risk prioritization
- Practiced incident response and recovery

These are not exotic solutions. They are governance-backed fundamentals. It’s important to note: these controls aren’t controls you go out and buy off the shelf. They have more to do with planning, policies, and procedures than investing in a best-in-class cybersecurity tool designed to keep out advanced threats.

[![](https://substackcdn.com/image/fetch/$s_!xlnf!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a32f217-de73-4593-baff-7029da840e64_1449x740.png)](https://substackcdn.com/image/fetch/$s_!xlnf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2a32f217-de73-4593-baff-7029da840e64_1449x740.png)

## Leadership questions to ask now

To translate entry-point awareness into action, district leaders can ask:

1. Which of these entry points is most likely in our environment? Why?
2. Where do we rely on “trust” instead of verification?
3. Are temporary access decisions being revisited and closed?
4. Which vendors represent our largest data exposure?
5. Have we tested whether our controls actually stop a real attack?

---

### Coming next in the series

Part #5: “When Systems Go Down: Instructional Disruption, Costs, and the Human Impact of K12 Cyber Incidents”

We’ll shift from entry points to consequences: what really breaks during an incident, who is affected first, and why recovery takes longer than most people expect.
