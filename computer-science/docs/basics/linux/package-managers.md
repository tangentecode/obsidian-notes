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
> to perform most operations with **pacman** 
### yay or paru

