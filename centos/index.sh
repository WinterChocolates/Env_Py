#!/bin/bash
echo "欢迎使用软件安装脚本"
echo
echo "==================================="
echo "1.安装python3.9  2.卸载python3.9"
echo "3.安装git2.9.5   4.卸载git2.9.5"
echo "5.安装ffmpeg     6.卸载ffmpeg"
echo "==================================="
echo
while read -p "请输入以上序号：" num
do
	case $num in
		1)
			yum remove -y python3*
			yum update -y && yum install -y gcc make tar wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel python-devel libffi-devel
			wget -P /usr/local/src https://repo.huaweicloud.com/python/3.9.10/Python-3.9.10.tgz
			cd /usr/local/src/
			tar -zxvf Python-3.9.10.tgz
			cd Python-3.9.10
			./configure --prefix=/usr/local/python3
			make && make install
			echo -e '# python3.9.0\nexport PYTHON_HOME=/usr/local/python3\nexport PATH=$PYTHON_HOME/bin:$PATH' >> /etc/profile
			source /etc/profile
			python3 --version
			pip3 --version
			rm -rf /usr/local/src/*
			break
			;;
		2)
			rm -rf /usr/local/python3
			rm -rf /usr/local/bin/python3
			rm -rf /usr/local/bin/pip3
			sed -i '/# python3.9.0/d' /etc/profile
			sed -i '/PYTHON_HOME/d' /etc/profile
			source /etc/profile
			echo "卸载成功"
			break
			;;
		3)
			yum update -y && yum install -y gcc make tar wget curl-devel expat-devel openssl-devel zlib-devel perl-ExtUtils-MakeMaker
			yum -y remove git
			wget -P /usr/local/src https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.39.0.tar.xz
			cd /usr/local/src/
			tar -xf git-2.39.0.tar.xz
			cd /usr/local/src/git-2.39.0
			./configure --prefix=/usr/local/git
			make && make install
			ln -s /usr/local/git/bin/git /usr/local/bin/git
			source /etc/profile
			git --version
			rm -rf /usr/local/src/*
			echo "安装成功"
			break
			;;
		4)
			rm -rf /usr/local/git
			rm -rf /usr/local/bin/git
			source /etc/profile
			echo "卸载成功"
			break
			;;
		5)
			yum update -y && yum install -y epel-release
			yum config-manager -set-enabled PowerTools
			yum install -y yum-utils
			yum-config-manager --add-repo=https://negativo17.org/repos/epel-multimedia.repo
			yum install -y ffmpeg
			ffmpeg -version
			echo "安装成功"
			break
			;;
		6)
			yum remove -y ffmpeg
			echo "卸载成功"
			break
			;;
		*)
			echo "输入序号不为显示中的，请重新输入"
			continue
			;;
	esac
done
