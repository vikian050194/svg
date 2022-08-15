# svg

[![MIT license][license-badge]][license-url]
[![Maintenance status][status-badge]][status-url]

## Generate and update wallpaper on startup

```bash
touch /etc/systemd/user/wallpaper.service 
```

Example of service file content

```
[Unit]
Description=Generate and update wallpaper

[Service]
Type=oneshot
ExecStart=/home/kirill/git/svg/wallpaper.py

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

[status-url]: https://github.com/vikian050194/svg/pulse
[status-badge]: https://img.shields.io/github/last-commit/vikian050194/svg.svg

[license-url]: https://github.com/vikian050194/svg/blob/master/LICENSE
[license-badge]: https://img.shields.io/github/license/vikian050194/svg.svg