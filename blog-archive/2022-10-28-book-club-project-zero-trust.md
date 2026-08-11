---
title: "Book Club: Project Zero Trust"
subtitle: "An introduction to the Zero Trust design principles and methodology as implemented in a fictional company"
date: 2022-10-28
author: Andy Lombardo
source: https://www.edtechirl.com/p/book-club-project-zero-trust
---

# Book Club: Project Zero Trust

*An introduction to the Zero Trust design principles and methodology as implemented in a fictional company*

[![](https://substackcdn.com/image/fetch/$s_!VT3T!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F976d5d22-accf-4a54-86d7-0a47ca000e12_638x739.png)](https://substackcdn.com/image/fetch/$s_!VT3T!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F976d5d22-accf-4a54-86d7-0a47ca000e12_638x739.png)

Project Zero Trust by George Finney

As an English major and former Literature teacher who now lives in the tech world, I’m a sucker for novels like *Project Phoenix*, *The Unicorn Project*, and *The Goal* that teach complex concepts through stories. Walking into *Project Zero Trust* by George Finney, most of my previous exposure to the concept of Zero Trust and Zero Trust Architecture came at the hands of cold contacts that were trying to sell me a solution. Beyond the mantra of “assume breach,” everything I knew about Zero Trust came directly from the marketing department.

This novel serves as a jumping-off point to the concept of Zero Trust by letting you look over the characters’ shoulders during a Zero Trust transformation at MarchFit, a fictional treadmill company that’s just experienced an attack that’s disrupted service and compromised data. Rather that following the incident response process (which is a novel I would read!), the story follows Dylan Thomas\*, the newly-hired Director of Cloud Infrastructure, whose Day 1 coincides with the breach and ongoing attack. Rather than diving into Cloud Infrastructure or Incident Response, however, Dylan is tasked with spearheading the company’s Zero Trust transformation to prevent future compromises.

Along the way, the story follows the structure of the four Zero Trust Design Principles and five steps of the Zero Trust Design Methodology, a framework devised by Zero Trust progenitor John Kindervag:

*Zero Trust Design Principles:*

1. Define business outcomes
2. Design from the inside out
3. Determine who or what needs access
4. Inspect and log all traffic

*Zero Trust Design Methodology:*

1. Define the protect surface
2. Map the transaction flows
3. Build a Zero Trust Architecture
4. Create a Zero Trust Policy
5. Monitor and maintain the environment

One point made in the book that’s worth noting is that any Zero Trust project is bespoke for each specific organization’s scenario, so this story isn’t intended to be a blueprint or guide for conducting your own transformation. Rather, it’s more like a primer to give you the main concepts and vocabulary to begin preparing for your transformation. Additionally, it’s not highly technical in nature. It can be read and understood by folks with roles varying from student to C-level without the need for a tech translator.

As the story develops, these are some of the key points about Zero Trust that are displayed:

- Traditional security was perimeter based - a castle with a moat = a network with a firewall. Once the castle is breached, attackers have access to the interior. Another example is an office building where the front door is locked, but all the interior offices are open. Zero Trust is about locking the interior doors as well. The assumption is that you have been or will be compromised, so how can you stop the bleeding when it happens?
- The concept that gives Zero Trust its name is the idea that trust is a human concept that shouldn’t have a place in information systems, so it should be removed from those systems wherever possible.
- The core unit in Zero Trust is a Protect Surface. This is in contrast to the more commonly discussed concept of an Attack Surface. Whereas an Attack Surface can be infinite as threat actors and their tactics, techniques, and procedures evolve, adapt, and multiply, a Protect Surface is a finite, definable resource that needs to be protected. Kindervag defines a Protect Surface as “[the smallest possible reduction of the attack surface](https://www.paloaltonetworks.com/blog/2018/09/define-protect-surface-massively-reduce-attack-surface/).” A Protect Surface is determined based on one or more of these components (DAAS):

  - **D**ata — What data needs to be protected?
  - **A**pplications — Which applications consume sensitive information?
  - **A**ssets — Which assets are most sensitive?
  - **S**ervices — Which services, such as DNS, DHCP, and Active Directory, can be exploited to disrupt normal IT operations?

    [from “Define a Protect Surface to Massively Reduce Your Attack Surface” by John Kindervag](https://www.paloaltonetworks.com/blog/2018/09/define-protect-surface-massively-reduce-attack-surface/)
- When evaluating where to inject Zero Trust design principles in a network, identifying Protect Surfaces using the above DAAS model is the first step in the methodology.
- An advantage to considering Protect Surfaces compared to considering Attack Surfaces is that Protect Surfaces are, as I mentioned, finite. If you’re familiar enough with your network, you or you and your team could probably sit down and identify the majority of your possible Protect Surfaces in a single meeting.
- After defining Protect Surfaces, the next part of the methodology is to map transaction flows. Since you have defined Protect Surfaces, who do they talk to? How does the data flow? Where is information being sent to and received from?
- The next step in the methodology is to build a Zero Trust architecture. Whereas the old architecture was a perimeter defense, Zero Trust is based on [microsegmentation](https://www.paloaltonetworks.com/cyberpedia/what-is-microsegmentation) and the isolation of Protect Surfaces in order to be able to assign granular, identity-based policies to each surface based on its own specific needs.
- Following the design of the Zero Trust Architecture, a Zero Trust Policy is created. For each of the Protect Surfaces, now that they’ve been segmented into their own isolated surface, they need a policy designed specifically for them in terms of who or what can access the surface, and who or what they can communicate with. The concept of stateful transactions is important here, because another antiquated network design principle is the concept of only restricting inbound traffic while allowing unrestricted outbound traffic. A tenet of Zero Trust is to design in a manner that you assume you have already been breached, and build the architecture and policies in a manner so that you limit the blast radius of the breach. Having stateful policies takes into consideration what traffic both to and FROM a specific Protect Surface should look like, and whether or not it should be permitted. Since the architecture is segmented to that specific surface, these policies can be very specific and granular.
- Finally, the methodology completes with monitoring and maintaining the environment. Without monitoring, you can’t verify the efficacy of your architecture and policies. Additionally, as your organization evolves, requirements and policies change, necessitating evaluation of your architecture and policies.

That’s a fair amount of pretty theoretical information on Zero Trust architecture. The power of *Project Zero Trust* is it takes that theoretical framework, and the author applies it to a mock scenario to be able to concretely apply the design principles and methodology to a realistic scenario. There’s a Socratic feeling to the book as you follow the characters through the steps of the process, and they ask the questions you should be thinking of as you’re moving through the process yourself. The book definitely isn’t a how-to manual for how to accomplish Zero Trust, but it doesn’t claim to be. Instead, it’s an excellent primer on the topic that gives shape to the concept in a way that cuts through all the FUD that vendors use when when trying to sell Zero Trust as a product.

**Additional Zero Trust Resources:**

[No More Chewy Centers: Introducing the Zero Trust Model of Information Security by John Kindervag](https://media.paloaltonetworks.com/documents/Forrester-No-More-Chewy-Centers.pdf) (whitepaper)

[Cloud Security Today with Matthew Chiodi podcast: Zero Trust with No FUD, an interview with John Kindervag](https://podcasts.apple.com/us/podcast/zero-trust-with-no-fud/id1557790941?i=1000570687574)

[Palo Alto Blog Posts by John Kindervag](https://www.paloaltonetworks.com/blog/author/john-kindervag/)

[NIST SP 800-207](https://csrc.nist.gov/publications/detail/sp/800-207/final)

\*No, not [that Dylan Thomas](https://poets.org/poem/do-not-go-gentle-good-night). Or that [Vic Vega](https://quentin-tarantino.fandom.com/wiki/Vic_Vega) or [Mia Wallace](https://en.wikipedia.org/wiki/Mia_Wallace)
