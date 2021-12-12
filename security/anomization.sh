echo "STARTING ANONIMITY..."
sudo openvpn open-vpn/OpenVPN/vpnbook-pl226-tcp443.ovpn
sudo systemctl tor start
sudo systemctl privoxy start

sudo systemctl tor status
sudo systemctl privoxy status
echo "ANONIMITY COMPLETED"
