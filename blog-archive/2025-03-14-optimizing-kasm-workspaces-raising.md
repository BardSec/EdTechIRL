---
title: "Optimizing Kasm Workspaces: Raising the Default 80GB Storage Cap"
date: 2025-03-14
author: Andy Lombardo
source: https://www.edtechirl.com/p/optimizing-kasm-workspaces-raising
---

# Optimizing Kasm Workspaces: Raising the Default 80GB Storage Cap

[![A large anthropomorphized computer with expressive eyes and arms, squeezed uncomfortably into a tiny birdcage. The computer looks frustrated or trapped, pressing against the bars. The scene is depicted in a whimsical, storybook fantasy style with rich colors, intricate details, and a painterly, magical atmosphere.](images/f7f4141c-a610-48b4-8e3c-c443227ed466_1024x1024.webp "A large anthropomorphized computer with expressive eyes and arms, squeezed uncomfortably into a tiny birdcage. The computer looks frustrated or trapped, pressing against the bars. The scene is depicted in a whimsical, storybook fantasy style with rich colors, intricate details, and a painterly, magical atmosphere.")](images/f7f4141c-a610-48b4-8e3c-c443227ed466_1024x1024.webp)

One of the problems I’ve run into with Kasm Workspaces is storage space. When creating a new Kasm environment, regardless of the size of the virtual machine or the VM’s storage space, Kasm always installs with 80GB of storage. With the wealth of containers available in the Kasm registries, 80GB disappears quickly.

At least for my scenario, where I’m hosting Kasm in a 200GB Ubuntu Server 24.04LTS VM, below are steps for allocating more storage. Note that commands, paths, variables, etc. may be different for your scenario. If you set up Kasm by following my previous tutorials, the below should be accurate, but is worth double-checking before copying and pasting commands in steps 5 and 6:

## Step 1: Verify available storage in Docker:

```
sudo df -h /var/lib/docker
```

[![](images/5cbf03aa-488e-483b-9422-22544cc713ed_697x61.png)](images/5cbf03aa-488e-483b-9422-22544cc713ed_697x61.png)

## Step 2: Check to see if Docker is on an LVM volume

Running the lsblk command will show the partitions… check to see if /var/lib/docker is shown as the mountpoint for an lvm partition. If configured as described in previous articles, this should be the case.

```
lsblk
```

[![](images/1a154c65-8e20-4829-ac40-4cfaf668317b_667x163.png)](images/1a154c65-8e20-4829-ac40-4cfaf668317b_667x163.png)

## Step 3: Check the LV name and path

Run this command to see the logical volume name and path… my path is /dev/ubuntu-vg/ubuntu-lv and the logical volume name is ubuntu-lv. You’ll need this info for steps 5 and 6.

```
sudo lvdisplay
```

[![](images/58ba3116-285a-43ee-97c4-6464f30f2161_681x334.png)](images/58ba3116-285a-43ee-97c4-6464f30f2161_681x334.png)

## Step 4: Check the free space in the volume group

```
sudo vgdisplay
```

[![](images/f55f302f-1da6-4ceb-b48b-045c374238fb_638x410.png)](images/f55f302f-1da6-4ceb-b48b-045c374238fb_638x410.png)

## Step 5: Extend the LV

As long as there is free space, we can extend the logical volume. Note that the volume group, volume name, and volume path may be different for you, so check this against your results from Step 3 above.

```
sudo lvextend -l +100%FREE /dev/ubuntu-vg/ubuntu-lv
```

[![](images/45453194-6a92-4715-b967-c6f143b7bccf_859x81.png)](images/45453194-6a92-4715-b967-c6f143b7bccf_859x81.png)

## Step 6: Resize the file system.

Again, be sure that your volume path matches your system:

```
 sudo resize2fs /dev/ubuntu-vg/ubuntu-lv
```

[![](images/215d616f-8453-4e9c-b0d9-de694447c527_876x109.png)](images/215d616f-8453-4e9c-b0d9-de694447c527_876x109.png)

Step 7: Verify that everything worked:

```
df -h /var/lib/docker
```

Before:

[![](images/08395c49-6604-4508-8855-569c45f57607_700x65.png)](images/08395c49-6604-4508-8855-569c45f57607_700x65.png)

After:

[![](images/dec0dddb-7757-4005-aba5-bcc4a45b66ce_707x62.png)](images/dec0dddb-7757-4005-aba5-bcc4a45b66ce_707x62.png)

And for the true test, check your Admin → Workspaces → Registry page in Kasm to check the available storage. I didn’t have to restart the VM or Container or any services… the storage just update automatically.

[![](images/73d4421d-f3c9-41c9-b066-a94e41f7b8cb_297x120.png)](images/73d4421d-f3c9-41c9-b066-a94e41f7b8cb_297x120.png)
