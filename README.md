# Hyperspace

net.ipv6.conf.all.disable_ipv6 = 0

net.ipv6.conf.default.disable_ipv6 = 0

echo -e "net.ipv6.conf.all.disable_ipv6 = 0\nnet.ipv6.conf.default.disable_ipv6 = 0\nkernel.panic = 10" | sudo tee /etc/sysctl.conf > /dev/null


sudo sysctl -p

wget -O Hyperspace.sh https://github.com/ljj0522/Hyperspace/raw/refs/heads/main/Hyperspace.sh && sed -i 's/\r$//' Hyperspace.sh && chmod +x Hyperspace.sh && ./Hyperspace.sh

source /root/.bashrc && bash Hyperspace.sh

aios-cli hive select-tier 3

aios-cli hive points

---------------END-------------------------------------------

