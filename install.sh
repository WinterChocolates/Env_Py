#!/bin/bash
if [ -f /etc/redhat-release ]
then release="centose"
elif cat /etc/issue | grep -q -E -i "debian"
then release="debian"
elif cat /etc/issue | grep -q -E -i "ubuntu"
then release="ubuntu"
elif cat /etc/issue | grep -q -E -i "centos|red hat|redhat"
then release="centos"
elif cat /proc/version | grep -q -E -i "debian"
then release="debian"
elif cat /proc/version | grep -q -E -i "ubuntu"
then release="ubuntu"
elif cat /proc/version | grep -q -E -i "centos|red hat|redhat"
then release="centos"
fi

if [ ${release} = "centose" ]
then bash "centos/index.sh"
fi

if [ ${release} = "centos" ]
then bash "centos/index.sh"
fi

if [ ${release} = "ubuntu" ]
then bash "ubuntu/index.sh"
fi

if [ ${release} = "debian" ]
then bash "debian/index.sh"
fi
