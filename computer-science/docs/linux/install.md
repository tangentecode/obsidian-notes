# Install

## Pre-installation

- download ISO (e.g. [Arch Linux](https://archlinux.org/) via [Torrent](https://www.qbittorrent.org/download)) 
- burn to flash drive (on Windows use [Rufus](https://rufus.ie/de/)) 
- boot into it using **Boot Manager** or **BIOS/UEFI**
- run `ping google.com` [command](bash.md) to check internet connection
- run `lsblk` to view **drives** and there corresponding **partition**
- to make the installation process easier run `archinstall`

## Archinstall Script


### Configuration:

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
	- preferably a short password if you don't want type in a long password every time

10. **User profiles:**
	- make one profile which should also be a **superuser**

11. **Profile:**
	- for convenience choose **Desktop** sand select **KDE**
	- If you have an **Nvidia Graphics Card** select driver and select **Nvidia (proprietary)**
	- Leave the **greeter** as **default**

12. **Audio:**
	- Select **Pipewire** because its very modern and stable

13. **Kernel:**
	- standard **linux** kernel

14. **Network configuration:**
	- Select **NetworkManager** if you use **KDE Plasma** or **Gnome**

15. **Additional Packages:**
	- Define multiple packages to install; separated by spaces
	- Example: `neovim git obsidian`

16. **Optional Repositorys:**
	- Leave default

17. **Timezone:**
	 - Select current Timezone

18. **Automatic Time Sync:**
	 - Leave **NTP** on

### Install

1. Hit **install** or **save configuration**
2. After complete say no to the `chroot` environment
3. If you see that the installation was successful type `sudo reboot`
4. Before the computer starts booting again remove the flash drive
5. Login to **KDE** with the user name and password specified during the configuration process (**Tip:** type in `root` as user name and and your root password if you want to perform multiple root actions for example after the installation) 

## Manual Install

- For a manual install, if you for exams le want a more customised partition layout refer to the guide on the [arch Linux](archlinux.org ) website
