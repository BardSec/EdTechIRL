---
title: "A Word About Passwords"
date: 2022-03-14
author: Andy Lombardo
source: https://www.edtechirl.com/p/a-word-about-passwords
---

# A Word About Passwords

#### 

[![](https://images.unsplash.com/photo-1635237393049-55046279ebb8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHwxNHx8cGFzc3dvcmRzfGVufDB8fHx8MTY0NzIyMzcwNA&ixlib=rb-1.2.1&q=80&w=1080)](https://images.unsplash.com/photo-1635237393049-55046279ebb8?crop=entropy&cs=tinysrgb&fit=max&fm=jpg&ixid=MnwzMDAzMzh8MHwxfHNlYXJjaHwxNHx8cGFzc3dvcmRzfGVufDB8fHx8MTY0NzIyMzcwNA&ixlib=rb-1.2.1&q=80&w=1080)

Photo by [olieman.eth](https://unsplash.com/@moneyphotos "olieman.eth") on [Unsplash](https://unsplash.com "Unsplash")

#### Admin rights and least privilege

Hot topic in education. As a former teacher, I completely understand the desire and the need to have admin rights to install what you want, when you want, without burdensome review. However, when our district went the least privilege route, malware infections went from a weekly event to virtually non-existent. All security is a trade-off though, so we went with a blended approached of explicitly denying admin rights by defaults, but offering our users the ability to earn admin rights by completing security awareness training about the responsibilities that come with admin rights, and that actions to take when you accidentally install something bad or lose your creds. When we revamp this system, we'll add in requirements to not use a recycled password for admin credentials. In a dream world, requiring MFA would be nice, but at least in my environment I don't think it's a trade-off folks are willing to make.

#### Password Strength

When making a push for password resets, KnowBe4 makes a[free password strength tester you can run in your AD environment](https://www.knowbe4.com/weak-password-test). I also like to use the[strength test found here](http://rumkin.com/tools/password/passchk.php), because it doesn't just say strong or weak, but determines how many bits of entropy the password has, and categorizes strength based on what you want to use it for. The scale ranges from "Very weak, might keep out family members" to "Very Strong; often overkill." The most important mental shift to make with passwords is to stop thinking about passwords and think about passphrases. For example, this 8 character password [u$T7Dc7U] with uppercase, lowercase, numbers, and special characters is rated as Week with 32.1 bits of entropy. [Rainbowunicornsaremyfavorite] on the other hand is approximately a billion times easier to memorize, and is also considered Very Strong with 130.6 bits of entropy.

#### Password Reuse

Password reuse keeps me awake at night. To think that everyone will use totally unique passwords for every sight is unrealistic, even with a password manager. It's something to aspire to, but I know it's not going to happen. Instead, I try to drive home the importance of making their most important accounts totally unique. School Email should be totally unique and not reused ANYWHERE. Student Information System (SIS) passwords should be totally unique and not reused ANYWHERE. Beyond that, I encourage folks to do clusters of unique passwords. For example, use/reuse one password for social media. Use a different password for banking. Use a different password for online shopping. In this same training, it's a great place to introduce the topic of password managers. For an advanced session, you could throw out something like[using 1password as a password manager with integration with Privacy.com](https://blog.1password.com/privacy-virtual-cards/). This setup allows you to set up temporary or one-time-use credit card numbers to shop online. Amazing.   
  
To help make this case more clearly to users, we subscribe to[HaveIBeenPwned.com](https://www.haveibeenpwned.com/)'s domain notification list. Whenever HIBP posts details of another breach, if any of the folks in my domain were included in the breach, I get a notification. I then notifify those users with a sample letter outlining what service they use that was breached, the data that was breached, and instructions for changing their most important school passwords, and point out that they should change that password anywhere they use it in junction with their school email account.

[![have i been pwned sample letter](https://substackcdn.com/image/fetch/$s_!-7uL!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7731b7de-4f2c-48ab-812c-7f9be3636789_626x714.png "have i been pwned sample letter")](https://substackcdn.com/image/fetch/$s_!-7uL!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F7731b7de-4f2c-48ab-812c-7f9be3636789_626x714.png)
