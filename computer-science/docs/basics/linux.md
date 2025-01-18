## Pre-installation

- download ISO (e.g. [Arch Linux](https://archlinux.org/))
- burn to flash drive (on Windows use [Rufus](https://rufus.ie/de/)) 
- boot into it using **Boot Manager** or **BIOS/UEFI**
- run `ping google.com` [command](bash.md) to check internet connection
- run `lsblk` to view **drives** and there corresponding **partition**
- to make the installation process easier run `archinstall`

## Archinstall

1. **Language:**
	- select preferred language (en)

2. **Locales:**
	 - select preferred keyboard layout (en) 

3. **Mirrors:**
	- select nearest download mirror (de)

4. **Disk configuration:**
	- select the **best effort partition layout option**
	- use `ext4` file system because its the most stable

5. **Disk encryption:**
	- just don't touch it the option

6. **Bootloader:**
	- select `Systemd` if you have one `os` installed on your system
	- select `Grub` if you want to multiboot

7. **Unified kernel images:**
	- skip this option

8. **Hostname:**
	- type a name for you computer
	- this is not the user name!

9. **Root password:**
	- this password is used to confirm any root operation (e.g. every `sudo` command)
	- preferably a short password if you dont want type in a long password every time

10. **User profiles:**
	- make one profile which should also be a **superuser**

11. **Profile:**
	- for convenience choose **Desktop** sand select **KDE**
	- If you have an **Nvidia Graphics Card** select driver and select **Nvidia (propriatery)**