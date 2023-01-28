DIR="$HOME/svg"
mkdir "$DIR"
ln -s "$PWD/configs" "$DIR"

/usr/bin/gsettings set org.gnome.desktop.background picture-uri "$DIR/latest.svg"

sudo cp automation/systemd/svg.service /lib/systemd/system/
sudo cp automation/systemd/svg.timer /lib/systemd/system/

systemctl daemon-reload

systemctl enable svg.timer
systemctl start svg.timer
systemctl status svg.timer

# systemctl enable svg.service
# systemctl start svg.service
systemctl status svg.service

sudo chmod 777 /lib/systemd/system/svg.service
sudo chmod 777 /lib/systemd/system/svg.timer
