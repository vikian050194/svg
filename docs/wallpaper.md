# Wallpaper

Generate and update wallpaper on startup

```bash
touch /etc/systemd/user/wallpaper.service 
```

Example of service file content

```
[Unit]
Description=Generate and update wallpaper

[Service]
Type=oneshot
ExecStart=/home/<user>/git/svg/wallpaper.py

[Install]
WantedBy=multi-user.target
```

Try to start service

```
systemctl --user start wallpaper.service
```

If everything is fine then enable it

```
systemctl --user enable wallpaper.service
```