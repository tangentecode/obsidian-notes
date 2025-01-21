## Systemctl

- on Arch use the `systemctl`  [command](bash.md) like this:
```shell 

sudo systemctl enable name.service
sudo systemctl disable name.service
sudo systemctl start name.service
sudo systemctl stop name.service
sudo systemctl restart name.service
sudo systemctl status name.service


systemctl —user enable name.service
systemctl —user disable name.service
systemctl —user start name.service
systemctl —user stop name.service
systemctl —user restart name.service
systemctl —user status name.service
```

- need to use `sudo` to if you want modify services on the local computer and not the user