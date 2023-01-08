# software-installation

提供服务器和termux的git2.9.5，python3.9.10，ffmpeg的安装

**注意：termux使用编译安装比较慢**

## 安装教程

> 使用前请安装git **（安装git2.9.5时自动卸载）**
>

```shell
# Ubuntu
apt-get install -y git
# CentOS
yum install -y git
```

> 下载
>

``` sh
git clone https://gitee.com/WinterChocolates/software-installation.git
```

> 使用
>

```shell
chmod +x software-installation/*
cd software-installation/
bash software-installation/install.sh
```

> 退出请按Ctrl+C
>

**注意python安装后需要使用python3和pip3**

## 手动安装

### python安装

- #### Ubuntu

  > 因为ubuntu的python3.6系统需要用所以不建议卸载，推荐使用下面的方法 **（想卸载的自行百度）**
  >

  ```shell
  rm -rf /usr/bin/python3
  rm -rf /usr/bin/pip3
  ```

  > 安装需要用的依赖
  >

  ```shell
  apt update && apt install -y wget gcc tar make build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev libbz2-dev liblzma-dev sqlite3 libsqlite3-dev tk-dev uuid-dev libgdbm-compat-dev
  ```

  > 官网速度太慢了，这是使用[华为镜像站](https://mirrors.huaweicloud.com/home)的python编译包
  >

  ```shell
  # 下载
  wget https://repo.huaweicloud.com/python/3.9.10/Python-3.9.10.tgz
  
  # 解压
  tar -xf Python-3.9.10.tgz
  
  # 进入目录并编译
  cd Python-3.9.10
  ./configure --prefix=/usr/local/python3
  make && make install
  ```

  > 配置系统环境
  >

  ```shell
  echo -e '# python3.9.10\nexport PYTHON_HOME=/usr/local/python3\nexport PATH=$PYTHON_HOME/bin:$PATH' >> /etc/profile
  
  source /etc/profile
  ```

  > 查看python配置
  >

  ```shell
  python3 --version
  pip3 --version
  ```

- #### CentOS

  > centos的python3.6并不推荐卸载，系统环境也需要使用，推荐使用下面的方法 **（想卸载的自行百度）**
>

  ```shell
  rm -rf /usr/bin/python3
  rm -rf /usr/bin/pip3
  ```

> 安装需要用的依赖
  >

  ```shell
yum update -y && yum install -y gcc make tar wget zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel python-devel libffi-devel
  ```

  > 官网速度太慢了，这是使用[华为镜像站](https://mirrors.huaweicloud.com/home)的python编译包
  >

  ```shell
  # 下载
  wget https://repo.huaweicloud.com/python/3.9.10/Python-3.9.10.tgz
  
  # 解压
  tar -xf Python-3.9.10.tgz
  
  # 进入目录并编译
  cd Python-3.9.10
./configure --prefix=/usr/local/python3
  make && make install
  ```

  > 配置系统环境 **（这里不能使用软链接，原因：poetry会出不来）**
  >

  ```shell
echo -e '# python3.9.10\nexport PYTHON_HOME=/usr/local/python3\nexport PATH=$PYTHON_HOME/bin:$PATH' >> /etc/profile
  
source /etc/profile
  ```

  > 查看python版本
  >

  ```shell
  python3 --version
  pip3 --version
  ```

  

### git安装

- #### Ubuntu

  > 因为Ubuntu能下载到的版本只用2.17，这个版本推荐升级，首先卸载已经安装的git
  >

  ```shell
  apt remove -y git
  ```

  > 安装需要的依赖
  >

  ```shell
  apt update && apt install -y wget gcc make gzip tar wget libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev
  ```

  > 暂且没找到国内源，用的是官方源
  >

  ```shell
  # 下载
  wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.xz
  
  # 解压
  tar -xf git-2.9.5.tar.xz
  
  # 进入目录并编译
  cd git-2.9.5
  ./configure --prefix=/usr/local/git
  make && make install
  ```

  > 配置git环境（下面方法任选其一）
  >

  ```shell
  # 配置系统环境
  echo -e '# Git2.9.5\nexport PATH=/usr/local/git/bin:$PATH' >> /etc/profile
  source /etc/profile
  
  #配置软链接
  ln -s /usr/local/git/bin/git /usr/local/bin/git
  ```

  > 查看git版本
  >

  ```shell
  git --version
  ```

  

- #### CentOS
  > 因为centos能下载到的版本只用1.8，这个版本肯定要升级，首先卸载已经安装的git
>

  ```shell
  yum remove -y git
  ```

> 安装需要的依赖
  >

  ```shell
yum update -y && yum install -y gcc make tar wget curl-devel expat-devel openssl-devel zlib-devel perl-ExtUtils-MakeMaker
  ```

  > 暂且没找到国内源，用的是官方源
  >

  ```shell
  # 下载
  wget https://mirrors.edge.kernel.org/pub/software/scm/git/git-2.9.5.tar.xz
  
  # 解压
  tar -xf git-2.9.5.tar.xz
  
  # 进入目录并编译
  cd git-2.9.5
./configure --prefix=/usr/local/git
  make && make install
  ```

  > 配置git环境（下面方法任选其一）
  >

  ```shell
  # 配置系统环境(不推荐会报错)
  echo -e '# Git2.9.5\nexport PATH=/usr/local/git/bin:$PATH' >> /etc/profile.d/git.sh
  source /etc/profile

  #配置软链接
ln -s /usr/local/git/bin/git /usr/local/bin/git
  ```

  > 查看git版本
  >

  ```shell
  git --version
  ```


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