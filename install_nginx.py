import os
import tarfile
import requests
from read_yaml import read_yaml_file

download_dir = os.path.expanduser("~/downloads")
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

conf = read_yaml_file()


def download_nginx(conf: dict):
    for base_url in conf.nginx.url:
        nginx_url = f"{base_url}nginx-{conf.nginx.version}.tar.gz"
        source_file = os.path.join(download_dir,
                                   f"nginx-{conf.nginx.version}.tar.gz")

        print(f"正在尝试从 {nginx_url} 下载")
        print(f"到 {source_file} 中...", end="\n")
        response = requests.get(nginx_url, timeout=5)

        if response.status_code == 200:
            with open(source_file, 'wb') as file:
                file.write(response.content)
            print(f"Nginx {conf.nginx.version}下载完成。保存到{source_file}", end="\n")
            return source_file
        else:
            print(f"从{nginx_url}(HTTP{response.status_code})下载失败...")
            print("正在尝试下一个URL...", end="\n")

    raise Exception(f"从所有提供的url下载Nginx {conf.nginx.version}失败。", end="\n")


def disposition_nginx(conf: dict):
    try:
        source_file = download_nginx(conf)
        print(f"解压{source_file}...")
        with tarfile.open(source_file, 'r:gz') as tar:
            tar.extractall(path=download_dir)
        print(f"Nginx{conf.nginx.version}解压完成.", end="\n")

        print("安装开发工具包中...")
        os.system('dnf group install "Development Tools" -y')
        print("开发工具包安装完成.", end="\n")

        print("安装Nginx必要库中...")
        os.system(
            "dnf install openssl openssl-devel pcre pcre-devel zlib zlib-devel -y"
        )
        print("必要库安装完成.", end="\n")

        source_dir = os.path.join(download_dir, f"nginx-{conf.nginx.version}")
        os.chdir(source_dir)
        print(f"在{os.getcwd()}中配置Nginx {conf.nginx.version}...")
        os.system(f"./configure --prefix={conf.nginx.bin} --with-http_ssl_module --with-http_gzip_static_module --with-http_stub_status_module --with-pcre")

        print(f"编译Nginx {conf.nginx.version}")
        os.system("make")

        print(f"安装Nginx {conf.nginx.version}")
        os.system("make install")
        os.chdir("..")
    except Exception as e:
        return e

    print(f"完成Nginx {conf.nginx.version}的安装.")
    print(f"安装目录为：{conf.nginx.bin}")


if __name__ == "__main__":
    disposition_nginx()
    # print(conf)
