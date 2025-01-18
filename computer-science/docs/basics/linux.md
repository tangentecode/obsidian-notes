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
	- just dont touch it the option

6. 