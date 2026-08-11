---
title: "How to Install Docker"
subtitle: "The Cornerstone of Countless Projects"
date: 2025-03-11
author: Andy Lombardo
source: https://www.edtechirl.com/p/how-to-install-docker
---

# How to Install Docker

*The Cornerstone of Countless Projects*

[![A majestic whale skydiving through the clouds with a standard parachute. The whale has a joyful expression, gracefully falling through the bright blue sky with fluffy white clouds. The scene is whimsical and surreal, capturing the wonder of an unexpected adventure.](images/2e00be1b-4017-44ce-a273-9cca3a964eab_1024x1024.webp "A majestic whale skydiving through the clouds with a standard parachute. The whale has a joyful expression, gracefully falling through the bright blue sky with fluffy white clouds. The scene is whimsical and surreal, capturing the wonder of an unexpected adventure.")](images/2e00be1b-4017-44ce-a273-9cca3a964eab_1024x1024.webp)

Docker is a platform used to run applications in lightweight, portable environments called containers, and it’s the starting point for a tons of tech projects. To help speed up the process of getting Docker in place, below is a quick installation guide that assumes you have an Ubuntu machine primed and ready to go.

## Docker Install

From the command line of Ubuntu server, we’re going to install Docker.

First, go to the [Docker Install page for Ubuntu found here](https://docs.docker.com/engine/install/ubuntu/) and copy the code to set up Docker’s apt repository (or just grab it from here 😉) :

```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
```

Paste that block into your server’s terminal and hit enter, and it will do its thing:

[![](images/aa9cfdd9-248a-4322-8831-d2e9f7cb70d6_943x659.png)](images/aa9cfdd9-248a-4322-8831-d2e9f7cb70d6_943x659.png)

Next, you’ll copy and paste this command (also from the Docker Ubuntu install page linked above):

```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

After that runs, you can test to make sure Docker is running with this command:

```
sudo docker run hello-world
```

If successful, you should see:

[![](images/2df0a140-9c1c-4aa1-a37f-37de712c1224_842x566.png)](images/2df0a140-9c1c-4aa1-a37f-37de712c1224_842x566.png)

And that’s it—Docker is up and running!
