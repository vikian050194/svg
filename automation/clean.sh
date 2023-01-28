DIR="$HOME/svg"
rm "$DIR/configs"
# rm -rf "$DIR"

systemctl stop svg.timer
systemctl disable svg.timer
systemctl disable svg.service

sudo rm automation/systemd/svg.service
sudo rm automation/systemd/svg.timer

systemctl daemon-reload
