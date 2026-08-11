---
title: "APIs: The Automation Pie in the Sky"
subtitle: "Start leveraging REST APIs to automate complex tasks!"
date: 2024-07-12
author: Andy Lombardo
source: https://www.edtechirl.com/p/apis-the-automation-pie-in-the-sky
---

# APIs: The Automation Pie in the Sky

*Start leveraging REST APIs to automate complex tasks!*

[![](images/daa07fd7-ea30-4686-8360-28881439d764_1080x1080.png)](images/daa07fd7-ea30-4686-8360-28881439d764_1080x1080.png)

This article is going to cover how APIs can be leveraged to make life easier for IT Admins, and why you should be adding this to your list of skills. It is also going to cover the types of things you can do with APIs, give a basic idea of how they work, and show you how to get started.

### First things first. What is an API?

API, or Application Programming Interfaces, are defined as building blocks for facilitating the transfer of data from two computers or systems. Specifically, we are going to be talking about **REST APIs (aka RESTful)**. The REST architecture is used for transferring data over the internet.

REST APIs are effectively requests you are making to a cloud-based system over the web regarding data on the cloud system. For example, an API I often use is for [Snipe IT](https://snipeitapp.com/), which is a cloud-based, asset management system. It contains information on the computers and other technology owned by our school district, so we have a record of these assets and who the devices are checked out to. Using the API, we can make requests to get information or make changes to Snipe’s list of users and devices. For example, we could have it do things like creating new assets or users in the system, check-in devices, get a list of all our users or assets, check out devices to users, and much more. You may be wondering, “Why is this useful? Aren’t these already features built into the GUI?”, and you would be right, but it really becomes useful for the niche scenarios that aren’t built into the GUI.

### Real life examples of things I have done with APIs

**Mass check in devices from Snipe IT** - Surprisingly, with all of the things you can do with a CSV in Snipe IT, there isn’t a way to mass check in devices. You can change the user they are assigned to, but you can remove that user association and change the device to unassigned and checked in. However, I was able to get around this using a script with an API. The script would check a CSV of our assets (around 500 on this list), and on each asset, would modify the device to be checked in. Writing this script took around 30 minutes, but doing this by hand would have taken hours to click on each device and to click the check in button.

**Mass generating groups and users in Intune -** I needed to create around 100 groups in Intune because I wanted to create a group for each of our elementary school’s classes. Instead of spending hours upon hours to manually add these in one by one, I created a CSV with all of the information for each group, and had a script take each line of the CSV and create a group out of it. After this, I made a similar script that allowed me to generate users this way directly into Intune as well.

**Creating an Integration between Intune and Snipe IT -** I wrote [an article here](https://www.edtechirl.com/p/snipe-it-and-azure-asset-management) on this one. I wanted to put information from Snipe into Intune, so we could easily see who a device was checked out to, without having to switch over to our asset management system. I ended up creating a script that would pull all of the devices in Snipe, associate it with the corresponding intune device based on the serial number, and then write the checked-out user and other information in the notes section of the device in Intune. I put this script in an azure automation account so it will run every day. This is something that couldn’t be maintained without automation.

### Okay, but I don’t use Snipe IT or Intune

Well, good news is there is an API for just about everything! Some examples of ones you may find interesting are…

- [Powerschool](https://support.powerschool.com/authenticate.action)
- [Canvas](https://canvas.instructure.com/doc/api/)
- [Blackboard/Anthology](https://developer.blackboard.com/portal/displayApi/Learn)
- [D2L/Brightspace](https://docs.valence.desire2learn.com/reference.html)
- [Aruba](https://developer.arubanetworks.com/aruba-central/docs/api-getting-started)
- [Cisco](https://developer.cisco.com/docs/service-apis/services-apis-base-urls/)
- [Google Admin Console](https://developers.google.com/admin-sdk/directory/reference/rest)
- [Follett Destiny](https://www.follettcommunity.com/s/article/Destiny-Open-APIs-Developers-Guide)
- [Freshdesk](https://developers.freshdesk.com/api/)
- [ChatGPT](https://platform.openai.com/docs/api-reference/introduction)
- you get the idea

### How to get started

The one prerequisite for using APIs is some fundamental coding skills. Luckily, almost every language has a way to make API requests, so if you are familiar with a specific language, you should be able to use it. You don’t need to be an expert at coding to do this, but having the fundamentals down of a language will make this a lot easier.

If you don’t have any coding knowledge yet, I would recommend PowerShell, especially if you’re in the sysadmin space working with windows computers, there’s lots of other benefits you’ll get from learning it. I am most familiar with PowerShell, so whenever I give examples of the coding structure it will be using Windows PowerShell. I will also be using the SNIPE IT API as an example, as it has really good [documentation](https://snipe-it.readme.io/reference/api-overview) and a sample database you can query.

### Formatting your API Request

#### The Header

First, you will need to prove you are authorized to access the information before doing anything else. Typically, this is done with some form of token. To get access to this token, typically there is a spot in the settings of the application where you can generate one, but be sure to refer to the documentation of the API you are using for best practice. Once you have this token, you will save this in the Header. The header is effectively a variable where you save your authentication details, define what format you are sending that data (typically XML or JSON), and how you expect to the response to be formatted (again, XML or JSON). Below is an example of a header in Powershell.

```
$headers=@{} #Create the hashtable for our header
$headers.Add("accept", "application/json") #defines the response format
$headers.Add("Authorization", "Bearer eyJ0eXAiOiJKV1QiLCJhbG...") #auth token
$headers.Add("content-type", "application/json") 
#defines the format of the body of the request
```

#### URIs (Uniform Resource Identifier)

When making a Request, you have to point to the specific resource you would like to work with. Typically, the best way to figure out these resources is to refer to documentation of the API. As you may expect, the URI looks like a website link. For example, below is the URI used to get the information of the device in Snipe with ID number 2597. Note that this URI is unique to your account on your system. The URI below links to the sample database of Snipe IT and an example resource on it.

```
https://develop.snipeitapp.com/api/v1/hardware/2597
```

#### Methods (Request Types)

When making an API request, you have to define the method of your request. For example, let’s say we want to delete the asset above from our URI section. The URI doesn’t tell the system what to do with the resource, we have just targeted it. That is where methods come in. Below is each method type and what they do.

- **GET** - A request to get data or information (i.e. getting info on an asset)
- **POST** - A request to create data or information (i.e. creating a new asset)
- **PATCH** - Update data without overwriting anything (i.e. changing the model number of an asset without changing any other information)
- **PUT** - Update data and overwriting the current entry (i.e. if you wanted to replace an asset in your system and to effectively treat it as a new entry)
- **DELETE -** Remove the data from the database (i.e. removing an asset entirely)

For our example scenario above, we would want to use the DELETE method. Typically, you can find the methods available to each URI in your API’s documentation (if you haven’t caught on yet, the documentation REALLY helps).

#### Body of the request

The body of the request is where you define the changes you would like to make. For example, if you wanted to change the asset tag of the device in snipe with ID 2597, you would make a PATCH request and format your body to look like the code below.

```
-Body '{"asset_tag":"a1234"}'
```

Note that you won’t always have a body for your requests. For example, with GET requests you’re asking for information and because of this, don’t have to define any changes. Same goes with DELETE requests.

#### Response

The response is where you figure out if you did it correct or not. Typically, in the response you will get a status code (in snipe 200 is success and 401 is failure) and you’ll get some content to your request that will tell you if the request went through successfully, or if there was an error. If you’re doing a GET request, this is where you will get the content of the information you are requesting. Below is the example of the response to the request I made above to update the asset tag of the asset with ID 2597. In the request you can see where it says it updated the asset successfully and where it has the new asset tag set below.

```
StatusCode        : 200
StatusDescription : OK
Content           : {"status":"success","messages":"Asset updated 
                    successfully.","payload":{"id":2597,"name":null,"asset_tag":"a1234","model_id":18,"serial":"b8e08b7b-f914-3394-89cd-89236b709e18","purchase_date":"2023-10...
RawContent        : HTTP/1.1 200 OK
                    Transfer-Encoding: chunked
                    Connection: keep-alive
                    X-RateLimit-Limit: 10
                    X-RateLimit-Remaining: 8
                    Access-Control-Allow-Origin: *
                    Pragma: no-cache
                    X-Content-Type-Options: nosniff...
Forms             : {}
Headers           : {[Transfer-Encoding, chunked], [Connection, keep-alive], [X-RateLimit-Limit, 10], [X-RateLimit-Remaining, 8]...}
Images            : {}
InputFields       : {}
Links             : {}
ParsedHtml        : mshtml.HTMLDocumentClass
RawContentLength  : 1478
```

#### Let’s put it all together

Now that you know each component of an API request, let’s put it all together and make a request to GET the information of asset 2597 from SNIPE’s example database.

[![](images/bbed3d85-0d92-4f7e-b2f6-45232b173a0a_2512x1002.png)](images/bbed3d85-0d92-4f7e-b2f6-45232b173a0a_2512x1002.png)

As you can see below, I am able to format my request and pull all of the information successfully on the asset with ID 2597.

#### Final tips and ending notes

Documentation, documentation, documentation. To use an API, documentation is basically required so you can figure out the URI’s of your resources. It makes this process so much easier. So please, READ THE ‘FLIPPIN’ MANUAL.

Some docs even have API explorers where it shows you all possible requests, how to format each type of request, and gives a code sample for each language. Below is an example of Snipe IT’s awesome explorer that is built into their docs.

[![](images/557b49b6-dbb6-4165-baca-4e91a10078a1_2917x1226.png)](images/557b49b6-dbb6-4165-baca-4e91a10078a1_2917x1226.png)

I hope this information is helpful and leads some of you all to save some man hours and reduce your workloads like it has for me.
