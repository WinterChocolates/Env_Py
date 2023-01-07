# software-installation

提供服务器和termux的git2.9.5，python3.9.10，ffmpeg的安装

**注意：termux使用编译安装比较慢**

## 安装教程

使用前请安装git **（安装git2.9.5时自动卸载）**

```shell
# Ubuntu
apt-get install -y git
# CentOS
yum install -y git
```

下载

``` sh
git clone https://gitee.com/WinterChocolates/software-installation.git
```

使用

```shell
chmod +x software-installation/*
bash software-installation/install.sh
```

退出请按Ctrl+C



## 解决内容

1.发送`#全部更新`时提示获取时间失败

```shell
解决方法：安装git更高版本
```

2.不会在服务器上安装python更高版本

```shell
本脚本使用编译安装，安装python3.9.10版本
```



[爱发电](https://afdian.net/a/WinterChocolates)

可以提供你的需求，让作者编写