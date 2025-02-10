# Package-managers

## Arch

### Pacman

-  **official** and **save** package manager
-  install packages like this:

```shell 
pacman -S _package_name1_ _package_name2_ ...
```

- sync and install packages to avoid **dependency conflicts** like this:

```shell
pacman -Sy _package_name1_ _package_name2_ ...
```

- remove packages 

```shell
pacman -R _package_name1_ _package_name2_ ...
```

- update all packages

```shell
pacman -Syu
```

Parameters:

- S stands for sync
- y is for refresh (local cache)
- u is for system update
- r stands for remove 

> to perform most operations with **pacman** you need to be root

### Yay or Paru

- **AUR Helper** to install unofficial user-made **Packages** 
- **BUT** they can also install official **Arch Packages**

> **ATTENTION:** These user-made dont have any checks for viruses or just bad code

```shell 
yay -S _package_name1_ _package_name2_ ...
```

- sync and install packages to avoid **dependency conflicts** like this:

```shell
yay -Sy _package_name1_ _package_name2_ ...
```

- remove packages 

```shell
yay -R _package_name1_ _package_name2_ ...
```

- update all packages

```shell
yay -Syu
```

> Dont requires `sudo` previeliges

